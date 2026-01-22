import os
import pandas as pd

data_path = "sales_analysis/data/sales.csv"

if os.path.exists(data_path):
    print(f"Found {data_path}")
else:
    print(f"Cannot find {data_path}")
    
df = pd.read_csv(data_path)


df['total'] = df['quantity']* df['price']

os.makedirs('output' , exist_ok=True)

df.to_json('sales_analysis/output/sales_data.json' , orient='records' , indent=2)
df.to_csv('sales_analysis/output/sales_data.csv' , index=False)
df.to_excel('sales_analysis/output/sales_data.xlsx' ,index=False)

print(df)

