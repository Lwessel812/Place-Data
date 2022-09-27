# This file counts how many instances there are of R/Place users who placed a pixel that was the same color, of the pixel that was already there.

import pandas as pd
import os, math, time

# 160353103 rows with whiteout ending
# 160033094 rows w/o whiteout ending
# 320010 pixles placed during ending
# Count: 26140145
# Time: 130700725 minutes
# Years: 248.6696
# Days: 90764.3924
# Hours: 2178345.4167

start_time = time.time()

os.system ("cls" if os.name == "nt" else "clear") # Clear console

filename = "C:\Temp\PlaceHistory\SortedSet.csv" # Name/Path of file being imported

data = pd.read_csv(filename) # Import file into Pandas dataframe

print(f"{(time.time() - start_time)} seconds to load")

Count = 0
Color = "FFFFFF" # Set color to white because the canvas started out completely white
Cords = "0,0"   # Starting with 0,0 as our coordinates 

for r in range (len(data.index)): # Loop through every line of the file
    if data.coordinate[r] == Cords: # Checks if the coordinate value @ row r is the same as our Cords variable, which after the first row will be the previous rows coordinates
        if data.pixel_color[r] == Color: # Checks if the color value @ row r is the same as our Color variable, which after the first row will be the previous rows color
            #print(f"line {r+1}, and {r+2}") 
            Count += 1 # Increase counter by 1, because the color and coordinates were identical between rows
        else:
            Color = data.pixel_color[r] # If the colors werent the same, we need to update our variable to reflect the "previous" color
    else:
        Cords = data.coordinate[r] # If the coordinates werent the same, we need to update our variable to reflect the "previous" coordinate
        Color = data.pixel_color[r] # If the colors werent the same, we need to update our variable to reflect the "previous" color

time = (time.time() - start_time)
print(f"{time} seconds to finish")
print(f"~{math.floor(time / 60)} minutes to finish")

print(f"Count: {Count}")
print(f"Time: {Count * 5} minutes")
print(f"Time: {( Count * 5 ) / 60} Hours")
print(f"Time: {( Count * 5 ) / 1440} Days")
print(f"Time: {( Count * 5 ) / 525600} Years")
