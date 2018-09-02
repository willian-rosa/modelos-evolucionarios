import random
import math
import sys
import time


class AlgoritmoGenetico:

    def gerar_individuo_modelo(self):
        return list(range(1, 65))

    def gerar_populacao_inicial(self, individuo_modelo, quantidade_populacao):
        individuals = []

        for i in range(quantidade_populacao):
            random.shuffle(individuo_modelo)
            individuals.append(individuo_modelo.copy())

        return individuals

    def pegar_posicao_matriz_pelo_indece(self, matriz, indice):
        tamanho_matriz = len(matriz)

        pos = {}
        pos['linha'] = indice // tamanho_matriz
        pos['coluna'] = indice % tamanho_matriz

        return pos

    def valida_passo(self, individuo_matriz: list, pos_vetor_anterior, pos_vetor_atual):

        p_a = self.pegar_posicao_matriz_pelo_indece(individuo_matriz, pos_vetor_anterior)

        p_atual = self.pegar_posicao_matriz_pelo_indece(individuo_matriz, pos_vetor_atual)

        if (p_a['coluna'] == p_atual['coluna'] -1 and p_a['linha'] == p_atual['linha'] + 2) or \
            (p_a['coluna'] == p_atual['coluna'] - 2 and p_a['linha'] == p_atual['linha'] + 1) or \
            (p_a['coluna'] == p_atual['coluna'] + 1 and p_a['linha'] == p_atual['linha'] + 2) or \
            (p_a['coluna'] == p_atual['coluna'] + 2 and p_a['linha'] == p_atual['linha'] + 1) or \
            (p_a['coluna'] == p_atual['coluna'] + 2 and p_a['linha'] == p_atual['linha'] - 1) or \
            (p_a['coluna'] == p_atual['coluna'] + 1 and p_a['linha'] == p_atual['linha'] - 2) or \
            (p_a['coluna'] == p_atual['coluna'] - 1 and p_a['linha'] == p_atual['linha'] - 2) or \
            (p_a['coluna'] == p_atual['coluna'] - 2 and p_a['linha'] == p_atual['linha'] - 1) :

            return True



        return False


    '''
    Melhor performace é 631
    
    '''
    def fitness(self, individuo_vetor:list):

        individuo_matriz = self.vetor2matriz(individuo_vetor)

        pontuacoes = [0]
        sequencia = True

        pos_vetor_anterior = individuo_vetor.index(1)

        i = 2

        #vai percorrer todos os itens do vetor (64 posicao)
        while i <= len(individuo_vetor):

            pos_vetor_atual = individuo_vetor.index(i)

            i = i + 1

            validade = self.valida_passo(individuo_matriz, pos_vetor_anterior, pos_vetor_atual)

            pos_vetor_anterior = pos_vetor_atual

            if validade and sequencia:
                pontuacoes[len(pontuacoes)-1] = pontuacoes[len(pontuacoes)-1] + 1
            elif validade:
                sequencia = True
                pontuacoes.append(1)
            else:
                sequencia = False


        somatorio = 0;

        for i, valor in enumerate(pontuacoes):
            multiplicador = 10 - i

            if multiplicador < 0:
                multiplicador = 0

            somatorio = somatorio + (valor * multiplicador + 1)

        return somatorio

    def vetor2matriz(self, vetor:list):

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

    def vetor_para_objeto_populacao_variavel(self, vetor):

        individuo = {}
        individuo['vida'] = 0
        individuo['vetor'] = vetor

        return individuo

    def atribuir_expectativa_vida(self, individuo):

        somatorio = self.fitness(individuo['vetor'])

        idade = math.ceil((somatorio*10) / 631)

        individuo['vida'] = idade

        return individuo


    def selecao_populacao_variavel(self, populacao:list):

        for i in populacao:
            if i['vida'] == 0:
                populacao.remove(i)

        return populacao

    def permutacao(self, individual1: list, individual2: list, ponto_corte):

        novo_individual = individual1[:ponto_corte]

        for i in individual2:
            if not novo_individual.count(i):
                novo_individual.append(i)

        return novo_individual

    def recombinacao_populacao_variavel(self, populacao:list, percentual_recombinacao:int):

        tamanho_populacao = len(populacao)

        num_recombinacao = int((tamanho_populacao*percentual_recombinacao)/100)

        posicoes_aleatorias = list(range(tamanho_populacao))
        random.shuffle(posicoes_aleatorias)

        novos_individuos = []

        for i in range(int(num_recombinacao / 2)):
            ponto_corte = random.randint(1, (tamanho_populacao-1))

            individual1 = populacao[posicoes_aleatorias[i]]['vetor']
            individual2 = populacao[posicoes_aleatorias[(num_recombinacao - 1) - i]]['vetor']

            novo_individuo1 = self.vetor_para_objeto_populacao_variavel(self.permutacao(individual1, individual2, ponto_corte))
            novo_individuo2 = self.vetor_para_objeto_populacao_variavel(self.permutacao(individual2, individual1, ponto_corte))

            self.atribuir_expectativa_vida(novo_individuo1)
            self.atribuir_expectativa_vida(novo_individuo2)


            novos_individuos.append(novo_individuo1)
            novos_individuos.append(novo_individuo2)

        return novos_individuos


    def tecnica_selecao_populacao_variavel(self, populacao_inicial:list, num_max_geracoes, percentual_recombinacao, percentual_mutacao):

        tempo = 1

        populacao = []

        for i in populacao_inicial:
            individuo = self.vetor_para_objeto_populacao_variavel(i)
            self.atribuir_expectativa_vida(individuo)
            populacao.append(individuo)

        while tempo < num_max_geracoes:



            #populacao = self.selecao_populacao_variavel(populacao)

            #novos_individuos = self.recombinacao_populacao_variavel(populacao, percentual_recombinacao)

            #populacao = populacao + novos_individuos

            print('populacao', tempo, len(populacao))


            #tempo de espera para trabalhar na proxima geração
            time.sleep(2)







            tempo = tempo + 1













        #avaliacao
        #selecao
        #recombinacao





