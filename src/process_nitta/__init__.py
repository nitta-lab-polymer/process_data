import subprocess

from process_nitta.agis import AGISSample as AGISSample
from process_nitta.csv_config import ColumnStrEnum as ColumnStrEnum
from process_nitta.csv_config import CSVConfig as CSVConfig
from process_nitta.csv_config import encodingStr as encodingStr
from process_nitta.dma import DMASample as DMASample
from process_nitta.instron import InstronSample as InstronSample
from process_nitta.ir_nicolet import IRNICOLETSample as IRNICOLETSample
from process_nitta.models import Base as Base
from process_nitta.models import Sample as Sample
from process_nitta.raman import RamanSample as RamanSample

subprocess.run(["pip install -qU process-nitta 2>/dev/null"], shell=True)
