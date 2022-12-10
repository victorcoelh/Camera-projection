import numpy as np
from typing import List
from shapes.shape_transformer import ShapeTransformer


class CameraBase:
    def __init__(self, eye: np.ndarray, at: np.ndarray):
        self.eye = eye
        self.at = at
        self.base = np.zeros((3, 3))

    def get_camera_base(self):
        self.__get_i()
        self.__get_k()
        self.__get_j()
        print(self.base)
        return self.base

    def __get_i(self):
        n = self.at - self.eye
        n = normalize(n)
        self.base[0] = n

    def __get_j(self):
        j = np.cross(self.base[0], self.base[2])
        j = normalize(j)
        self.base[1] = j

    def __get_k(self):
        aux = np.array([0, 0, 1])
        projection = project_a_on_b(aux, self.base[0])
        k = aux - projection
        k = normalize(k)
        self.base[2] = k


class ConvertBase:
    @staticmethod
    def convert_objects(objects: List[np.ndarray], new_base: np.ndarray, eye: np.ndarray) -> List[np.ndarray]:
        for i in range(len(objects)):
            converted = ConvertBase.convert_base(objects[i], new_base)
            transformer = ShapeTransformer(converted)
            transformer.translate(-eye[0], -eye[1], -eye[2])
            objects[i] = transformer.apply_transformations()
        return objects

    @staticmethod
    def convert_base(matrix: np.ndarray, new_base: np.ndarray):
        inverted_base = np.linalg.inv(new_base)
        return inverted_base @ matrix


def normalize(vector: np.ndarray) -> np.ndarray:
    magnitude = abs(np.linalg.norm(vector))
    normalized = vector / magnitude
    return normalized


def project_a_on_b(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    projection = (np.dot(a, b) / np.dot(b, b)) * b
    return projection
