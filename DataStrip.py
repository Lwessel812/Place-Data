import pandas as pd
import os, math, time

# 160353103 rows with ending
# 160033094 rows w/o pixel ending
# 320010 pixles placed during ending

start_time = time.time()

os.system ('cls' if os.name == 'nt' else 'clear')

filename = "PlaceData.csv"

data = pd.read_csv(filename)

time = (time.time() - start_time)
print(f"{time} seconds to load")
print(f"~{math.floor(time / 60)} minutes to load")

print(f"{len(data.index)} rows")

data.drop("user_id", inplace=True, axis=1)

data.replace(to_replace=[" UTC", "2022-04-04", "2022-04-03", "2022-04-02", "2022-04-01", ":", "#"], value=["", "4", "3", "2", "1", "", ""], inplace=True, regex=True)

#data = data[data["timestamp"].str.contains("05 ", regex=True) == False]

data.replace(to_replace=["#"], value=[""], inplace=True, regex=True)

data.to_csv("ProcessedSet.csv", index=False)

time = (time.time() - start_time)
print(f"{time} seconds to finish")
print(f"{math.floor(time / 60)} minutes to finish")
print(f"{len(data.index)} rows")
