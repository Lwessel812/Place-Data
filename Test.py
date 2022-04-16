import pandas as pd
import os

# 160353103-4 rows

os.system ('cls' if os.name == 'nt' else 'clear')
print("==========================================\n")
filename = "SmallSet.csv"

data = pd.read_csv(filename)

#print(f"Original {filename} CSV Data: \n")
#print(data)

#data.drop("user_id", inplace=True, axis=1)

#print("\nCSV Data after deleting the column 'user_id':\n")
#print(data)

#data.to_csv("SmallerCutSet.csv", index=False)

#print(f"# Rows: {len(data.index)}")
