import subprocess

program_list = ['notebooks/extract_data.py',
                'notebooks/clean_data.py',
                'notebooks/equally_weighted_portfolio.py',
                'notebooks/green_less_green_portfolio.py']

for program in program_list:
    subprocess.run(['python', program])
    print("Finished: " + program)