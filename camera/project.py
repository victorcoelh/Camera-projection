from typing import List

import numpy as np


class Projection2d:
    def __init__(self, solids: List[np.ndarray]):
        self.solids = solids

    def project_solids(self, r: float, d: float) -> List[np.ndarray]:
        for i in range(len(self.solids)):
            solid = self.solids[i]
            size = solid.shape[1]
            solid = np.append(solid, [np.ones(size)], 0)
            self.solids[i] = self.project_single_solid(solid, r, d)
        return self.solids

    def project_single_solid(self, solid: np.ndarray, r: float, d: float):
        transpose = solid.T
        for i in range(len(transpose)):
            vector = transpose[i]
            x = vector[0]
            m = np.array([
                (0, 0, 0, d),
                (0, d/(r*x), 0, 0),
                (0, 0, d/x, 0),
                (0, 0, 0, 1)
            ])
            # m = np.array([
            #     (d/(r*x), 0, 0, 0),
            #     (0, d/x, 0, 0),
            #     (0, 0, 0, d),
            #     (0, 0, 0, 1)
            # ])
            transpose[i] = m @ vector
        solid = transpose.T
        return np.delete(solid, -1, 0)
