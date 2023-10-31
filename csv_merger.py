import os
import pandas as pd

master_df = pd.DataFrame()

for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        master_df = master_df._append(pd.read_csv(file))
        
master_df.to_csv('master_tax_file_all.csv', index=False)
