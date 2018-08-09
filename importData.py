
import pandas as pd
from plotData import plotCircumplex

def importIAPS(file_path):

    # import data without header and skil till line 7
    IAPS_df = pd.read_csv(file_path,skiprows=7,sep="\t",header=None)
    # Add header manually
    IAPS_df.columns = ["Description","IAPS","Val_mn","Val_sd","Arou_mn","Arou_sd","Dom1mn","Dom1sd","Dom2mn","Dom2sd","Set"]
    # Select only the first eight column
    IAPS_df = IAPS_df.iloc[:,0:6]
    return IAPS_df
    



