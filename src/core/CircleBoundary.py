import numpy as np


class Circle:

    def __init__(self, radius, center):
        self.radius = radius
        self.center = center

    def hit(self, bm_val):
        dist = np.sqrt((bm_val[0]-self.center[0])**2 + (bm_val[1]-self.center[1])**2)
        if dist <= self.radius:
            return False
        else:
            return True

    def clip(self, bm_val):
        norm = np.sqrt(bm_val[0]**2 + bm_val[1]**2)
        clipped = bm_val/norm * self.radius
        return clipped