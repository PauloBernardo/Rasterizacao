import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from utils import get_rectangle_faces, get_triangle_faces


def draw_camera_and_vectors_in_world(ponto_camera, vetor_up, vetor_n, vetor_u, vetor_v, cube, pyramid, parallel,
                                     tronco):
    camera = np.array(
        [
            [ponto_camera[0] - 0.5, ponto_camera[1] - 0.5, ponto_camera[2] - 0.5],
            [ponto_camera[0] + 0.5, ponto_camera[1] - 0.5, ponto_camera[2] - 0.5],
            [ponto_camera[0] + 0.5, ponto_camera[1] + 0.5, ponto_camera[2] - 0.5],
            [ponto_camera[0] - 0.5, ponto_camera[1] + 0.5, ponto_camera[2] - 0.5],
            [ponto_camera[0] - 0.5, ponto_camera[1] - 0.5, ponto_camera[2] + 0.5],
            [ponto_camera[0] + 0.5, ponto_camera[1] - 0.5, ponto_camera[2] + 0.5],
            [ponto_camera[0] + 0.5, ponto_camera[1] + 0.5, ponto_camera[2] + 0.5],
            [ponto_camera[0] - 0.5, ponto_camera[1] + 0.5, ponto_camera[2] + 0.5],
        ]
    )

    all_points = []
    all_points.extend(cube.tolist())
    all_points.extend(parallel.tolist())
    all_points.extend(pyramid.tolist())
    all_points.extend(tronco.tolist())
    all_points.extend(camera.tolist())
    all_points.extend([
        [0, 6, 6], [0, -6, 6], [0, -6, -6], [0, 6, -6],
        [6, 0, 6], [-6, 0, 6], [-6, 0, -6], [6, 0, -6],
        [6, 6, 0], [-6, 6, 0], [-6, -6, 0], [6, -6, 0]
    ])

    points = np.array(all_points)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.text(*[ponto_camera[0] + 1, ponto_camera[1] - 2, ponto_camera[2] - 1], "Câmera", c="Black")

    # plot vertices
    ax.scatter3D(points[:, 0], points[:, 1], points[:, 2])

    ax.add_collection3d(
        Poly3DCollection(
            get_rectangle_faces(camera),
            facecolors="blue",
            linewidths=1,
            edgecolors="b",
            alpha=0.25,
        )
    )

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

    soa = np.array([
        [ponto_camera[0], ponto_camera[1], ponto_camera[2], vetor_up[0] * 3, vetor_up[1] * 3, vetor_up[2] * 3],
        [ponto_camera[0], ponto_camera[1], ponto_camera[2], vetor_n[0] * -3, vetor_n[1] * -3, vetor_n[2] * -3],
        [ponto_camera[0], ponto_camera[1], ponto_camera[2], vetor_u[0] * 3, vetor_u[1] * 3, vetor_u[2] * 3],
        [ponto_camera[0], ponto_camera[1], ponto_camera[2], vetor_v[0] * 3, vetor_v[1] * 3, vetor_v[2] * 3]
    ])

    X, Y, Z, U, V, W = zip(*soa)
    ax.quiver(X, Y, Z, U, V, W)
    plt.show()


def q3(cube, pyramid, parallel, tronco, ponto_camera=np.array([3, -3, 3]), show=False):
    cube = np.array(cube)
    centro_cubo = [(max(cube[:, i]) + min(cube[:, i])) / 2 for i in range(3)]
    centro_piramide = [(max(pyramid[:, i]) + min(pyramid[:, i])) / 2 for i in range(3)]

    ponto_medio = np.add(centro_cubo, centro_piramide) / 2

    if show:
        print("Centro cubo", centro_cubo)
        print("Centro pirâmide", centro_piramide)
        print("Ponto médio", ponto_medio)

    vetor_n = np.subtract(ponto_camera, ponto_medio)

    vetor_up = [0, 0, 1]

    vetor_u = np.cross(vetor_up, vetor_n)
    vetor_v = np.cross(vetor_n, vetor_u)

    if show:
        print("Vetor n, u e v:", vetor_n, vetor_u, vetor_v)

    vetor_n = np.divide(vetor_n, np.linalg.norm(vetor_n))
    vetor_u = np.divide(vetor_u, np.linalg.norm(vetor_u))
    vetor_v = np.divide(vetor_v, np.linalg.norm(vetor_v))

    if show:
        print("Vetor n, u e v:", vetor_n, vetor_u, vetor_v)

    # base = [vetor_n, vetor_u, vetor_v]
    # inv = np.linalg.inv(base)

    V = np.matrix([
        [vetor_u[0], vetor_u[1], vetor_u[2],
         - ponto_camera[0] * vetor_u[0] - ponto_camera[1] * vetor_u[1] - ponto_camera[2] * vetor_u[2]],
        [vetor_v[0], vetor_v[1], vetor_v[2],
         - ponto_camera[0] * vetor_v[0] - ponto_camera[1] * vetor_v[1] - ponto_camera[2] * vetor_v[2]],
        [vetor_n[0], vetor_n[1], vetor_n[2],
         - ponto_camera[0] * vetor_n[0] - ponto_camera[1] * vetor_n[1] - ponto_camera[2] * vetor_n[2]],
        [0, 0, 0, 1]
    ])

    def transform_camera(object_points):
        p = np.ones((len(object_points) + 1, 4))
        for i in range(len(object_points)):
            p[i][0] = object_points[i][0]
            p[i][1] = object_points[i][1]
            p[i][2] = object_points[i][2]

        p = (V * p.transpose()).transpose()[0:8]
        return np.array([[point[0], point[1], point[2]] for point in p.A])

    if show:
        print("Transformação V", V)
    cubo_projetado = transform_camera(cube)
    piramide_projetada = transform_camera(pyramid)

    if show:
        draw_camera_and_vectors_in_world(ponto_camera, vetor_up, vetor_n, vetor_u, vetor_v, cube, pyramid, parallel,
                                         tronco)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        all_points = []
        all_points.extend(cubo_projetado.tolist())
        all_points.extend(piramide_projetada.tolist())
        points = np.array(all_points)

        # plot vertices
        ax.scatter3D(points[:, 0], points[:, 1], points[:, 2])

        ax.add_collection3d(
            Poly3DCollection(
                get_rectangle_faces(cubo_projetado),
                facecolors="cyan",
                linewidths=1,
                edgecolors="r",
                alpha=0.25,
            )
        )
        ax.add_collection3d(
            Poly3DCollection(
                get_triangle_faces(piramide_projetada),
                facecolors="red",
                linewidths=1,
                edgecolors="r",
                alpha=0.25,
            )
        )

        ax.add_collection3d(Poly3DCollection(get_rectangle_faces(cubo_projetado),
                                             facecolors="green", linewidths=1, edgecolors="r", alpha=.25))

        ax.add_collection3d(Poly3DCollection(get_rectangle_faces(cubo_projetado),
                                             facecolors="yellow", linewidths=1, edgecolors="r", alpha=.25))

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        plt.show()

    return cubo_projetado, piramide_projetada
