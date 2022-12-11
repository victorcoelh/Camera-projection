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
        polygons = []
        for face in self.faces:
            polygon = []
            for point in face:
                x = self.shape[0][point]
                y = self.shape[1][point]
                z = self.shape[2][point]
                current_point = [x, y, z]
                polygon.append(current_point)
            polygons.append(polygon)
        return polygons

