import subprocess

program_list = ['notebooks/extract_data.py',
                'notebooks/clean_data.py']

for program in program_list:
    subprocess.run(['python', program])
    print("Finished: " + program)