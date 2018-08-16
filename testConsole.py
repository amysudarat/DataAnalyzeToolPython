from extraMath import calculateCoordinateFromAngle

# set x coordination
x = 6.5
y = calculateCoordinateFromAngle(x,90)
y = float(format(y,'.2f'))
print(y)