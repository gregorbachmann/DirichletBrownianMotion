from src.core.BrownianMotion2D import BrownianMotion2D


class BMCloud:

    def __init__(self, b_0, dt, boundary, num_bm, f):
        self.b_0 = b_0
        self.dt = dt
        self.boundary = boundary
        self.num_bm = num_bm
        self.hitting_values = []
        self.f = f

        self.bms = []

    def run_all_bms(self):
        self.hitting_values = []
        b_0 = self.b_0.copy()
        for _ in range(self.num_bm):
            bm = BrownianMotion2D(b_0, b_0, self.dt, self.boundary)
            bm.run_bm()
            self.hitting_values.append(bm.hitting_value)

    def get_mean(self):
        self.run_all_bms()
        current = 0
        for val in self.hitting_values:
            val = self.boundary.clip(val)
            current += self.f(val[0], val[1])
        current /= self.num_bm
        return current

