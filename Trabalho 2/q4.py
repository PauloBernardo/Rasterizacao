import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from utils import get_rectangle_faces, get_triangle_faces


def q4(cube, pyramid):
    # X,Y,Z
    ponto_camera = [5,5,-5]

    print(cube,pyramid)