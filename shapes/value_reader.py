import numpy as np


class ValueReader:
    def __init__(self, shape, faces):
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
