import math


def calculateCoordinateFromAngle(coorX,angle):
    '''
    return the coordinate of y from angle in degrees
    '''
    coorX=- 4.5
    coorY = coorX*math.sin(math.radians(angle))
    coorY = float(format(coorY,'.2f'))+5
    return 

