from extraMath import calculateCoordinateFromAngle
from importData import filterIAPS
from importData import importIAPS

# # set x coordination
# r = 2
# print(calculateCoordinateFromAngle(r,30))

# r,angle = a,b
# coord = calculateCoordinateFromAngle(r,angle)
# indexOfDescription = list(set(indexOfDescription + filterIAPS(IAPS_df,coord[0],coord[1],width=0.1)))

# IAPs_file_path = r"C:\Users\DSPLab\Research\IAPSdata\AllSubjects_1-20.txt"
IAPs_file_path = r"C:\Research\AllSubjects_1-20.txt"
IAPS_df = importIAPS(IAPs_file_path)
result = filterIAPS(IAPS_df,6,6,width=0.2)
print(result)
result = result.reshape((5,1))
print(result)
