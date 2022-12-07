import numpy as np
from typing import List


class CameraBase:
    def __init__(self, eye: np.ndarray, at: np.ndarray):
        self.eye = eye
        self.at = at
        self.base = np.zeros((3, 3))

    def get_camera_base(self):
        self.__get_i()
        self.__get_k()
        self.__get_j()
        return self.base

    def __get_i(self):
        n = self.eye - self.at
        n = normalize(n)
        self.base[0] = n

    def __get_j(self):
        j = np.cross(self.base[0], self.base[2])
        self.base[1] = j

    def __get_k(self):
        aux = np.array([0, 0, 2])
        projection = project_a_on_b(aux, self.base[0])
        k = aux - projection
        self.base[2] = k


class ConvertBase:
    @staticmethod
    def convert_objects(objects: List[np.ndarray], new_base: np.ndarray) -> List[np.ndarray]:
        for i in range(len(objects)):
            objects[i] = ConvertBase.convert_base(objects[i], new_base)
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
