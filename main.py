import pandas as pd
from plotData import plotCircumplex
from plotData import plotCircumplex_byImageFileName
from importData import importIAPS
from importData import filterIAPS
from extraMath import calculateCoordinateFromAngle
from selectImage import importSelectedList


# import Data
# declare file path (put r in front to convert normal string to raw string)
# IAPs_file_path = r"C:\Users\DSPLab\Research\IAPSdata\AllSubjects_1-20.txt"
IAPs_file_path = r"C:\Users\DSPLab\Research\IAPSdata\AllSubjects_1-20.txt"
IAPS_df = importIAPS(IAPs_file_path)

""" Plot using list of indexes """
# file path to list csv file
list_file_path = r"C:\Users\DSPLab\Research\IAPSdata\IAPS_selectedList_Moderate.csv"
# Get targeted index of rows
indexOfDescription = importSelectedList(list_file_path)
# Plot circumplex model of affect
plotCircumplex_byImageFileName(IAPS_df,amp=100,indexs=indexOfDescription)


""" Plot using radius and angle """
# # Set the target list
# targetList = [(3,15)]
# # create indexOfDescription from lists
# indexOfDescription = []
# for (a,b) in targetList:
#     r,angle = a,b
#     (x,y) = calculateCoordinateFromAngle(r,angle)      
#     resultList = filterIAPS(IAPS_df,x,y,width=0.4)
#     for i in resultList:
#         indexOfDescription.append(i)

# # Select rows by list of index
# IAPS_filtered_df = IAPS_df.loc[indexOfDescription,:]
# print(IAPS_filtered_df)
# # Plot circumplex model of affect
# plotCircumplex(IAPS_df,amp=100,indexs=indexOfDescription)


"""  Old code with pin point method  """

# # get list of indexs by pin point location (df,valence,arousal,width)
# indexOfDescription = filterIAPS(IAPS_df,9,9,width=0.2)

# # Select rows by list of index
# IAPS_filtered_df = IAPS_df.loc[indexOfDescription,:]
# print(IAPS_filtered_df)
# # Plot circumplex model of affect
# plotCircumplex(IAPS_df,amp=100,indexs=indexOfDescription)
