import constants

# converts simplified grid coordinates into pixel locations 
def setLocation(x, y, objectSize):
    # establish the mid point in pixels of the object
    xpix = (x * constants.GRID_SIZE) + (constants.GRID_SIZE/2)
    ypix = (y * constants.GRID_SIZE) + (constants.GRID_SIZE/2)

    # the pygame draw.rect() function needs the top left corner pixel of the shape.
    # convert the midpoint to the top left corner and return that
    topLeftX = xpix - (objectSize/2)
    topLeftY = ypix - (objectSize/2)

    return topLeftX, topLeftY