# QUESTÃO 1 - CUBO
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from utils import make_rectangle, plot_image, make_triangle


def q1(cube_points, parallel_points, pyramid_points, tronco_points):
    def cubo():
        lado = 1.5

        ax, verts = make_rectangle(cube_points)
        plot_image(ax, verts)

    # QUESTÃO 1 - PARALELEPÍPEDO
    def paralelepipedo():
        ladoX = 1.5
        ladoY = 5
        ladoZ = 2.5

        ax, verts = make_rectangle(parallel_points)
        plot_image(ax, verts, "green", "b")

    # QUESTÃO 1 - PIRÂMIDE BASE QUADRADA
    def piramide():
        lado = 2
        altura = 3

        ax, verts = make_triangle(pyramid_points)
        plot_image(ax, verts, "red", "w")

    # QUESTÃO 1 - TRONCO DE PIRÂMIDE BASE QUADRADA
    def tronco():
        ladoMaior = 3
        ladoMenor = 1.3

        ax, verts = make_rectangle(tronco_points)
        plot_image(ax, verts, "yellow", "b")

    # QUESTÃO 1 - EXTRA -> MESCLANDO OBJETOS - TRONCO COM PIRÂMIDE
    def extra():
        points = np.array(
            [
                [-1.5, -1.5, 0],
                [1.5, -1.5, 0],
                [1.5, 1.5, 0],
                [-1.5, 1.5, 0],
                [-0.65, -0.65, 2.5],
                [0.65, -0.65, 2.5],
                [0.65, 0.65, 2.5],
                [-0.65, 0.65, 2.5],
            ]
        )

        points2 = np.array(
            [
                [-0.65, -0.65, 2.5],
                [0.65, -0.65, 2.5],
                [-0.65, 0.65, 2.5],
                [0.65, 0.65, 2.5],
                [0, 0, 4],
            ]
        )

        ax2, verts2 = make_triangle(points2)
        ax, verts = make_rectangle(points)

        points = np.array(
            [
                [-1.5, -1.5, 0],
                [1.5, -1.5, 0],
                [1.5, 1.5, 0],
                [-1.5, 1.5, 0],
                [-0.65, -0.65, 2.5],
                [0.65, -0.65, 2.5],
                [0.65, 0.65, 2.5],
                [-0.65, 0.65, 2.5],
                [0, 0, 4],
            ]
        )

        ax.scatter3D(points[:, 0], points[:, 1], points[:, 2])

        ax.add_collection3d(
            Poly3DCollection(
                verts, facecolors="yellow", linewidths=1, edgecolors="b", alpha=0.25
            )
        )
        ax.add_collection3d(
            Poly3DCollection(
                verts2, facecolors="red", linewidths=1, edgecolors="w", alpha=0.25
            )
        )
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        plt.show()

    cubo()
    piramide()
    paralelepipedo()
    tronco()
    # extra()
