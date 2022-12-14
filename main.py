import numpy as np

from shapes.shape_creator import ShapeCreator
from shapes.shape_transformer import ShapeTransformer
from shapes.center_of_mass import CenterGetter
from graphs.matplotlib_graph import ObjectGrapher, Graph2D
from camera.camera_base import CameraBase, ConvertBase
from camera.project import Projection2d
from camera.vision_volume import VolumeFilter


def create_and_position_cube():
    cube, cube_faces = ShapeCreator.cube(4)
    cube_transformer = ShapeTransformer(cube)
    cube_transformer.translate(0, 1, 0)
    return cube_transformer.apply_transformations(), cube_faces


def create_and_position_pyramid():
    pyramid, pyramid_faces = ShapeCreator.square_base_pyramid(5, 5)
    pyramid_transformer = ShapeTransformer(pyramid)
    pyramid_transformer.translate(4.5, 5, 0)
    return pyramid_transformer.apply_transformations(), pyramid_faces


def create_and_position_parallelepiped():
    parallelepiped, parallelepiped_faces = ShapeCreator.parallelepiped(3, 3, 5)
    para_transformer = ShapeTransformer(parallelepiped)
    para_transformer.translate(5, -10, -10)
    return para_transformer.apply_transformations(), parallelepiped_faces


def create_and_position_stub():
    stub, stub_faces = ShapeCreator.pyramid_stub(4, 4, 2)
    stub_transformer = ShapeTransformer(stub)
    stub_transformer.translate(5.5, -6, -6)
    return stub_transformer.apply_transformations(), stub_faces


def create_and_position_cylinder():
    cylinder, cylinder_faces = ShapeCreator.cylinder(5, 1, 2, 16)
    cylinder_transformer = ShapeTransformer(cylinder)
    cylinder_transformer.translate(3, -5, -5)
    return cylinder_transformer.apply_transformations(), cylinder_faces


def test_transformations():
    cube, cube_faces = ShapeCreator.cube(4)
    cube_transformer = ShapeTransformer(cube)
    cube_transformer.rotate('y', np.pi/8)
    cube_transformer.escalate(1, 2, 1)
    cube_transformer.translate(1, 1, 1)
    cube = cube_transformer.apply_transformations()

    solids = [cube]
    faces = [cube_faces]
    objects = zip(solids, faces)

    graph = ObjectGrapher()
    graph.set_axes_sizes(-10, 10)
    graph.set_config(line_width=0.2, edge_color='black', face_color='blue', alpha=0.1)
    graph.plot_objects(objects)
    graph.render_plot()


def main():
    # Create solids
    cube, cube_faces = create_and_position_cube()
    parallelepiped, parallelepiped_faces = create_and_position_parallelepiped()
    pyramid, pyramid_faces = create_and_position_pyramid()
    stub, stub_faces = create_and_position_stub()
    cylinder, cylinder_faces = create_and_position_cylinder()

    # Pack solids together and plot 3d view
    solids = [cube, parallelepiped, pyramid, stub, cylinder]
    # print(solids)
    faces = [cube_faces, parallelepiped_faces, pyramid_faces, stub_faces, cylinder_faces]
    objects = zip(solids, faces)

    graph = ObjectGrapher()
    graph.set_axes_sizes(-10, 10)
    graph.set_config(line_width=0.2, edge_color='black', face_color='blue', alpha=0.1)
    graph.plot_objects(objects)

    # Convert to camera coordinates and plot 3d view again
    solids_in_vision, faces_in_vision = VolumeFilter(solids, faces).filter_solids()

    eye = np.array([-10, -3, -3])
    at = CenterGetter(solids_in_vision).get_center()

    camera_base = CameraBase(eye, at).get_camera_base()
    solids = ConvertBase.convert_objects(solids, camera_base, eye)
    objects = zip(solids, faces)

    graph = ObjectGrapher()
    graph.set_axes_sizes(-10, 10)
    graph.set_config(line_width=0.2, edge_color='black', face_color='red', alpha=0.1)
    graph.plot_objects(objects)

    # Project to 2d view
    solids_in_vision = ConvertBase.convert_objects(solids_in_vision, camera_base, eye)
    projection = Projection2d(solids_in_vision).project_solids(1, 10)
    objects = zip(projection, faces_in_vision)

    graph2d = Graph2D()
    graph2d.plot_objects(objects)
    graph2d.render_plot()


if __name__ == '__main__':
    main()
