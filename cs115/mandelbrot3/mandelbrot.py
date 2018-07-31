# mandelbrot.py
# Lab 9
#
# Name: Zachary Talarick
#I pledge my honor that I have abided by the stevens honor system. ztalaric

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:
def mult(c,n):
    """multiplies c and n without using * notation"""
    b = 0
    for i in range(n):
        b += c
        i += 1
    return b

def update(c, n):
    """ update starts with z=0 and runs z = z**2 + c
 for a total of n times. It returns the final z. """
    z = 0
    for i in range(n):
        z = z**2 + c
        i += 1
    return z

def inMSet(c, n):
    '''takes a complext numbber c and
integer n returns a bool demonstrating if c is in the mandelbrot set'''
    z = 0
    for i in range(n):
        z = z**2 + c
        i += 1
        if abs(z) > 2:
            return False
    return True

def weWantThisPixel( col, row ):
    """ a function that returns True if we want
    the pixel at col, row and False otherwise
    """
    if col%10 == 0 or row%10 == 0:
        return True
    else:
        return False

def scale( pix, pixelMax, floatMin, floatMax):
    """ scale takes in
     pix, the CURRENT pixel column (or row)
     pixMax, the total # of pixel columns
     floatMin, the min floating-point value
     floatMax, the max floating-point value
     scale returns the floating-point value that
     corresponds to pix
     """

    return (pix / pixelMax) * (floatMax - floatMin) + floatMin 

def test():
    """ a function to demonstrate how
    to create and save a png image
    if you change and to or in the function above it makes the image a grid
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
    
    # create a loop in order to draw some pixels

    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
                
    # we looped through every image pixel; we now write the file
    image.saveFile()

def mset():
    """ creates a 300x200 image of the Mandelbrot set
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
    
    # create a loop in order to draw some pixels
    
    for col in range(width):
        for row in range(height):
            # here is where you will need
            # to create the complex number, c!
            c = scale(col, width, -2.0, 1.0) + scale(row, height, -1.0, 1.0) * 1j
            if inMSet( c, 25 ) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()

mset()

