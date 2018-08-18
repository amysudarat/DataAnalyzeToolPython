import pandas as pd
from plotData import plotCircumplex
from importData import importIAPS
from importData import filterIAPS
import shutil
from math import isnan

def main():
    # Get targeted dataframe
    # targetedIAPS = buildDataframe(3,6,0.1)
    # targetedIAPS = []
    # fileNameList = targetedIAPS["IAPS"].tolist()
    # fileNameList = [int(i) for i in fileNameList]
    # print(fileNameList)

    # # Copy all the selected picture to the targeted folder
    # for i in fileNameList:
    #     # Declare src and dest   
    #     src = r"C:\Research\IAPS 1-20 Images\\" + str(i) + r".jpg"
    #     dest = r"C:\Research\IAPS 1-20 Images\\Sample_extreme\\" + str(i) + r".jpg"
    #     copyFile(src,dest)
    importSelectedList()

def importSelectedList():
    filePath = r"C:\Research\IAPS_selectedList_Extreme.csv"
    selectedList = pd.read_csv(filePath,sep=",",index_col=0)   
    print(selectedList)
    selectedList = selectedList[:10]
    selectedList = selectedList.drop(selectedList.columns[9],axis=1)
    totalList = []
    for i in range(0,selectedList.shape[1]):
        for j in selectedList.iloc[:,i]:
            if not isnan(j):
                totalList.append(int(j))

    print(totalList)
    print("Number of item: " + str(len(totalList)))
    

def buildDataframe(v,a,w):
    # import Data
    # declare file path 
    # (put r in front to convert normal string to raw string)
    IAPs_file_path = r"C:\Users\DSPLab\Research\IAPSdata\AllSubjects_1-20.txt"
    IAPS_df = importIAPS(IAPs_file_path)

    # get list of indexs by pin point location (df,valence,arousal,width)
    indexOfDescription = filterIAPS(IAPS_df,v,a,width=w)
    # Select rows by list of index
    IAPS_filtered_df = IAPS_df.loc[indexOfDescription,:]
    return IAPS_filtered_df


def copyFile(src, dest):
    """
    copy file with error handler
    """
    try:
        shutil.copy(src,dest)
    except shutil.Error as e:
        print("Error: " + str(e))
    except IOError as e:
        print("Error: " + e.strerror)

# To start the program in main 
# (have to place at last so every function above get recoginized first)
if __name__ == "__main__":
    main()
