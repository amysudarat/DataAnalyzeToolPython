import pandas as pd
from plotData import plotCircumplex
from importData import importIAPS
from importData import filterIAPS

# import Data
# declare file path (put r in front to convert normal string to raw string)
IAPs_file_path = r"C:\Users\DSPLab\Research\IAPSdata\AllSubjects_1-20.txt"
IAPS_df = importIAPS(IAPs_file_path)

# get list of indexs by pin point location (df,valence,arousal,width)
indexOfDescription = filterIAPS(IAPS_df,5.5,3.5,width=0.2)
# Select rows by list of index
IAPS_filtered_df = IAPS_df.loc[indexOfDescription,:]
print(IAPS_filtered_df)
# Plot circumplex model of affect
plotCircumplex(IAPS_df,amp=100,indexs=indexOfDescription)
