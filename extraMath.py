import math

<<<<<<< HEAD

def calculateCoordinateFromAngle(coorX,angle):
    '''
    return the coordinate of y from angle in degrees
    '''
    coorX=- 4.5
    coorY = coorX*math.sin(math.radians(angle))
    coorY = float(format(coorY,'.2f'))+5
    return 

=======
def calculateCoordinateFromAngle(r,angle):
    '''
    r= radius, angle= angle in degrees
    return the coordinate of x,y from angle(in degrees) 
    circumplex's origin is translated from (0,0) to (4.5,4.5)
    the coordinate of x,y in unit circle that turn seta angle
    (r*cos@ +a),(r*sin@+b)
    '''
    coorX = r*math.cos(math.radians(angle))+4.5
    coorX = float(format(coorX,'.2f'))
    coorY = r*math.sin(math.radians(angle))+4.5
    coorY = float(format(coorY,'.2f'))
    return (coorX, coorY)
    
>>>>>>> ec91de9686c4c1a42a26b784e1d33e503502fc7c
