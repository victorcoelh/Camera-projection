import numpy as np


class Projection2d:
    def __init__(self, solids: list[np.ndarray]):
        self.solids = solids

    def project_solids(self, r: float, d: float):
        for i in range(len(self.solids)):
            solid = self.solids[i]
            size = solid.shape[1]
            solid = np.append(solid, [np.ones(size)], 0)
            self.solids[i] = self.project_single_solid(solid, r, d)
        return np.delete(self.solids, -1, 0)

    def project_single_solid(self, solid: np.ndarray, r: float, d: float):
        for vector in solid.T:
            x = vector[0]
            m = np.array([
                (d/(r*x), 0, 0, 0),
                (0, d/x, 0, 0),
                (0, 0, 0, d),
                (0, 0, 0, 1)
            ])
            vector = m @ vector
        return solid
