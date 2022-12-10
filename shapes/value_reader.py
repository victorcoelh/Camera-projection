import numpy as np


class ValueReader:
    def __init__(self, shape: np.ndarray, faces: np.ndarray):
        self.shape = shape
        self.faces = faces

    def get_values(self):
        faces = []
        for face in self.faces:
            current_face = []
            for point in face:
                x = self.shape[0][point]
                y = self.shape[1][point]
                z = self.shape[2][point]
                point = [x, y, z]
                current_face.append(point)
            faces.append(current_face)
        return np.array(faces)

    def get_values2d(self):
        faces = np.append(self.faces, [self.faces[0]], 0)
        points = self.faces.flatten()
        np.append(points, points[0])
        size = len(points) - 1
        lines = []
        for i in range(0, size, 2):
            a = points[i]
            b = points[i+1]
            point_a = (self.shape[0][a], self.shape[1][a], self.shape[1][a])
            point_b = (self.shape[0][b], self.shape[1][b], self.shape[2][b])
            lines.append((point_a, point_b))
        return lines
