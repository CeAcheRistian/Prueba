"""	
Estás atrapado en una pesadilla en la que Freddy Krueger te persigue. El sueño está representado por un laberinto de celdas, donde cada celda tiene un valor numérico que indica el nivel de peligro de esa parte del sueño.

Debes encontrar el camino más seguro (es decir, el que tenga el menor valor total de peligro) desde la esquina superior izquierda hasta la esquina inferior derecha de la matriz.

En este desafío, solo puedes moverte hacia la derecha o hacia abajo (no puedes retroceder ni moverte en diagonal) y debes calcular el nivel total de peligro del camino más seguro.

La pesadilla está representada por una matriz dream de tamaño n x m donde cada celda es un número positivo que representa el nivel de peligro de esa celda en el sueño.

Y tienes que devolver el valor total de peligro del camino más seguro de la esquina superior izquierda (posición [0][0]) a la esquina inferior derecha (posición [n-1][m-1]).

dream = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1],
]

const bestPath = findSafestPath(dream) // Devuelve 7
El mejor camino es:
[0, 0] -> 1
[0, 1] -> 3
[0, 2] -> 1
[1, 2] -> 1
[2, 2] -> 1

1 -> 3 -> 1 -> 1 -> 1 = 7

"""
def findSafestPath(dream):
    rows = len(dream[0]) 
    columns = len(dream)
    road = []
    road.append(dream[0][0])

    for row in range(1,rows):
        road.append(road[row - 1] + dream[0][row])


    for row in range(1, rows):
        road[0] = road[0] + dream[row][0]

        for column in range(1, columns):
            road[column] = min(road[column], road[column - 1]) + dream[row][column]

    return road[-1]

dream = [
    [1,3,1],
    [1,5,1],
    [4,2,1],
    ]

print(findSafestPath(dream))