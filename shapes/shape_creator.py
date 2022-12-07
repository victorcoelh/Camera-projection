import numpy as np
from typing import Tuple


class ShapeCreator:
    @classmethod
    def generic(cls, polygon, *args) -> Tuple[np.ndarray, np.ndarray]:
        if polygon == 'cube':
            return ShapeCreator.cube(*args)
        if polygon == 'parallelepiped':
            return ShapeCreator.parallelepiped(*args)
        if polygon == 'pyramid':
            return ShapeCreator.square_base_pyramid(*args)
        if polygon == 'pyramid stub':
            return ShapeCreator.pyramid_stub(*args)
        if polygon == 'cylinder':
            return ShapeCreator.cylinder(*args)

    @classmethod
    def cube(cls, edge_size) -> Tuple[np.ndarray, np.ndarray]:
        s = edge_size
        x = [0, s, s, 0, 0, s, s, 0]
        y = [s, s, 0, 0, s, s, 0, 0]
        z = [s, s, s, s, 0, 0, 0, 0]
        cube = np.array([x, y, z])

        faces = np.array([
            (0, 1, 2, 3),
            (4, 5, 6, 7),
            (3, 2, 6, 7),
            (2, 1, 5, 6),
            (1, 5, 4, 0),
            (0, 4, 7, 3)
        ])
        return cube, faces

    @classmethod
    def parallelepiped(cls, height, width, depth) -> Tuple[np.ndarray, np.ndarray]:
        h, w, d = height, width, depth
        # The axes are in this particular order for the sake of making the graph easier to understand.
        x = [d, d, d, d, 0, 0, 0, 0]
        y = [0, w, w, 0, 0, w, w, 0]
        z = [h, h, 0, 0, h, h, 0, 0]
        parallelepiped = np.array([x, y, z])

        faces = np.array([
            (0, 1, 2, 3),
            (4, 5, 6, 7),
            (4, 0, 3, 7),
            (5, 1, 2, 6),
            (5, 1, 0, 4),
            (6, 2, 3, 7)
        ])
        return parallelepiped, faces

    @classmethod
    def square_base_pyramid(cls, height, edge_size):
        h, e = height, edge_size
        x = [0, e, e, 0, e/2]
        y = [e, e, 0, 0, e/2]
        z = [0, 0, 0, 0, h]
        pyramid = np.array([x, y, z])

        faces = np.array([
            (0, 1, 2, 3),
            (1, 2, 4, 4),
            (3, 2, 4, 4),
            (0, 3, 4, 4),
            (0, 1, 4, 4)
        ])
        return pyramid, faces

    @classmethod
    def pyramid_stub(cls, height, bottom_edge_size, top_edge_size):
        h, b, t = height, bottom_edge_size, top_edge_size
        gap = (b - t) / 2
        x = [0, b, b, 0, gap, gap + t, gap + t, gap]
        y = [b, b, 0, 0, gap + t, gap + t, gap, gap]
        z = [0, 0, 0, 0, h, h, h, h]
        stub = np.array([x, y, z])

        faces = np.array([
            (0, 1, 2, 3),
            (4, 5, 6, 7),
            (3, 2, 6, 7),
            (2, 1, 5, 6),
            (1, 0, 4, 5),
            (3, 0, 4, 7)
        ])
        return stub, faces

    @classmethod
    def cylinder(cls, height, radius, slices):
        cylinder = ShapeCreator.__generate_circles(height, radius, slices)
        last_face = np.empty(slices, dtype='int64')
        last_face.fill(-1)
        last_face[0:4] = (slices-1, 0, slices, -1)

        faces = [
            range(0, slices),
            range(slices, slices * 2),
            last_face]

        for i in range(0, slices - 1):
            face = np.empty(slices, dtype='int64')
            j = i + slices
            face.fill(j)
            face[0:4] = (i, i+1, j+1, j)
            faces.append(face)

        return cylinder, np.array(faces)

    @classmethod
    def __generate_circles(cls, height, radius, slices) -> np.ndarray:
        x = []
        y = []
        z = [height] * slices

        interval = np.pi*2 / slices
        for i in range(0, slices):
            a = interval * i
            current_x = np.cos(a) * radius
            current_y = np.sin(a) * radius
            x.append(current_x)
            y.append(current_y)
        # generating the second circle
        x = x * 2
        y = y * 2
        z.extend([0] * slices)
        return np.array([x, y, z])
