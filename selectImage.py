import pandas as pd
from plotData import plotCircumplex
from importData import importIAPS
from importData import filterIAPS
import shutil

def main():
    # Get targeted dataframe
    targetedIAPS = buildDataframe(3,6,0.1)
    fileNameList = targetedIAPS["IAPS"].tolist()
    fileNameList = [int(i) for i in fileNameList]
    print(fileNameList)

    # Copy all the selected picture to the targeted folder
    for i in fileNameList:
        # Declare src and dest   
        src = r"C:\Users\DSPLab\Research\IAPSdata\IAPS 1-20 Images\\" + str(i) + r".jpg"
        dest = r"C:\Users\DSPLab\Research\IAPSdata\IAPS 1-20 Images\\Sample1\\" + str(i) + r".jpg"
        copyFile(src,dest)

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
