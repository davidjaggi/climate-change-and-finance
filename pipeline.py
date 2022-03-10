import subprocess
from src.utils.get_path import get_root_path

ROOT_PATH = get_root_path()

pipeline = {
    "notebooks/data/extract_data.py": True,
    "notebooks/data/clean_data.py": True,
    "notebooks/portfolios/equally_weighted_portfolio.py": True,
    "notebooks/portfolios/green_less_green_portfolio.py": True,

}

def run_pipeline():
    for script, run in pipeline.items():
        if run:
            subprocess.run(["python", f"{ROOT_PATH}/{script}"])