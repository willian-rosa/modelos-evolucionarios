import genetic_algorithm

#configurações
qtdCycles = 1000
tamanhoPopulacao = 20
qtdPares = 10

#população inicial aleatória
individual = [0, 1, 2, 3, 4, 5, 6, 7]
population = genetic_algorithm.generateInitialPolulation(individual, tamanhoPopulacao)

bestAll = []
bestScore = 99999

t = 0

while t < qtdCycles and bestScore > 0:

    classifiedPopulation = genetic_algorithm.evaluation(population)

    bestCycle = classifiedPopulation[0]
    scoreCycle = genetic_algorithm.fitness(bestCycle)

    if scoreCycle < bestScore:
        bestAll = bestCycle
        bestScore = scoreCycle

    selectedPopulation = genetic_algorithm.selection(classifiedPopulation, qtdPares)

    population = genetic_algorithm.recombination(selectedPopulation, qtdPares)

    t = t + 1

print("------------------------------------------------")
print("Melhor indivíduo: ", bestAll)
print("Quant. conflitos: ", bestScore)
print("Quant. de gerações: ", t)