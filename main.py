import pandas as pd
from plotData import plotCircumplex
from importData import importIAPS
from importData import filterIAPS
from extraMath import calculateCoordinateFromAngle

# import Data
# declare file path (put r in front to convert normal string to raw string)
IAPs_file_path = r"C:\Users\DSPLab\Research\IAPSdata\AllSubjects_1-20.txt"
IAPS_df = importIAPS(IAPs_file_path)

# set x coordination
x = 3 
y = calculateCoordinateFromAngle(x,45)
y = float(format(y,'.2f'))
print(y)
# # get list of indexs by pin point location (df,valence,arousal,width)
# indexOfDescription = filterIAPS(IAPS_df,x,calculateCoordinateFromAngle(x,30),width=0.2)
# # Select rows by list of index
# IAPS_filtered_df = IAPS_df.loc[indexOfDescription,:]
# print(IAPS_filtered_df)
# # Plot circumplex model of affect
# plotCircumplex(IAPS_df,amp=100,indexs=indexOfDescription)
