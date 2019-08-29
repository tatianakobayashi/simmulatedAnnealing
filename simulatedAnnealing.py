import sys
from random import seed, randrange, random

ALPHA = 0.5
BETA = 0.5

FINAL_TEMPERATURE = 1

SIZE = 100

FILE_NAME = 'teste_2.txt'

# Leitura da entrada
with open(FILE_NAME, 'r') as f:
    lines = f.readlines()
    numberOfStreets = int(lines[0])
    nodes = [[int(val) for val in line.split()] for line in lines[1:]]

# print(numberOfStreets)
# print(str(nodes))

seed(None)


def viable(solution):
    hasFirePrevention = [False for x in range(numberOfStreets)]

    for node in solution:
        # print(node)
        for pos in node:
            # print(pos)
            hasFirePrevention[pos - 1] = True

    for hasPrev in hasFirePrevention:
        if not hasPrev:
            return False
    # print('Viable : ' + str(solution) + str(hasFirePrevention))
    return True


def new_random_node():
    newA = randrange(1, numberOfStreets+1)
    newB = randrange(1, numberOfStreets+1)
    while [newA, newB] not in nodes:
        newA = randrange(1, numberOfStreets + 1)
        newB = randrange(1, numberOfStreets + 1)
    return [newA, newB]


def is_in_solution(node, solution):
    # print(node)
    # print(solution)
    # print(node in solution)
    return node in solution


solution = list(nodes[:2])
bestSolution = list(nodes)

if sys.version_info.major < 3:
    temperature = sys.maxint
else:
    temperature = sys.maxsize

while temperature >= FINAL_TEMPERATURE or not viable(bestSolution):
    for it in range(SIZE):
        newSolution = solution
        randomNeighbor = new_random_node()
        if not is_in_solution(randomNeighbor, solution):
            newSolution.append(randomNeighbor)
            while not viable(newSolution) and newSolution is True:
                print('removing nodes from solution')
                # remove item aleatorio
                removeIndex = randrange(len(newSolution))
                newSolution.pop(removeIndex)
            delta = len(solution) - len(newSolution)
            num = random()
            if delta >= 0 or num < FINAL_TEMPERATURE ** (delta / temperature):
                solution = newSolution
        else:
            # remove item aleatorio
            removeIndex = randrange(len(newSolution))
            newSolution.pop(removeIndex)
            # adiciona novo item
            newNode = new_random_node()
            if not is_in_solution(randomNeighbor, solution):
                # newNode = new_random_node()
                newSolution.append(newNode)

            delta = len(solution) - len(newSolution)
            num = random()
            if delta >= 0 or num < FINAL_TEMPERATURE ** (delta / temperature):
                solution = newSolution
        # print('Solution: ' + str(solution) + ' Len: ' + str(len(solution)) + ' Best: ' + str(bestSolution) + ' Len: ' + str(len(bestSolution)))
        if len(solution) < len(bestSolution) and viable(solution):
            # print('Change')
            bestSolution = list(solution)
        # else:
            # print('No change')
        temperature *= BETA
        # print(' Best: ' + str(bestSolution) + ' Len: ' + str(len(bestSolution)))

print(bestSolution)
print(len(bestSolution))
