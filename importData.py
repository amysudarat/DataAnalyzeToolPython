import numpy as np
import pandas as pd
import matplotlib.pyplot as pltv

# declare file path (put r in front to convert normal string to raw string)
file_path = r"C:\Users\DSPLab\Research\IAPSdata\AllSubjects_1-20.txt"

# import data without header and skil till line 7
IAPS_df = pd.read_csv(file_path,skiprows=7,sep="\t",header=None)
# Add header manually
IAPS_df.columns = ["Description","IAPS","Val_mn","Val_sd","Arou_mn","Arou_sd","Dom1mn","Dom1sd","Dom2mn","Dom2sd","Set"]
# Select only the first eight column
IAPS_df = IAPS_df.iloc[:,0:5]
print(IAPS_df)
