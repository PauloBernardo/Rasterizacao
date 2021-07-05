import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
from q2 import q2
from q1 import q1

if __name__ == "__main__":
    cube_points = np.array([[-0.75, -0.75, 0],
                            [0.75, -0.75, 0],
                            [0.75, 0.75, 0],
                            [-0.75, 0.75, 0],
                            [-0.75, -0.75, 1.5],
                            [0.75, -0.75, 1.5],
                            [0.75, 0.75, 1.5],
                            [-0.75, 0.75, 1.5]])


    parallel_points = np.array([[0, 0, 0],
                                [1.5, 0, 0],
                                [1.5, 5, 0],
                                [0, 5, 0],
                                [0, 0, 2.5],
                                [1.5, 0, 2.5],
                                [1.5, 5, 2.5],
                                [0, 5, 2.5]])


    pyramid_points = np.array([[0, -1, 0],
                               [-1, 0, 0],
                               [1, 0, 0],
                               [0, 1, 0],
                               [0, 0, 3]])

    tronco_points = np.array([[-1.5, -1.5, 0],
                           [1.5, -1.5, 0],
                           [1.5, 1.5, 0],
                           [-1.5, 1.5, 0],
                           [-0.65, -0.65, 2.5],
                           [0.65, -0.65, 2.5],
                           [0.65, 0.65, 2.5],
                           [-0.65, 0.65, 2.5]])



    # SEGUNDA QUESTÃO
    q1(cube_points, parallel_points, pyramid_points, tronco_points)
    # SEGUNDA QUESTÃO
    q2(cube_points, parallel_points, pyramid_points, tronco_points)
