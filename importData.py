import numpy as np
import pandas as pd
import matplotlib.pyplot as pltv

# declare file path (put r in front to convert normal string to raw string)
file_path = r"C:\Users\DSPLab\Research\IAPSdata\AllSubjects_1-20.txt"

# import the data
IAPS_header = []
IAPS_df = pd.read_csv(file_path,skiprows=7,sep="\t",header=None)
IAPS_df
print(IAPS_df.head(5))
