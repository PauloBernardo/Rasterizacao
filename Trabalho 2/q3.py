import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from utils import get_rectangle_faces, get_triangle_faces, make_rectangle, plot_image, make_triangle


def q3(cube, pyramid):
    # X,Y,Z
    ponto_camera = np.array([5, 5, -5])

    cube = np.array(cube)
    centro_cubo = [(max(cube[:, i]) + min(cube[:, i])) / 2 for i in range(3)]
    centro_piramide = [(max(pyramid[:, i]) + min(pyramid[:, i])) / 2 for i in range(3)]

    ponto_medio = np.add(centro_cubo, centro_piramide) / 2

    print(centro_cubo)
    print(centro_piramide)
    print(ponto_medio)

    vetor_n = np.subtract(ponto_camera, ponto_medio)

    aux = [10, 10, 10]

    vetor_u = np.cross(aux, vetor_n)
    vetor_v = np.cross(vetor_n, vetor_u)

    vetor_n = np.divide(vetor_n, np.linalg.norm(vetor_n))
    vetor_u = np.divide(vetor_u, np.linalg.norm(vetor_u))
    vetor_v = np.divide(vetor_v, np.linalg.norm(vetor_v))

    base = [vetor_n, vetor_u, vetor_v]
    inv = np.linalg.inv(base)

    cubo_projetado = np.dot(inv, cube.T).T
    piramide_projetada = np.dot(inv, pyramid.T).T

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
