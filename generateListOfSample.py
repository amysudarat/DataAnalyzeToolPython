import pandas as pd
from selectImage import importSelectedList 
from importData import importIAPS 

def main():

    # import Data
    # declare file path (put r in front to convert normal string to raw string)
    # IAPs_file_path = r"C:\Users\DSPLab\Research\IAPSdata\AllSubjects_1-20.txt"
    IAPs_file_path = r"C:\Users\DSPLab\Research\IAPSdata\AllSubjects_1-20.txt"
    IAPS_df = importIAPS(IAPs_file_path)

    # file path to csv file
    filePath = r"C:\Users\DSPLab\Research\IAPSdata\IAPS_selectedList_Moderate.csv"
    # Get targeted List of picture number
    fileNameList = importSelectedList(filePath)

    # Select rows that data in column IAPS match the list file
    selectedIAPS_df = IAPS_df.loc[IAPS_df["IAPS"].isin(fileNameList)]
    # print(selectedIAPS_df)
    # print(len(selectedIAPS_df))

    # Create an export DataFrame
    selectedIAPS_df_export = pd.DataFrame()
    selectedIAPS_df_export["imageID"] = selectedIAPS_df["IAPS"]
    selectedIAPS_df_export["slideNumber"] = [x for x in range(len(selectedIAPS_df.index))]
    selectedIAPS_df_export["pictureSet"] = ["Moderate" for x in range(len(selectedIAPS_df.index))] #Change the name of set here
    selectedIAPS_df_export["ValenceMean"] = selectedIAPS_df["Val_mn"]
    selectedIAPS_df_export["ArousalMean"] = selectedIAPS_df["Arou_mn"]
    selectedIAPS_df_export["ValenceSD"] = selectedIAPS_df["Val_sd"]
    selectedIAPS_df_export["ArousalSD"] = selectedIAPS_df["Arou_sd"]
    selectedIAPS_df_export["picture"] = generateImageFileName(selectedIAPS_df["IAPS"])
    print(selectedIAPS_df_export.head())
    

def generateImageFileName(listInput):
    result = []
    for elem in listInput:
        result.append(str(int(elem))+".jpg")
    return result




# To start the program in main 
# (have to place at last so every function above get recoginized first)
if __name__ == "__main__":
    main()