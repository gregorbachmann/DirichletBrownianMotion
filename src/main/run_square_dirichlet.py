from src.core.Dirichlet import Dirichlet
import numpy as np
from src.core.SquareBoundary import Square


def main():
    # Grid creation
    nx, ny = (40, 40)
    x = np.linspace(0.1, 0.9, nx)
    y = np.linspace(0.1, 0.9, ny)
    grid = np.stack((x, y))
    dt = 0.0000001
    num_bm = 100000

    # Initialize boundary
    x_off = 1
    y_off = 1
    boundary = Square(x_off=x_off, y_off=y_off)

    # Get boundary value function
    def f(x, y):
        if x == 0:
            return y
        if x == 1:
            return 1 + y
        if y == 0:
            return x
        if y == 1:
            return 1 + x

    # Initial Dirichlet problem
    d = Dirichlet(grid, dt, boundary, f, num_bm)
    d.get_values()
    print(d.values)


if __name__ == "__main__":
    main()
