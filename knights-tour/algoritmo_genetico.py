import random
import math

class AlgoritmoGenetico:

    def gerar_individuo_modelo(self):
        return list(range(1, 65))

    def gerar_populacao_inicial(self, individuo_modelo, quantidade_populacao):
        individuals = []

        for i in range(quantidade_populacao):
            random.shuffle(individuo_modelo)
            individuals.append(individuo_modelo.copy())

        return individuals

    def fitness(self, individuo_matriz):

        sequencia_certa = 0

        for i in individuo_matriz:

            sequencia_certa = sequencia_certa + 1

        return sequencia_certa

    def vetor2matriz(self, vetor):

        raiz = int(math.sqrt(len(vetor)))

        matriz = []

        for i in range(0, raiz):
            matriz.append(vetor[i*raiz:raiz*(i+1)])

        return matriz

    def matriz2vetor(self, matriz):

        vetor = []

        for i in matriz:
            vetor = vetor + i

        return vetor



    def tecnica_selecao_populacao_variavel(self, populacao_inicial, num_max_geracoes):
        pass

        #avaliacao
        #selecao
        #recombinacao





