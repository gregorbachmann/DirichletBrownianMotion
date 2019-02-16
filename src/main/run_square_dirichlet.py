from Dirichlet import Dirichlet
import numpy as np
from SquareBoundary import Square


def main():
    # Grid creation
    nx, ny = (40, 40)
    x = np.linspace(0, 1, nx)
    y = np.linspace(0, 1, ny)
    grid = np.stack((x, y))
    dt = 0.01
    num_bm = 1000

    # Initialize boundary
    x_off = 1
    y_off = 1
    boundary = Square(x_off=x_off, y_off=y_off)

    # Get boundary value function
    def f(x, y):
        if x == 0 or x == 1:
            return y
        if y == 0 or y == 1:
            return x

    # Initial Dirichlet problem
    d = Dirichlet(grid, dt, boundary, f, num_bm)
    d.get_values()
    print(d.values)


if __name__ == "__main__":
    main()
