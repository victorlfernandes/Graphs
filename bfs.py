from sys import stdin

def bfs(grafo, v, matriz):
    fila = []
    print(v - 1)
    grafo.cor[v - 1] = 'cinza'
    matriz[v - 1][v - 1] = 0
    fila.append(v)
    while fila:
        atual = fila.pop(0)
        aux = grafo.listaDeAdjacencia[atual - 1]
        for i in aux:
            vAdjacente = aux[i]
            if grafo.cor[vAdjacente] == 'branco':
                matriz[v - 1][vAdjacente] = matriz[v - 1][atual - 1] + 1
                grafo.cor[vAdjacente] = 'cinza'
                fila.append(vAdjacente + 1)
        grafo.cor[atual - 1] = 'preto'
    for i in range(grafo.qtdVertices):
        grafo.cor[i - 1] = 'branco'

def matrizDistancia(grafo):
    matriz = []
    for i in range(grafo.qtdVertices):
        matriz.append(grafo.qtdVertices * [0])
    for i in range(grafo.qtdVertices):
        bfs(grafo, i + 1, matriz)
    for i in range(grafo.qtdVertices):
        for j in range(grafo.qtdVertices):
            print(matriz[i][j], end='')
        print()

class Grafo:

    def __init__(self, qtdVertices):
        self.qtdVertices = qtdVertices
        self.listaDeAdjacencia = []
        for i in range(self.qtdVertices):
            self.listaDeAdjacencia.append(self.qtdVertices * [0])
        self.cor = qtdVertices * [0]

    def criarAresta(self, v1, v2):
        self.listaDeAdjacencia[v1 - 1].append(v2)
        self.listaDeAdjacencia[v2 - 1].append(v1)

s = stdin.read()
tamEntrada = len(s)
qtdVertices = int(s[10])
g = Grafo(qtdVertices)
i = 21
while i < tamEntrada:
    v1 = int(s[i])
    i += 2
    v2 = int(s[i])
    i += 3
    g.criarAresta(v1, v2)
matrizDistancia(g)