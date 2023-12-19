# process-nitta

実験データの解析ライブラリ

## 使い方

インストール

```bash
pip install process-nitta
```

実行例

```python
from process_nitta.instron import InstronSample

sample = InstronSample(
    file_path="../test/csv/instron.csv",
    width_mm=4,
    thickness_μm=100,
    length_mm=10,
    speed_mm_per_min=10,
)

sample.get_stress_strain_df()
```

[example](https://github.com/nitta-lab-polymer/process-nitta/tree/main/example)に実行例を置いていますが、Gooogle Colaboratoryのpythonランタイムバージョンが3.10であり、実行できません。
