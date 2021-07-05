import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt


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

    plt.show()
