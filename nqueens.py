# N-Queens Problem
import random
import time
start_time = time.time()

# Define size of board
SIZE_OF_BOARD = 60
POPULATION_SIZE = 50
TOURNAMENT_SIZE = 5
MAX_MUTATIONS = 5
generation = 0

population = []

startingIndividual = []
# Populate starting individual
for x in range(0, SIZE_OF_BOARD):
    startingIndividual.append(x)

for x in range(0, POPULATION_SIZE - 1):
    temp = startingIndividual[:]
    random.shuffle(temp)
    if temp not in population:
        population.append(temp)


def fitnessCheck(individual):
    fitness = (SIZE_OF_BOARD * (SIZE_OF_BOARD - 1)) / 2
    index1 = 0
    index2 = 0

    for queen1 in individual:
        index2 = 0
        for queen2 in individual:
            if (queen1 - index1 == queen2 - index2) or (queen1 + index1 == queen2 + index2):
                if index1 == index2:
                    index2 += 1
                    continue
                fitness -= 1
            index2 += 1
        index1 += 1
    return fitness

hasFoundSolution = False

def goalCheck():
    if (fitnessPopulation[0][0] == (SIZE_OF_BOARD * (SIZE_OF_BOARD - 1)) / 2):
        print("Goal individual found: " + str(fitnessPopulation[0][1]) + str(fitnessPopulation[0][0]))
        print("Generations ran: " + str(generation))
        print("Time to termination: " + str(time.time()-start_time) + " seconds")
        return False
    else:
        return True

def crossover(individualA, individualB):
    placeToSplit = random.randint(0, SIZE_OF_BOARD)
    newIndividual = individualA[0: placeToSplit]
    for queen in individualB:
        if queen not in newIndividual:
            newIndividual.append(queen)

    return newIndividual

def runGeneration():
    tournament1, tournament2 = [], []

    for x in range(0, TOURNAMENT_SIZE):
        tournament1.append(random.choice(fitnessPopulation))
        tournament2.append(random.choice(fitnessPopulation))

    tournament1 = sorted(tournament1, key=lambda tup: tup[0])
    tournament2 = sorted(tournament2, key=lambda tup: tup[0])

    selectedA, selectedB = tournament1[0][1], tournament2[0][1]

    newIndividual = crossover(selectedA, selectedB)

    print("Parents: " + str(selectedA) + str(fitnessCheck(selectedA)) + " and " + str(selectedB) + str(fitnessCheck(selectedB)))
    print("yield: " + str(newIndividual) + str(fitnessCheck(newIndividual)))

    for x in range(0, random.randint(0, MAX_MUTATIONS)):
        indexA = random.randint(0, SIZE_OF_BOARD - 1)
        indexB = random.randint(0, SIZE_OF_BOARD - 1)

        print("Applying mutation - swapping " + str(newIndividual[indexA]) + " with " + str(newIndividual[indexB]))
        newIndividual[indexA], newIndividual[indexB] = newIndividual[indexB], newIndividual[indexA]

    return newIndividual

fitnessPopulation = []

for individual in population:
    fitness = fitnessCheck(individual)
    fitnessPopulation.append((fitness, individual))

fitnessPopulation = sorted(fitnessPopulation, key=lambda tup: tup[0], reverse=True)

while goalCheck():
    print("Starting generation: " + str(generation))
    print("Top individual: " + str(fitnessPopulation[0][1]) + str(fitnessPopulation[0][0]))
    newIndividual = runGeneration()

    if fitnessCheck(newIndividual) > fitnessPopulation[-1][0]:
        print("The new individual has replaced " + str(fitnessPopulation[-1][1]) + str(fitnessPopulation[-1][0]))
        fitnessPopulation.remove(fitnessPopulation[-1])
        fitnessPopulation.append((fitnessCheck(newIndividual), newIndividual))
        fitnessPopulation = sorted(fitnessPopulation, key=lambda tup: tup[0], reverse=True)

    print("END OF GENERATION \n------------------------------\n")
    generation += 1








