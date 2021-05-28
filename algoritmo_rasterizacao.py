import math
import matplotlib.pyplot as plt
import numpy as np

LIMITE_MINIMO_SRU = (-80, -50)
LIMITE_MAXIMO_SRU = (80, 50)


class Resolucoes:
    QQVGA = (160, 120)
    QVGA = (320, 240)
    VGA = (640, 480)
    XVGA = (1024, 768)


def render(matriz, resolucao, title="Reta"):
    """
    Renderiza a matriz com pyplot.imshow
    :param matriz: um matriz bidimensional, do tipo ndarray
    :param resolucao: uma tupla que possui os valores da resolução (x, y)
    :param title: string que será mostrada como titulo da imagem
    :return: void
    """
    plt.imshow(matriz, cmap='gray_r')
    plt.xticks(rotation=-90)
    plt.grid(True)
    plt.xlabel(resolucao[1])
    plt.ylabel(resolucao[0])
    plt.title(title)
    plt.show()


def produz_fragmento(x, y):
    x_m = math.floor(x)
    y_m = math.floor(y)
    x_p = x_m + 0.5
    y_p = y_m + 0.5
    return x_p, y_p


def rasteriza_reta(ponto1, ponto2, resolucao, matriz=None):
    """
    A função rasteriza_reta faz a rasterização de uma reta definida por dois pontos, ponto1
    e ponto2, que representam os pontos extremos da reta.
    Os limites dos pontos são LIMITE_MINIMO_SRU e LIMITE_MAXIMO_SRU.
    :param ponto1: tupla que guarda o valor x e y de um dos pontos extremos da reta
    :param ponto2: tupla que guarda o valor x e y de um dos pontos extremos da reta
    :param resolucao: resolução no qual a reta deve ser representada
    :param matriz: opcional, representa uma matriz do tipo ndarray
    :return: retorna uma matriz do tipo ndarray
    """
    title = f"Desenho de uma reta ({ponto1[0]},{ponto1[1]}) ({ponto2[0]}, {ponto2[1]})"

    # Converte o SRU para o SRD
    ponto1 = (ponto1[0] * resolucao[0] / (LIMITE_MAXIMO_SRU[0] - LIMITE_MINIMO_SRU[0]),
              (ponto1[1] * resolucao[1] / (LIMITE_MAXIMO_SRU[1] - LIMITE_MINIMO_SRU[1])) - resolucao[1])
    ponto2 = (ponto2[0] * resolucao[0] / (LIMITE_MAXIMO_SRU[0] - LIMITE_MINIMO_SRU[0]),
              (ponto2[1] * resolucao[1] / (LIMITE_MAXIMO_SRU[1] - LIMITE_MINIMO_SRU[1])) - resolucao[1])

    # Forma equação da reta
    x = ponto1[0]
    y = ponto1[1]
    dx = ponto2[0] - ponto1[0]
    dy = ponto2[1] - ponto1[1]
    if dx == 0:
        m = 0
    else:
        m = dy / dx
    b = y - m * x

    # Rasteriza
    pontos = [produz_fragmento(x, y)]
    if math.fabs(dx) > math.fabs(dy):
        if x < ponto2[0]:
            while x < ponto2[0]:
                x += 1
                y = m * x + b
                pontos.append(produz_fragmento(x, y))
        else:
            while x > ponto2[0]:
                x -= 1
                y = m * x + b
                pontos.append(produz_fragmento(x, y))
    else:
        if y < ponto2[1]:
            while y < ponto2[1]:
                y += 1
                x = (y - b) / m if m else x
                pontos.append(produz_fragmento(x, y))
        else:
            while y > ponto2[1]:
                y -= 1
                x = (y - b) / m if m else x
                pontos.append(produz_fragmento(x, y))

    # Forma matriz e renderiza
    if matriz is not None:
        for ponto in pontos:
            matriz[math.floor(ponto[0])][math.floor(ponto[1])] = 1
        return matriz
    else:
        matriz = np.zeros([resolucao[0] + 1, resolucao[1] + 1])
        for ponto in pontos:
            matriz[math.floor(ponto[0])][math.floor(ponto[1])] = 1
        render(matriz, resolucao, title)
        return matriz


def desenha_face(face, resolucao, matriz):
    vertice = face[0]
    for i in range(1, len(face)):
        matriz = rasteriza_reta(vertice, face[i], resolucao, matriz)
        vertice = face[i]
    matriz = rasteriza_reta(vertice, face[0], resolucao, matriz)
    return matriz


def apply_transformation(vertices, scale, rX, rY, aX, aY):
    vertices = vertices * np.matrix([[scale, 0], [0, scale]])
    vertices = vertices * np.matrix([[rY, 0], [0, rX]])
    vertices = vertices * np.matrix([[1, aY], [aX, 1]])
    return vertices


def desenha_quadrado(size, resolucao, rX=1, rY=1, aX=0, aY=0):
    """
    Desenha um quadrado com um tamanho definido em size
    :param size: valor do tamanho do quadrado
    :param resolucao: resolução na qual deve ser desenhado
    :return: void
    """
    matriz = np.zeros([resolucao[0] + 1, resolucao[1] + 1])
    vertices = np.matrix([
        [1, 1],
        [1, 10],
        [10, 1],
        [10, 10],
    ])
    vertices = apply_transformation(vertices, size, rX, rY, aX, aY)
    vertices = vertices.A
    faces = [
        [vertices[0], vertices[1], vertices[3], vertices[2]],
    ]
    for face in faces:
        matriz = desenha_face(face, resolucao, matriz)

    render(matriz, resolucao, "Desenho de um quadrado")


def desenha_triangulo(size, resolucao, rX=1, rY=1, aX=0, aY=0):
    """
    Desenha um triangulo com um tamanho definido em size
    :param size: valor do tamanho do triangulo
    :param resolucao: resolução na qual deve ser desenhado
    :return: void
    """
    matriz = np.zeros([resolucao[0] + 1, resolucao[1] + 1])
    vertices = np.matrix([
        [1, 1],
        [10, 1],
        [10 / 2, 10],
    ])
    vertices = apply_transformation(vertices, size, rX, rY, aX, aY)
    vertices = vertices.A
    faces = [
        [vertices[0], vertices[2], vertices[1]],
    ]
    for face in faces:
        matriz = desenha_face(face, resolucao, matriz)

    render(matriz, resolucao, "Desenho de um triângulo")


def desenha_pentagono(size, resolucao, rX=1, rY=1, aX=0, aY=0):
    """
    Desenha um pentagono com o tamanho definido em size
    :param size: valor do tamanho do pentagono
    :param resolucao: resolução na qual deve ser desenhado
    :return: void
    """
    matriz = np.zeros([resolucao[0] + 1, resolucao[1] + 1])
    vertices = np.matrix([
        [10 / 2, 1],
        [1, 10 / 1.5],
        [10 / 2, 10 * 1.3],
        [10, 10 / 2],
        [10, 10],
        [10 / 2, 10 / 1.5]
    ])
    vertices = apply_transformation(vertices, size, rX, rY, aX, aY)
    vertices = vertices.A
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[4], vertices[3]],
        [vertices[5], vertices[0], vertices[1]],
        [vertices[5], vertices[1], vertices[2]],
        [vertices[5], vertices[2], vertices[4]],
        [vertices[5], vertices[4], vertices[3]],
    ]
    for face in faces:
        matriz = desenha_face(face, resolucao, matriz)

    render(matriz, resolucao, "Desenho de um Pentágono")


def desenha_casa(size, resolucao, rX=1, rY=1.0, aX=0.0, aY=0.0):
    """
    Desenha um casa com um tamanho definido em size
    :param size: valor do tamanho da casa
    :param resolucao: resolução na qual deve ser desenhada
    :return: void
    """
    matriz = np.zeros([resolucao[0] + 1, resolucao[1] + 1])
    vertices = np.matrix([
        [1, 1],
        [1, 10],
        [10, 1],
        [10, 10],
        [10 / 2, 10 + 10],
        [10 / 3, 1],
        [10 / 3, 10 / 2],
        [10 / 2, 1],
        [10 / 2, 10 / 2],
        [10 + 10 / 3, 10 / 3],
        [10 + 10 / 3, 10 / 1.5],
        [10 + 10 / 1.5, 10 / 3],
        [10 + 10 / 1.5, 10 / 1.5],
        [10 + 10, 1],
        [10 + 10, 10],
        [10 + 10, 10 + 10],
    ])
    vertices = apply_transformation(vertices, size, rX, rY, aX, aY)
    vertices = vertices.A
    faces = [
        [vertices[0], vertices[1], vertices[3], vertices[2]],
        [vertices[1], vertices[4], vertices[3]],
        [vertices[5], vertices[6], vertices[8], vertices[7]],
        [vertices[9], vertices[10], vertices[12], vertices[11]],
        [vertices[2], vertices[3], vertices[14], vertices[13]],
        [vertices[3], vertices[4], vertices[15], vertices[14]],
    ]
    for face in faces:
        matriz = desenha_face(face, resolucao, matriz)

    render(matriz, resolucao, "Desenho de uma casa")


if __name__ == "__main__":
    # Rasterização de retas nas diferentes resoluções
    # rasteriza_reta((0, 0), (90, 30), Resolucoes.QQVGA)
    # rasteriza_reta((0, 0), (30, 90), Resolucoes.QQVGA)
    # rasteriza_reta((30, 80), (90, 20), Resolucoes.QQVGA)
    # rasteriza_reta((0, 0), (90, 30), Resolucoes.QVGA)
    # rasteriza_reta((0, 0), (30, 90), Resolucoes.QVGA)
    # rasteriza_reta((30, 80), (90, 20), Resolucoes.QVGA)
    # rasteriza_reta((0, 0), (90, 30), Resolucoes.VGA)
    # rasteriza_reta((0, 0), (30, 90), Resolucoes.VGA)
    # rasteriza_reta((30, 80), (90, 20), Resolucoes.VGA)

    # Rasterização de retas verticais e horizontais
    # rasteriza_reta((1, 80), (80, 80), Resolucoes.QQVGA)
    # rasteriza_reta((80, 1), (80, 80), Resolucoes.QQVGA)

    # Rasterização de poligonos
    # desenha_quadrado(3, Resolucoes.QQVGA, 1, 1, 0.25, 0)
    # desenha_triangulo(4, Resolucoes.QQVGA, 2, 2, 0.3, 0)
    # desenha_pentagono(5, Resolucoes.QQVGA, 1, 1, -0.2, -0.2)
    desenha_casa(3.8, Resolucoes.QQVGA, 1, 1, 0.2, 0.3)
