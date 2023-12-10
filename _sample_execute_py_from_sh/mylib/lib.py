import pandas as pd

def load_jobs_dataframe(filename:str):
    df_csv = pd.read_csv(f'~/_codes/sample/data/{filename}', header=0)
    # df_csv[0:1]
    return df_csv

# load_jobs_dataframe()
