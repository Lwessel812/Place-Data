import pandas as pd
import os, time

# 160353103-4 rows

start_time = time.time()

os.system ('cls' if os.name == 'nt' else 'clear')

#filename = "SmallSet.csv"

#data = pd.read_csv(filename)

#data.drop("user_id", inplace=True, axis=1)
#data.replace(to_replace=[" UTC", "2022-04-", "2022-03-", "2022-02-", "2022-01-"], value=["", "", "", "", ""], inplace=True, regex=True)

#data.to_csv("SmallCutSet.csv", index=False)

print(f"{(time.time() - start_time)} seconds")
