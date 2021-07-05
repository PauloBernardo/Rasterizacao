import numpy as np
from matplotlib import pyplot as plt
from utils import get_rectangle_faces, get_triangle_faces, make_rectangle, plot_image, make_triangle, iterable_to_list, \
    get_edges


def q4(cube, pyramid):
    matriz_projecao = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]

    fig = plt.figure()
    ax = fig.add_subplot(111)

    cube_faces = get_rectangle_faces(np.dot(cube, matriz_projecao))
    arestas = get_edges(cube_faces)
    arestas = iterable_to_list(arestas)

    for aresta in arestas:
        aresta = np.array(aresta)
        ax.plot(aresta[:, 0], aresta[:, 1], color='blue')

    cube_faces = get_triangle_faces(np.dot(pyramid, matriz_projecao))
    arestas = get_edges(cube_faces)
    arestas = iterable_to_list(arestas)

    for aresta in arestas:
        aresta = np.array(aresta)
        ax.plot(aresta[:, 0], aresta[:, 1], color='red')

    plt.show()
