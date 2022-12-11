import numpy as np


class CenterGetter:
    def __init__(self, solids):
        self.solids = solids

    def get_center(self):
        means = []
        for solid in self.solids:
            mean = np.mean(solid, axis=1)
            means.append(mean)
        return np.mean(means, axis=0)
