# TSP Problem
import random
import time
import math

start_time = time.time()

# Define size of board
DIMENSION = 127
POPULATION_SIZE = 100
TOURNAMENT_SIZE = 5
generation = 0

population = []
locationArray = []

# Load in xy coordinates
text_file = open("tsp.txt", "r")
lines = text_file.read().split(' ')

lines = list(filter(('').__ne__, lines))

for x in range(5, lines.__len__(), 3):
    thisNode = lines[x]
    thisX = lines[x + 1]
    thisY = lines[x + 2]

    locationArray.append((thisNode, thisX, thisY))

locationArray.append((lines[x], lines[x+1], lines[x+2]))


startingIndividual = []
# Populate starting individual
for x in range(0, DIMENSION):
    startingIndividual.append(x)

for x in range(0, POPULATION_SIZE - 1):
    temp = startingIndividual[:]
    random.shuffle(temp)
    if temp not in population:
        population.append(temp)

print(population)

def fitnessCheck(individual):
    fitness = 0
    index = 0

    for x in individual:
        if(index == 0):
            index += 1
            continue
        else:

            xa = int(locationArray[x - 1][1])
            xb = int(locationArray[x - 2][1])
            ya = int(locationArray[x - 1][2])
            yb = int(locationArray[x - 2][2])
            dist = math.sqrt((xa - xb)**2 + (ya - yb)**2)
            fitness += dist

    return fitness
    print(fitness)


hasFoundSolution = False

def goalCheck():
    if fitnessPopulation[0][0] == 118282:
        print("Goal individual found: " + str(fitnessPopulation[0][1]) + str(fitnessPopulation[0][0]))
        print("Generations ran: " + str(generation))
        print("Time to termination: " + str(time.time()-start_time) + " seconds")
        return False
    else:
        return True

def crossover(individualA, individualB):
    placeToSplit = random.randint(0, DIMENSION)
    newIndividual = individualA[0: placeToSplit]
    for node in individualB:
        if node not in newIndividual:
            newIndividual.append(node)

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
    print("Fitness:" + str(fitnessCheck(newIndividual)))

    for x in range(0, random.randint(1, 15)):
        indexA = random.randint(0, DIMENSION - 1)
        indexB = random.randint(0, DIMENSION - 1)

        #print("Applying mutation - swapping " + str(newIndividual[indexA]) + " with " + str(newIndividual[indexB]))
        newIndividual[indexA], newIndividual[indexB] = newIndividual[indexB], newIndividual[indexA]

    return newIndividual

fitnessPopulation = []

for individual in population:
    fitness = fitnessCheck(individual)
    fitnessPopulation.append((fitness, individual))

fitnessPopulation = sorted(fitnessPopulation, key=lambda tup: tup[0])
print(fitnessPopulation)
#
while goalCheck():
    print("Starting generation: " + str(generation))
    print("Top individual: " + str(fitnessPopulation[0][1]) + "\nFitness: " + str(fitnessPopulation[0][0]))
    newIndividual = runGeneration()

    print("The new individual has replaced a random individual")
    fitnessPopulation.remove(random.choice(fitnessPopulation))
    fitnessPopulation.append((fitnessCheck(newIndividual), newIndividual))
    fitnessPopulation = sorted(fitnessPopulation, key=lambda tup: tup[0])

    print("END OF GENERATION \n------------------------------\n")
    generation += 1

