# This file strips unnecessary data from the csv file

import pandas as pd
import os, math, time

start_time = time.time()

os.system ("cls" if os.name == "nt" else "clear") # Clear console

filename = "C:\Temp\PlaceHistory\PlaceData.csv" # Name/Path of file being imported

data = pd.read_csv(filename) # Import file into Pandas dataframe

print(f"{(time.time() - start_time)} seconds to load")

print(f"{len(data.index)} rows") # Print the number of rows in the file

data.drop("user_id", inplace=True, axis=1) # Strips user_id data out, I didnt need this

data.replace(to_replace=[" UTC", "2022-04-04", "2022-04-03", "2022-04-02", "2022-04-01", ":", "#"], value=["", "4", "3", "2", "1", "", ""], inplace=True, regex=True) # Stripping any data that is identical between every row, ounces save pounds

data.to_csv("C:\Temp\PlaceHistory\ProcessedSet.csv", index=False) # Save the new stripped file to another file

time = (time.time() - start_time)
print(f"{time} seconds to finish")
print(f"{math.floor(time / 60)} minutes to finish")
