import pandas as pd
df = pd.read_csv('https://statbel.fgov.be/sites/default/files/files/opendata/deathday/DEMO_DEATH_OPEN.zip',sep='|')
df['DATE'] = pd.to_datetime(df['DT_DATE'], dayfirst = True)
sterfte_per_dag = pd.pivot_table(df, index = 'DATE', values = ['MS_NUM_DEATH'], aggfunc='sum')
sterfte_per_dag.to_csv('sterfte_per_dag.csv', index=True)
