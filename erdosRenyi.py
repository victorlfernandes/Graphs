from random import random

def erdos_renyi(grade, probability):

    matrix = []
    for i in range(grade):
        matrix.append([0] * grade)

    for i in range(grade):
        for j in range(i):
            if i == j:
                matrix[i][j] = 0
            else:
                aux = random()
                if aux > probability:
                    matrix[i][j] = 1
                    matrix[j][i] = 1
                else:
                    matrix[i][j] = 0
                    matrix[j][i] = 0

    return matrix

grade = int(input('Grade: '))
probability = float(input('Probability: '))

matrix = erdos_renyi(grade, probability)

for i in range(grade):
    for j in range(grade):
        print(matrix[i][j], end = '')
    print()    
            