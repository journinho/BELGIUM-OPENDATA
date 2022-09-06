import pandas as pd
df = pd.read_csv('https://statbel.fgov.be/sites/default/files/files/opendata/Indexen%20per%20productgroep/CPI%20All%20groups.zip', sep='|', low_memory=False)
df['day'] = 1
df['DATE'] = pd.to_datetime(dict(year=df.NM_YR, month=df.NM_MTH, day=df.day), format="%Y-%m-%d")
df['YR_MTH'] = df['DATE'].dt.strftime('%Y-%m')
level4 = df[df["NM_CD_COICOP_LVL"] == 4] 
prijzen = pd.pivot_table(level4, index = 'TX_COICOP_NL_LVL4', columns = 'YR_MTH', values = 'MS_CPI_INFL', aggfunc='sum').reset_index()
prijzen.dropna(inplace=True)
inflatie_per_productgroep = pd.concat([prijzen.iloc[:,:1],prijzen.iloc[:,-120:]],axis=1) # Puts them together row wise
inflatie_per_productgroep.rename(columns={'TX_COICOP_NL_LVL4': 'Productgroep', 'YR_MTH': 'Index'}, inplace=True)
inflatie_per_productgroep['Inflatie'] = inflatie_per_productgroep.iloc[:,-1:]
inflatie_per_productgroep.to_csv('inflatie_per_productgroep.csv')
