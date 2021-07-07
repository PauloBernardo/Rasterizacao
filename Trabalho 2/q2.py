import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from utils import get_rectangle_faces, get_triangle_faces, make_scale, make_translation


def q2(cube, parallel, pyramid, tronco):
    # Escalas
    tronco = make_scale(tronco, 0.5, 0.5, 0.5)

    # Translaçẽs
    cube = make_translation(cube, 1, 1, 1)
    parallel = make_translation(parallel, -5, 1, 1)
    pyramid = make_translation(pyramid, 3, 3, 1)
    tronco = make_translation(tronco, -2, 3, 1)

    all_points = []
    all_points.extend(cube.tolist())
    all_points.extend(parallel.tolist())
    all_points.extend(pyramid.tolist())
    all_points.extend(tronco.tolist())
    all_points.extend([
        [0, 6, 6], [0, -6, 6], [0, -6, -6], [0, 6, -6],
        [6, 0, 6], [-6, 0, 6], [-6, 0, -6], [6, 0, -6],
        [6, 6, 0], [-6, 6, 0], [-6, -6, 0], [6, -6, 0]
    ])

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

    ax.add_collection3d(Poly3DCollection(get_rectangle_faces(parallel),
                                         facecolors="green", linewidths=1, edgecolors="r", alpha=.25))

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

    return cube, parallel, pyramid, tronco
