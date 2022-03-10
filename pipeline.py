import subprocess
from src.utils.get_path import get_root_path

ROOT_PATH = get_root_path()

pipeline = {
    "notebooks/data/extract_data.py": True,
    "notebooks/data/clean_data.py": True,
    "notebooks/data/extract_shock_data.py": True,
    "notebooks/portfolios/equally_weighted_portfolio.py": True,
    "notebooks/portfolios/green_less_green_portfolio.py": True,
    "notebooks/portfolios/paris_agreement_stats.py": True,
    "notebooks/data/create_discount_data.py": True,

}

def run_pipeline():
    for script, run in pipeline.items():
        if run:
            print(f"Running {script}")
            subprocess.run(["python", f"{ROOT_PATH}/{script}"])

if __name__ == "__main__":
    run_pipeline()