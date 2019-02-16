import numpy as np


class Square:

    def __init__(self, x_off, y_off):
        self.x_off = x_off
        self.y_off = y_off

    def hit(self, bm_val):
        if 0 > bm_val[0] or bm_val[0] > self.x_off or 0 > bm_val[1] or bm_val[1] > self.y_off:
            return True
        else:
            return False

    def clip(self, bm_val):
        xdiff1 = np.abs(1-bm_val[0])
        xdiff2 = np.abs(bm_val[0])
        ydiff1 = np.abs(1-bm_val[1])
        ydiff2 = np.abs(bm_val[1])
        diffs = (xdiff1, xdiff2, ydiff1, ydiff2)
        i = np.argmin(diffs)

        if i == 0:
            bm_val[0] = 1
            return bm_val
        if i == 1:
            bm_val[0] = 0
            return bm_val
        if i == 2:
            bm_val[1] = 1
            return bm_val
        if i == 3:
            bm_val[1] = 0
            return bm_val

