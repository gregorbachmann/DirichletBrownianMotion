import numpy as np


class BrownianMotion2D:

    def __init__(self,
                 b_0,
                 dt,
                 boundary):
        self.b_0 = b_0
        self.current = b_0
        self.dt = dt
        self.t = 0
        self.boundary = boundary
        self.hit_time = None
        self.hitting = False
        self.hitting_value = None

    def sample_one_step(self):
        normal_1 = np.random.normal(0, scale=np.sqrt(self.dt), size=1)
        normal_2 = np.random.normal(0, scale=np.sqrt(self.dt), size=1)
        self.current[0] += normal_1
        self.current[1] += normal_2
        self.t += self.dt

    def hitting_time(self):
        self.hitting = self.boundary.hit(self.current)
        if self.hitting:
            self.hit_time = self.t
            self.hitting_value = self.current

    def run_bm(self):
        while not self.hitting:
            self.sample_one_step()
            self.hitting_time()
