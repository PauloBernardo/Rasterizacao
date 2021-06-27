import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt


def get_rectangle_faces(Z):
    return [[Z[0], Z[1], Z[2], Z[3]],
            [Z[4], Z[5], Z[6], Z[7]],
            [Z[0], Z[1], Z[5], Z[4]],
            [Z[2], Z[3], Z[7], Z[6]],
            [Z[1], Z[2], Z[6], Z[5]],
            [Z[4], Z[7], Z[3], Z[0]],
            [Z[2], Z[3], Z[7], Z[6]]]


def make_rectangle(points):
    P = [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]]

    Z = np.zeros((8, 3))
    for i in range(8): Z[i, :] = np.dot(points[i, :], P)
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
        [Z[2], Z[0], Z[4]]
    ]


def make_triangle(points):
    P = [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]]

    Z = np.zeros((5, 3))
    for i in range(5): Z[i, :] = np.dot(points[i, :], P)
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
    ax.add_collection3d(Poly3DCollection(verts,
                                         facecolors=side_color, linewidths=1, edgecolors=line_color, alpha=.25))

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.show()


def question_2(cube, parallel, pyramid, tronco):
    print("whatfoca velho")
    # convert nympy array to dictionary

    # Translação do cubo
    cube = np.array([[x[0] + 1, x[1] + 1, x[2] + 1] for x in cube])
    # Translação do paralelepipedo
    parallel = np.array([[x[0] + 1, x[1] - 6, x[2] + 1] for x in parallel])
    # Translação da piramide
    pyramid = np.array([[x[0] - 3, x[1] - 3, x[2] - 4] for x in pyramid])
    # Translação do tronco
    tronco = np.array([[x[0] - 3, x[1] + 3, x[2] - 4] for x in tronco])

    all_points = []
    all_points.extend(cube.tolist())
    all_points.extend(parallel.tolist())
    all_points.extend(pyramid.tolist())
    all_points.extend(tronco.tolist())

    # print(all_points)

    points = np.array(all_points)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # plot vertices
    # print(points)
    ax.scatter3D(points[:, 0], points[:, 1], points[:, 2])

    ax.add_collection3d(Poly3DCollection(get_rectangle_faces(cube),
                                         facecolors="cyan", linewidths=1, edgecolors="r", alpha=.25))

    ax.add_collection3d(Poly3DCollection(get_rectangle_faces(parallel),
                                         facecolors="green", linewidths=1, edgecolors="r", alpha=.25))

    ax.add_collection3d(Poly3DCollection(get_triangle_faces(pyramid),
                                         facecolors="red", linewidths=1, edgecolors="r", alpha=.25))

    ax.add_collection3d(Poly3DCollection(get_rectangle_faces(tronco),
                                         facecolors="yellow", linewidths=1, edgecolors="r", alpha=.25))

    ax.add_collection3d(Poly3DCollection([
        [
            [0, 6, 6], [0, -6, 6], [0, -6, -6], [0, 6, -6]
        ],
        [
            [6, 0, 6], [-6, 0, 6], [-6, 0, -6], [6, 0, -6]
        ],
        [
            [6, 6, 0], [-6, 6, 0], [-6, -6, 0], [6, -6, 0]
        ]
    ],
                                         facecolors="purple", linewidths=1, edgecolors="w", alpha=.25))

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.show()


if __name__ == "__main__":
    # QUESTÃO 1 - CUBO

    lado = 1.5

    cube_points = np.array([[-0.75, -0.75, 0],
                            [0.75, -0.75, 0],
                            [0.75, 0.75, 0],
                            [-0.75, 0.75, 0],
                            [-0.75, -0.75, 1.5],
                            [0.75, -0.75, 1.5],
                            [0.75, 0.75, 1.5],
                            [-0.75, 0.75, 1.5]])

    ax, verts = make_rectangle(cube_points)
    plot_image(ax, verts)

    # QUESTÃO 1 - PARALELEPÍPEDO

    ladoX = 1.5
    ladoY = 5
    ladoZ = 2.5

    parallel_points = np.array([[0, 0, 0],
                                [1.5, 0, 0],
                                [1.5, 5, 0],
                                [0, 5, 0],
                                [0, 0, 2.5],
                                [1.5, 0, 2.5],
                                [1.5, 5, 2.5],
                                [0, 5, 2.5]])

    ax, verts = make_rectangle(parallel_points)
    plot_image(ax, verts, "green", "b")

    # QUESTÃO 1 - PIRÂMIDE BASE QUADRADA

    lado = 2
    altura = 3

    pyramid_points = np.array([[0, -1, 0],
                               [-1, 0, 0],
                               [1, 0, 0],
                               [0, 1, 0],
                               [0, 0, 3]])

    ax, verts = make_triangle(pyramid_points)
    plot_image(ax, verts, "red", "w")

    # QUESTÃO 1 - TRONCO DE PIRÂMIDE BASE QUADRADA

    ladoMaior = 3
    ladoMenor = 1.3

    tronco_points = np.array([[-1.5, -1.5, 0],
                              [1.5, -1.5, 0],
                              [1.5, 1.5, 0],
                              [-1.5, 1.5, 0],
                              [-0.65, -0.65, 2.5],
                              [0.65, -0.65, 2.5],
                              [0.65, 0.65, 2.5],
                              [-0.65, 0.65, 2.5]])

    ax, verts = make_rectangle(tronco_points)
    plot_image(ax, verts, "yellow", "b")

    # QUESTÃO 1 - EXTRA -> MESCLANDO OBJETOS - TRONCO COM PIRÂMIDE
    points = np.array([[-1.5, -1.5, 0],
                       [1.5, -1.5, 0],
                       [1.5, 1.5, 0],
                       [-1.5, 1.5, 0],
                       [-0.65, -0.65, 2.5],
                       [0.65, -0.65, 2.5],
                       [0.65, 0.65, 2.5],
                       [-0.65, 0.65, 2.5]])

    points2 = np.array([[-0.65, -0.65, 2.5],
                        [0.65, -0.65, 2.5],
                        [-0.65, 0.65, 2.5],
                        [0.65, 0.65, 2.5],
                       [0, 0, 4]])

    ax2, verts2 = make_triangle(points2)
    ax, verts = make_rectangle(points)

    points = np.array([[-1.5, -1.5, 0],
                       [1.5, -1.5, 0],
                       [1.5, 1.5, 0],
                       [-1.5, 1.5, 0],
                       [-0.65, -0.65, 2.5],
                       [0.65, -0.65, 2.5],
                       [0.65, 0.65, 2.5],
                       [-0.65, 0.65, 2.5],
                       [0, 0, 4]])
    ax.scatter3D(points[:, 0], points[:, 1], points[:, 2])

    ax.add_collection3d(Poly3DCollection(verts,
                                         facecolors="yellow", linewidths=1, edgecolors="b", alpha=.25))
    ax.add_collection3d(Poly3DCollection(verts2,
                                         facecolors="red", linewidths=1, edgecolors="w", alpha=.25))

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.show()

    # SEGUNDA QUESTÃO
    question_2(cube_points, parallel_points, pyramid_points, tronco_points)
