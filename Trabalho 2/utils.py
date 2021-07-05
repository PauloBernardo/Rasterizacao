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


def make_rectangle(points):
    P = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    Z = np.zeros((8, 3))
    for i in range(8):
        Z[i, :] = np.dot(points[i, :], P)
    Z = 1 * Z

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # plot vertices
    ax.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2])

    # list of sides" polygons of figure
    verts = get_rectangle_faces(Z)

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
    P = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    Z = np.zeros((5, 3))
    for i in range(5):
        Z[i, :] = np.dot(points[i, :], P)
    Z = 1 * Z

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # plot vertices
    ax.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2])

    # list of sides" polygons of figure
    verts = get_triangle_faces(Z)

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
