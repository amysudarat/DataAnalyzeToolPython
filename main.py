import pandas as pd
from plotData import plotCircumplex
from importData import importIAPS

# import Data
# declare file path (put r in front to convert normal string to raw string)
IAPs_file_path = r"C:\Users\DSPLab\Research\IAPSdata\AllSubjects_1-20.txt"
IAPS_df = importIAPS(IAPs_file_path)

# plot project
plotCircumplex(IAPS_df,amp=120)