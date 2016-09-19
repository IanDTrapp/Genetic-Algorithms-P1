import math

text_file = open("tsp.txt", "r")
lines = text_file.read().split(' ')

lines = list(filter(('').__ne__, lines))

locationArray = []

individual = [99, 105, 55, 36, 50, 58, 108, 48, 4, 42, 86, 111, 24, 30, 84, 2, 66, 38, 9, 67, 102, 78, 31, 117, 49, 95, 12, 26, 6, 33, 47, 126, 19, 79, 11, 44, 39, 8, 7, 43, 116, 29, 106, 76, 100, 113, 3, 52, 110, 56, 94, 101, 34, 80, 109, 124, 125, 118, 69, 70, 96, 77, 97, 103, 89, 57, 21, 112, 5, 1, 63, 51, 93, 59, 61, 107, 16, 83, 60, 72, 13, 74, 18, 46, 75, 14, 68, 53, 27, 114, 82, 62, 85, 40, 28, 17, 23, 120, 64, 71, 0, 81, 123, 122, 90, 37, 22, 119, 73, 91, 98, 88, 121, 92, 20, 45, 41, 104, 54, 87, 10, 25, 32, 65, 15, 115, 35]


for x in range(5, lines.__len__(), 3):
    thisNode = lines[x]
    thisX = lines[x + 1]
    thisY = lines[x + 2]

    locationArray.append((thisNode, thisX, thisY))



fitness = 0
index = 0

for x in individual:
    if (index == 0):
        index += 1
        continue
    else:

        xa = int(locationArray[x - 1][1])
        xb = int(locationArray[x - 2][1])
        ya = int(locationArray[x - 1][2])
        yb = int(locationArray[x - 2][2])
        dist = math.sqrt(((xa - xb) ** 2) + ((ya - yb) ** 2))
        fitness += dist

print(fitness)
