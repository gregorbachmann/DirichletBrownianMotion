import numpy as np
from src.core.BrownianMotionCloud import BMCloud
from mpl_toolkits.mplot3d import Axes3D


class Dirichlet:

    def __init__(self, grid, dt, boundary, f, num_bm):
        self.grid = grid
        self.dt = dt
        self.boundary = boundary
        self.f = f
        self.num_bm = num_bm
        self.values = np.zeros(shape=num_bm)

    def get_values(self):
        for i in range(len(self.grid[0, :])):
            grid_val = self.grid[:, i].copy()
            cloud = BMCloud(b_0=grid_val, dt=self.dt, boundary=self.boundary, num_bm=self.num_bm, f=self.f)
            self.values[i] = cloud.get_mean()

    def plot(self):
        Axes3D.plot_surface(X=self.grid[:, 0], Y=self.grid[:, 1], Z=self.values)



