import pandas as pd

from .csv_config import CSVConfig
from .models import Sample


class InstronSample(Sample):
    speed_mm_per_min: float
    freq_Hz: float = 0.05
    load_cell_max_N: int = 100
    load_cell_calibration_coef: float = 1
    max_Voltage: float = 10

    def trim_instron_df(self, df: pd.DataFrame, mean_range: int = 100) -> pd.DataFrame:
        df = df.copy()
        roll = pd.DataFrame(df["Voltage"].rolling(window=mean_range).mean().diff())

        start = (
            int(roll["Voltage"][mean_range : mean_range * 2].idxmax()) - mean_range + 1
        )  # 傾きが最大のところを探す
        end = int(roll["Voltage"].idxmin()) + 10

        result = df[start:end].reset_index(drop=True)
        result["Voltage"] = result["Voltage"] - result["Voltage"][0]  # 初期値を0にする

        return result

    def calc_stress_strain_df(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        area_mm2 = self.width_mm * self.thickness_μm / 1000
        speed_mm_per_sec = self.speed_mm_per_min / 60

        stress_Mpa = (
            self.load_cell_max_N
            / (self.load_cell_calibration_coef * self.max_Voltage)
            / area_mm2
            * df["Voltage"]
        )
        strain = speed_mm_per_sec * self.freq_Hz * df.index / self.length_mm

        strain_label = "Strain"  # type: ignore
        stress_label = "Stress_MPa"  # type: ignore
        return pd.DataFrame(
            {strain_label: strain, stress_label: stress_Mpa},
        )

    def get_stress_strain_df(self) -> pd.DataFrame:
        df = pd.read_csv(self.file_path, **CSVConfig().Instron().to_dict())
        return self.calc_stress_strain_df(self.trim_instron_df(df))
