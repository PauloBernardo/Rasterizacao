import os
from collections.abc import Iterable

import imageio as imageio
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt

from trab_2 import ROOT_DIR


def get_rectangle_faces(Z):
    return [
        [Z[0], Z[1], Z[2], Z[3]],
        [Z[4], Z[5], Z[6], Z[7]],
        [Z[0], Z[1], Z[5], Z[4]],
        [Z[2], Z[3], Z[7], Z[6]],
        [Z[1], Z[2], Z[6], Z[5]],
        [Z[4], Z[7], Z[3], Z[0]],
        [Z[2], Z[3], Z[7], Z[6]],
    ]


def make_translation(points, x=0, y=0, z=0):
    m = np.matrix(
        [
            [1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]
        ]
    )
    p = np.ones((len(points) + 1, 4))
    for i in range(len(points)):
        p[i][0] = points[i][0]
        p[i][1] = points[i][1]
        p[i][2] = points[i][2]

    p = (m * p.transpose()).transpose()[0:8]
    return np.array([[point[0], point[1], point[2]] for point in p.A])


def make_scale(points, x=1, y=1, z=1):
    m = [[x, 0, 0], [0, z, 0], [0, 0, y]]

    p = np.zeros((8, 3))
    for i in range(8):
        p[i, :] = np.dot(points[i, :], m)

    return p


def make_rectangle(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # plot vertices
    ax.scatter3D(points[:, 0], points[:, 1], points[:, 2])

    # list of sides" polygons of figure
    verts = get_rectangle_faces(points)

    return ax, verts


def get_triangle_faces(Z):
    return [
        [Z[0], Z[1], Z[3], Z[2]],
        [Z[0], Z[1], Z[4]],
        [Z[1], Z[3], Z[4]],
        [Z[2], Z[3], Z[4]],
        [Z[2], Z[0], Z[4]],
    ]


def make_triangle(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # plot vertices
    ax.scatter3D(points[:, 0], points[:, 1], points[:, 2])

    # list of sides" polygons of figure
    verts = get_triangle_faces(points)

    return ax, verts


def plot_image(ax, verts, side_color="cyan", line_color="r"):
    # plot sides
    ax.add_collection3d(
        Poly3DCollection(
            verts,
            facecolors=side_color,
            linewidths=1,
            edgecolors=line_color,
            alpha=0.25,
        )
    )

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.auto_scale_xyz([-2, 5], [-2, 5], [-2, 5])

    plt.show()


def get_face_edges(face):
    faces = set()
    qnt_points = len(face)
    for i in range(qnt_points):
        faces.add(((face[i][0], face[i][1]), (face[(i + 1) % qnt_points][0], face[(i + 1) % qnt_points][1])))
    return faces


def get_edges(cube):
    edges = set()
    for i in cube:
        edges = edges.union(get_face_edges(i))
    return edges


def iterable_to_list(data):
    if isinstance(data, Iterable):
        data = list(data)
        for i, item in enumerate(data):
            print(item)
            data[i] = iterable_to_list(item)
    else:
        return data
    return data


def make_gif(dir='gif_images'):
    with imageio.get_writer(ROOT_DIR / 'movie.gif', mode='I', duration=0.1) as writer:
        for filename in sorted(os.listdir(ROOT_DIR / dir)):
            print(filename)
            if filename.endswith(".png"):
                image = imageio.imread(str((ROOT_DIR / dir / filename)))
                writer.append_data(image)
    for image in os.listdir(ROOT_DIR/dir):
        if image.endswith(".png"):
            os.remove(ROOT_DIR/dir/image)


if __name__ == '__main__':
    make_gif()
