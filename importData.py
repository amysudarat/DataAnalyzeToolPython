
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

def filterIAPS(IAPS_df,v,a,width=1):

    """
    return index of filtered dataframe for function plotIAPS
    # filter the dataframe using .apply()  axis=1 means to send row (this one use python syntax so logic symbol use 'and')
    # IAPS_df_filtered = IAPS_df[IAPS_df.apply(lambda x: x['Val_mn'] > 5 and x['Arou_mn'] > 5, axis=1)]

    # filter dataframe using logic mask (this one use panda syntax so bitwise symbol is use '&')
    # mn_range = [(8,7),(4,5),(3,3),(7,4)]
    # IAPS_df_filtered = pd.DataFrame()
    # for (v,a) in mn_range:
    #     Q1 = IAPS_df[((IAPS_df['Val_mn']> v )& (IAPS_df['Arou_mn']>a))]
    #     IAPS_df_filtered = IAPS_df_filtered.append(Q1)2
    """

    # Select rows that is fit in the condition df[True]
    tmp = IAPS_df[ (IAPS_df['Val_mn'] < v+width ) & ( IAPS_df['Val_mn'] >v-width)& ( IAPS_df['Arou_mn'] <a+width)& ( IAPS_df['Arou_mn'] >a-width)]
    # Get index of rows from filtered dataframe
    indexOfFiltered = tmp.index.values

    return indexOfFiltered

def checkRange(value,center,width):
    if center-width/2 <= value <= center+width/2:
        return True
    return False

def filterCornerIAPS(IAPS_df):
    IAPS_df_filtered = pd.DataFrame()
    Q1 = IAPS_df[((IAPS_df['Val_mn']> 7 )& (IAPS_df['Arou_mn']>7))]
    IAPS_df_filtered = IAPS_df_filtered.append(Q1)
    Q2 = IAPS_df[((IAPS_df['Val_mn']< 2 )& (IAPS_df['Arou_mn']>7))]
    IAPS_df_filtered = IAPS_df_filtered.append(Q2)
    Q3 = IAPS_df[((IAPS_df['Val_mn']< 3 )& (IAPS_df['Arou_mn']<4.5))]
    IAPS_df_filtered = IAPS_df_filtered.append(Q3)
    Q4 = IAPS_df[((IAPS_df['Val_mn']> 7 )& (IAPS_df['Arou_mn']<3))]
    IAPS_df_filtered = IAPS_df_filtered.append(Q4)

    return IAPS_df_filtered.index.values
    






