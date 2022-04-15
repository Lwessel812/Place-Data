import pandas as pd
import os

os.system ('cls' if os.name == 'nt' else 'clear')
print("==========================================\n")
filename = "SmallSet.csv"

data = pd.read_csv(filename)

#print(f"Original {filename} CSV Data: \n")
#print(data)

data.drop("user_id", inplace=True, axis=1)

#print("\nCSV Data after deleting the column 'user_id':\n")
#print(data)

data.to_csv("CutSet.csv", index=False)
