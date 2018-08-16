import pandas as pd
from plotData import plotCircumplex
from importData import importIAPS
from importData import filterIAPS
from extraMath import calculateCoordinateFromAngle

# import Data
# declare file path (put r in front to convert normal string to raw string)
# IAPs_file_path = r"C:\Users\DSPLab\Research\IAPSdata\AllSubjects_1-20.txt"
IAPs_file_path = r"C:\Research\AllSubjects_1-20.txt"
IAPS_df = importIAPS(IAPs_file_path)

# Three set of picture samples: Extreme, Moderate, Mild: Form (r,angle)
Extreme = [(3.6,3),(3,34),(3.6,54),(3,71),(2.5,90),(3.6,143),
          (2,149),(2.6,154),(3.6,173),(2,180),(1,190),(1,220),(2,234),
          (2,317),(2,327),(2,332)]
# Moderate = [(3.6,3),(3.6,34),(3.6,54),(3.6,71),(3.6,90),(3.6,143),
#           (3.6,149),(3.6,154),(3.6,173),(3.6,180),(3.6,190),(3.6,220),(3.6,234),
#           (3.6,317),(3.6,327),(3.6,332)]
# Mild = [(3.6,3),(3.6,34),(3.6,54),(3.6,71),(3.6,90),(3.6,143),
#           (3.6,149),(3.6,154),(3.6,173),(3.6,180),(3.6,190),(3.6,220),(3.6,234),
#           (3.6,317),(3.6,327),(3.6,332)]

# create indexOfDescription from lists
indexOfDescription = []
for (a,b) in Extreme:
    r,angle = a,b
    (x,y) = calculateCoordinateFromAngle(r,angle)      
    resultList = filterIAPS(IAPS_df,x,y,width=0.2)
    for i in resultList:
        indexOfDescription.append(i)
    


# Select rows by list of index
IAPS_filtered_df = IAPS_df.loc[indexOfDescription,:]
print(IAPS_filtered_df)
# Plot circumplex model of affect
plotCircumplex(IAPS_df,amp=100,indexs=indexOfDescription)


"""  Old code with pin point method  """

# # get list of indexs by pin point location (df,valence,arousal,width)
# indexOfDescription = filterIAPS(IAPS_df,9,9,width=0.2)
# # Select rows by list of index
# IAPS_filtered_df = IAPS_df.loc[indexOfDescription,:]
# print(IAPS_filtered_df)
# # Plot circumplex model of affect
# plotCircumplex(IAPS_df,amp=100,indexs=indexOfDescription)
