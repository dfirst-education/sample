import pandas as pd
import sys
from mylib import lib

if __name__ == '__main__':
    for idx, arg in enumerate(sys.argv):
        print(f'arg[{idx}]: {arg}')

    load_file_name = sys.argv[1]
    df_jobs = lib.load_jobs_dataframe(load_file_name)
    print(df_jobs[0:1])
