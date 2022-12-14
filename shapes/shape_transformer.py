import numpy as np


class ShapeTransformer:
    def __init__(self, vertices: np.ndarray):
        self.vertices = vertices
        self.m = np.identity(4)
        self.__turn_vertices_homogenous()

    def apply_transformations(self) -> np.ndarray:
        homogenous_vertices = self.m @ self.vertices
        return np.delete(homogenous_vertices, -1, 0)

    def escalate(self, x_ratio, y_ratio, z_ratio):
        transformation = np.array([
            (x_ratio, 0, 0, 0),
            (0, y_ratio, 0, 0),
            (0, 0, z_ratio, 0),
            (0, 0, 0, 1)
        ])
        self.m = self.m @ transformation

    def translate(self, x, y, z):
        transformation = np.array([
            (1, 0, 0, x),
            (0, 1, 0, y),
            (0, 0, 1, z),
            (0, 0, 0, 1)
        ])
        self.m = self.m @ transformation

    def rotate(self, axis, angle):
        cos = np.cos(angle)
        sin = np.sin(angle)
        if axis == 'x':
            rotation = [
                (1, 0, 0, 0),
                (0, cos, -sin, 0),
                (0, sin, cos, 0),
                (0, 0, 0, 1)
            ]
        elif axis == 'y':
            rotation = [
                (cos, 0, sin, 0),
                (0, 1, 0, 0),
                (-sin, 0, cos, 0),
                (0, 0, 0, 1)
            ]
        else:
            rotation = [
                (cos, -sin, 0, 0),
                (sin, cos, 0, 0),
                (0, 0, 1, 0),
                (0, 0, 0, 1)
            ]
        transformation = np.array(rotation)
        self.m = self.m @ transformation

    def __turn_vertices_homogenous(self):
        size = self.vertices.shape[1]
        self.vertices = np.append(self.vertices, [np.ones(size)], 0)
