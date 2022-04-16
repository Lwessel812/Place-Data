import pandas as pd
import os

# 160353103-4 rows

os.system ('cls' if os.name == 'nt' else 'clear')
print("==========================================\n")
filename = "SmallerCutSet.csv"

data = pd.read_csv(filename)

#data.sort_values("timestamp", kind = "mergesort")
data.replace(to_replace=[" UTC", "2022-04-", "2022-03-", "2022-02-", "2022-01-"], value=["", "", "", "", ""], inplace=True, regex=True)


data.to_csv("SmallerCut2Set.csv", index=False)
