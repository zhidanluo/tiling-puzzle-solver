import numpy as np


class MaxtrixRotator(object):
    def __init__(self, angle = 0, direction = 'left'):
        self.angle = angle
        self.direction = direction
                 
    def rotation(self, matrix):
        if self.direction == 'left':
            if self.angle%360 == 0:
                return matrix
            elif self.angle%360 == 90:
                return np.rot90(matrix, 1)
            elif self.angle%360 == 180:
                return np.rot90(matrix, 2)
            elif self.angle%360 == 270:
                return np.rot90(matrix, 3)
            else:
                print("unvalid angle rotator")
        else:
            if self.angle%360 == 0:
                return matrix
            elif self.angle%360 == 90:
                return np.rot90(matrix, -1)
            elif self.angle%360 == 180:
                return np.rot90(matrix, -2)
            elif self.angle%360 == 270:
                return np.rot90(matrix, -3)
            else:
                print("unvalid angle rotator")
            
    def flip(self, matrix):
        return np.fliplr(matrix)