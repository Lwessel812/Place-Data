import pandas as pd
import os

# 160353103-4 rows

os.system ('cls' if os.name == 'nt' else 'clear')
print("==========================================\n")
filename = "CutSet.csv"

data = pd.read_csv(filename)
