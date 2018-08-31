import random

def generateInitialPolulation(individual, numInd):

    individuals = []

    for i in range(numInd):
        random.shuffle(individual)
        individuals.append(individual.copy())

    return individuals

def fitness(individual):

    conflitos = 0

    for i in range(7):
        for j in range(i+1, 8):
            pos = individual[i]
            posNext = individual[j]
            if pos+(j-i) == posNext  or pos-(j-i) == posNext:
                conflitos += 1

    return conflitos

def recombination(population):

    newPopulation = []

    for i in population:
        newPopulation = i

#função de avaliação
def evaluation(population):

    representation = []

    for i, individual in enumerate(population):
        item = []
        item.append(i)
        item.append(fitness(individual))

        representation.append(item)


    sortedRepresentation = sortRepresentation(representation)

    sortedPopulation = []

    for item in sortedRepresentation:
        sortedPopulation.append(population[item[0]])

    return sortedPopulation

def sortRepresentation(representation):

    for item in range(len(representation) - 1, 0, -1):
        for i in range(item):
            if representation[i][1] > representation[i + 1][1]:
                temp = representation[i]
                representation[i] = representation[i + 1]
                representation[i + 1] = temp

    return representation

def selection(population:list, cutoff):
    return population[:cutoff]

def permutations(individual1:list, individual2:list, cutoff):

    newIndividual = individual1[:cutoff]

    for i in individual2:
        if not newIndividual.count(i):
            newIndividual.append(i)

    return newIndividual

def recombination(population, sizePairs):

    numsSeqRecombination = list(range(sizePairs))
    random.shuffle(numsSeqRecombination)

    newPopulation = []

    for i in range(int(sizePairs/2)):
        cutoff = random.randint(1, 7)

        individual1 = population[numsSeqRecombination[i]]
        individual2 = population[numsSeqRecombination[(sizePairs-1)-i]]

        newPopulation.append(individual1)
        newPopulation.append(individual2)
        newPopulation.append(permutations(individual1, individual2, cutoff))
        newPopulation.append(permutations(individual2, individual1, cutoff))

    return newPopulation



