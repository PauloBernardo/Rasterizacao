import math
import matplotlib.pyplot as plt
import numpy as np


class Resolucoes:
    QQVGA = (160, 120)
    QVGA = (320, 240)
    VGA = (640, 480)
    XVGA = (1024, 768)


def render(matriz, resolucao, title="Reta"):
    plt.imshow(matriz, cmap='gray_r')
    plt.grid(True)
    plt.xlabel(resolucao[1])
    plt.ylabel(resolucao[0])
    plt.title(title)
    plt.show()


def produz_fragmento(x, y, valor_correcao=0.5):
    x_m = math.floor(x)
    y_m = math.floor(y)
    x_p = x_m + valor_correcao
    y_p = y_m + valor_correcao
    return x_p, y_p


def rasteriza_reta(ponto1, ponto2, resolucao, matriz=None):
    title = f"Desenho de uma reta ({ponto1[0]},{ponto1[1]}) ({ponto2[0]}, {ponto2[1]})"
    print(ponto1, ponto2)

    # Normaliza os valores
    ponto1 = (ponto1[0] * 0.01, ponto1[1] * 0.01)
    ponto2 = (ponto2[0] * 0.01, ponto2[1] * 0.01)

    # print(ponto1, ponto2)

    # Converte o SRU para o SRD
    ponto1 = (ponto1[0] * resolucao[0] / 1, (ponto1[1] * resolucao[1] / 1) - resolucao[1])
    ponto2 = (ponto2[0] * resolucao[0] / 1, (ponto2[1] * resolucao[1] / 1) - resolucao[1])

    # print(ponto1, ponto2)
    x = ponto1[0]
    y = ponto1[1]
    dx = ponto2[0] - ponto1[0]
    dy = ponto2[1] - ponto1[1]
    if dx == 0:
        m = 0
    else:
        m = dy / dx
    b = y - m * x
    pontos = []
    pontos.append(produz_fragmento(x, y))
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

    # print(pontos)

    if matriz is not None:
        for ponto in pontos:
            matriz[math.floor(ponto[0])][math.floor(ponto[1])] = 1
        return matriz
    else:
        matriz = np.zeros([resolucao[0] + 1, resolucao[1] + 1])
        for ponto in pontos:
            matriz[math.floor(ponto[0])][math.floor(ponto[1])] = 1
        render(matriz, resolucao, title)


def desenha_face(face, resolucao, matriz):
    vertice = face[0]
    for i in range(1, len(face)):
        matriz = rasteriza_reta(vertice, face[i], resolucao, matriz)
        vertice = face[i]
    matriz = rasteriza_reta(vertice, face[0], resolucao, matriz)
    return matriz


def desenha_quadrado(size, resolucao):
    matriz = np.zeros([resolucao[0] + 1, resolucao[1] + 1])
    vertices = [
        (1, 1),
        (1, size),
        (size, 1),
        (size, size),
    ]
    faces = [
        [vertices[0], vertices[1], vertices[3], vertices[2]],
    ]
    for face in faces:
        matriz = desenha_face(face, resolucao, matriz)

    render(matriz, resolucao, "Desenho de um quadrado")


def desenha_triangulo(size, resolucao):
    matriz = np.zeros([resolucao[0] + 1, resolucao[1] + 1])
    vertices = [
        (1, 1),
        (size, 1),
        (size / 2, size),
    ]
    faces = [
        [vertices[0], vertices[2], vertices[1]],
    ]
    for face in faces:
        matriz = desenha_face(face, resolucao, matriz)

    render(matriz, resolucao, "Desenho de um triângulo")


def desenha_pentagono(size, resolucao):
    matriz = np.zeros([resolucao[0] + 1, resolucao[1] + 1])
    vertices = [
        (size / 2, 1),
        (1, size / 1.5),
        (size / 2, size * 1.3),
        (size, size / 2),
        (size, size),
        (size / 2, size / 1.5)
    ]
    faces = [
        [vertices[0], vertices[1],  vertices[2],  vertices[4], vertices[3]],
        [vertices[5], vertices[0], vertices[1]],
        [vertices[5], vertices[1], vertices[2]],
        [vertices[5], vertices[2], vertices[4]],
        [vertices[5], vertices[4], vertices[3]],
    ]
    for face in faces:
        matriz = desenha_face(face, resolucao, matriz)

    render(matriz, resolucao, "Desenho de um Pentágono")


def desenha_casa(size, resolucao, rotate=0):
    matriz = np.zeros([resolucao[0] + 1, resolucao[1] + 1])
    vertices = [
        (1, 1),
        (1, size),
        (size, 1),
        (size, size),
        (size / 2, size + size),
        (size / 3, 1),
        (size / 3, size / 2),
        (size / 2, 1),
        (size / 2, size / 2),
        (size + size / 3, size / 3),
        (size + size / 3, size / 1.5),
        (size + size / 1.5, size / 3),
        (size + size / 1.5, size / 1.5),
        (size + size, 1),
        (size + size, size),
        (size + size, size + size),
    ]
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
    rasteriza_reta((0, 0), (90, 30), Resolucoes.QQVGA)
    rasteriza_reta((0, 0), (30, 90), Resolucoes.QQVGA)
    rasteriza_reta((30, 80), (90, 20), Resolucoes.QQVGA)
    rasteriza_reta((0, 0), (90, 30), Resolucoes.QVGA)
    rasteriza_reta((0, 0), (30, 90), Resolucoes.QVGA)
    rasteriza_reta((30, 80), (90, 20), Resolucoes.QVGA)
    rasteriza_reta((0, 0), (90, 30), Resolucoes.VGA)
    rasteriza_reta((0, 0), (30, 90), Resolucoes.VGA)
    rasteriza_reta((30, 80), (90, 20), Resolucoes.VGA)

    # rasteriza_reta((1, 8), (8, 8), Resolucoes.QVGA)
    # rasteriza_reta((8, 1), (8, 8), Resolucoes.QVGA)
    #
    # desenha_quadrado(40, Resolucoes.QQVGA)
    # desenha_triangulo(40, Resolucoes.QQVGA)
    # desenha_pentagono(40, Resolucoes.QQVGA)
    # desenha_casa(30, Resolucoes.QQVGA)
