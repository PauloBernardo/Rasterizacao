import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from utils import get_rectangle_faces, get_triangle_faces


def q2(cube, parallel, pyramid, tronco):
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

    points = np.array(all_points)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # plot vertices
    ax.scatter3D(points[:, 0], points[:, 1], points[:, 2])

    ax.add_collection3d(
        Poly3DCollection(
            get_rectangle_faces(cube),
            facecolors="cyan",
            linewidths=1,
            edgecolors="r",
            alpha=0.25,
        )
    )
    ax.add_collection3d(
        Poly3DCollection(
            get_triangle_faces(pyramid),
            facecolors="red",
            linewidths=1,
            edgecolors="r",
            alpha=0.25,
        )
    )

    # ax.add_collection3d(Poly3DCollection(get_rectangle_faces(parallel),
    #                                      facecolors="green", linewidths=1, edgecolors="r", alpha=.25))

    # ax.add_collection3d(Poly3DCollection(get_rectangle_faces(tronco),
    #                                      facecolors="yellow", linewidths=1, edgecolors="r", alpha=.25))

    # ax.add_collection3d(Poly3DCollection([
    #     [
    #         [0, 6, 6], [0, -6, 6], [0, -6, -6], [0, 6, -6]
    #     ],
    #     [
    #         [6, 0, 6], [-6, 0, 6], [-6, 0, -6], [6, 0, -6]
    #     ],
    #     [
    #         [6, 6, 0], [-6, 6, 0], [-6, -6, 0], [6, -6, 0]
    #     ]
    # ],
    #                                      facecolors="purple", linewidths=1, edgecolors="w", alpha=.25))

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.show()
