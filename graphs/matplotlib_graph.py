from typing import Tuple, List

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from shapes.value_reader import ValueReader


class ObjectGrapher:
    def __init__(self):
        fig = plt.figure()
        self.ax = fig.add_subplot(111, projection='3d')
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.set_zlabel('z')
        self.line_width = 0.2
        self.edge_color = 'black'
        self.face_color = 'blue'
        self.alpha = 0.1

    def render_plot(self):
        plt.show()

    def save_fig(self, file_name: str):
        plt.savefig(file_name)

    def set_config(self, line_width, edge_color, face_color, alpha):
        self.line_width = line_width
        self.edge_color = edge_color
        self.face_color = face_color
        self.alpha = alpha

    def plot_objects(self, objects: List[Tuple]):
        for vertices, faces in objects:
            object_values = ValueReader(vertices, faces).get_values()
            polygon = Poly3DCollection(object_values,
                                       facecolors=self.face_color,
                                       linewidths=self.line_width,
                                       edgecolors=self.edge_color,
                                       alpha=self.alpha)

            self.ax.add_collection3d(polygon)

    def set_axes_sizes(self, lower_bound, upper_bound):
        self.ax.set_xlim3d(lower_bound, upper_bound)
        self.ax.set_ylim3d(lower_bound, upper_bound)
        self.ax.set_zlim3d(lower_bound, upper_bound)


class Graph2D:
    def __init__(self):
        fig, ax = plt.subplots()
        self.ax = ax
        self.colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

    def render_plot(self):
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        plt.gca().invert_xaxis()
        plt.show()

    def save_fig(self, file_name: str):
        plt.savefig(file_name)

    def plot_objects(self, objects: List[Tuple]):
        for vertices, faces in objects:
            polygons = ValueReader(vertices, faces).get_values2d()
            color = self.decide_color()
            for face in polygons:
                points = [(p[1], p[2]) for p in face]
                p = Polygon(points, fc=color, ec=color, fill=False)
                self.ax.add_patch(p)

    def decide_color(self):
        return self.colors.pop(0)
