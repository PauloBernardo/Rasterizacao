import numpy as np

from q2 import q2
from q1 import q1
from q3 import q3
from q4 import q4
from utils import make_gif

if __name__ == "__main__":
    cube_points = np.array(
        [
            [-0.75, -0.75, 0],
            [0.75, -0.75, 0],
            [0.75, 0.75, 0],
            [-0.75, 0.75, 0],
            [-0.75, -0.75, 1.5],
            [0.75, -0.75, 1.5],
            [0.75, 0.75, 1.5],
            [-0.75, 0.75, 1.5],
        ]
    )

    parallel_points = np.array(
        [
            [0, 0, 0],
            [1.5, 0, 0],
            [1.5, 5, 0],
            [0, 5, 0],
            [0, 0, 2.5],
            [1.5, 0, 2.5],
            [1.5, 5, 2.5],
            [0, 5, 2.5],
        ]
    )

    pyramid_points = np.array([[0, -1, 0], [-1, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 3]])

    tronco_points = np.array(
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

    # # PRIMEIRA QUESTÃO
    q1(cube_points, parallel_points, pyramid_points, tronco_points)

    # SEGUNDA QUESTÃO
    cube_points, parallel_points, pyramid_points, tronco_points = q2(cube_points, parallel_points, pyramid_points, tronco_points)

    eyes = [np.array([i,-3,3]) for i in np.arange(-2,8,.5)]
    for eye in eyes:
        # TERCEIRA QUESTÃO
        cube_points, pyramid_points = q3(cube_points, pyramid_points, parallel_points, tronco_points,i)

        # QUARTA QUESTÃO
        q4(cube_points, pyramid_points)

    make_gif()