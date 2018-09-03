import random
import math
import sys
import time
from interface import Application


class AlgoritmoGenetico:

    def __init__(self):
        #configurações
        self.tamanho_inicial_populacao = 300
        self.num_max_geracoes = 200
        self.percentual_recombinacao = 50
        self.percentual_mutacao = 5
        self.limite_populacional = 50000
        self.porcentagem_reducao_populacional = 80

        #########################
        self.melhor_fitness = 0

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
    def fitness(self, individuo):

        individuo_vetor = individuo['vetor']

        individuo_matriz = self.vetor2matriz(individuo_vetor)

        pontuacoes = [0]
        sequencia = True

        pos_vetor_anterior = individuo_vetor.index(1)

        i = 2
        acertos = 0

        #vai percorrer todos os itens do vetor (64 posicao)
        while i <= len(individuo_vetor):

            pos_vetor_atual = individuo_vetor.index(i)

            i = i + 1

            validade = self.valida_passo(individuo_matriz, pos_vetor_anterior, pos_vetor_atual)

            pos_vetor_anterior = pos_vetor_atual

            if validade and sequencia:
                pontuacoes[len(pontuacoes)-1] = pontuacoes[len(pontuacoes)-1] + 1
                acertos = acertos + 1
            elif validade:
                sequencia = True
                pontuacoes.append(1)
                acertos = acertos + 1
            else:
                sequencia = False

        #ordenando pontuacao
        pontuacoes = sorted(pontuacoes, reverse=True)

        individuo['fitness'] = acertos
        individuo['calculo_somario'] = pontuacoes

        somatorio = 0;

        multiplicador = 20

        for valor in pontuacoes:

            somatorio = somatorio + (valor * multiplicador)

            if multiplicador > 0:
                multiplicador = multiplicador - 2
            else:
                multiplicador = 0

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
        individuo['fitness'] = 0
        individuo['somatorio'] = 0
        individuo['calculo_somario'] = []
        individuo['vetor'] = vetor

        return individuo

    def atribuir_expectativa_vida(self, individuo):

        somatorio = self.fitness(individuo)

        idade = math.ceil((somatorio*20) / 1260)

        individuo['vida'] = idade
        individuo['somatorio'] = somatorio

        return individuo


    def selecao_populacao_variavel(self, populacao:list):

        #print(len(populacao))

        for i in populacao:
            if i['vida'] <= 0:
                populacao.remove(i)
            else:
                i['vida'] = i['vida'] - 1

        #print(len(populacao))

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

    def extincao_populacional(self, populacao):

        tamanho_populacao = len(populacao)

        corte = int(tamanho_populacao - (tamanho_populacao * self.porcentagem_reducao_populacional) / 100)
        random.shuffle(populacao)
        return populacao[0:corte]

    def mutacao_swap(self, individuo):
        tamanho_individuo = len(individuo)

        indece1 = random.randint(0, (tamanho_individuo - 1))
        indece2 = random.randint(0, (tamanho_individuo - 1))

        aux = individuo[indece1]
        individuo[indece1] = individuo[indece2]
        individuo[indece2] = aux

        return individuo



    def mutacao_troca_posicoes_aleatoria(self):
        pass



    def mutacao(self, populacao):

        tamanho_populacao = len(populacao)

        num_mutacao = int(tamanho_populacao - (tamanho_populacao*self.percentual_mutacao)/100)
        num_mutacao = 1

        for i in range(0, num_mutacao):
            indece = random.randint(0, (tamanho_populacao-1))

            vetor = self.mutacao_swap(populacao[indece]['vetor'])

            individuo = self.vetor_para_objeto_populacao_variavel(vetor)

            populacao[indece] = self.atribuir_expectativa_vida(individuo)

        return populacao

    def tecnica_selecao_populacao_variavel(self, populacao_inicial:list):

        tela = Application()
        tela.start()

        tempo = 1

        populacao = []
        melhor_individuo = {}

        for i in populacao_inicial:
            individuo = self.vetor_para_objeto_populacao_variavel(i)
            self.atribuir_expectativa_vida(individuo)
            populacao.append(individuo)

        while tempo < self.num_max_geracoes and self.melhor_fitness < 63:

            # avaliacao
            # selecao
            # recombinacao

            tela.show_geracao(tempo)
            tela.show_estado("Seleção")
            populacao = self.selecao_populacao_variavel(populacao)


            #Gerando estatisticas
            tela.show_estado("Estatistica")

            self.melhor_fitness = 0
            pontuacao_melhor_individuo = 0
            vida_individuo_melhor_finess = 0

            for i in populacao:
                if self.melhor_fitness < i['fitness']:
                    self.melhor_fitness = i['fitness']
                    vida_individuo_melhor_finess = i['vida']
                    melhor_individuo = i
                    pontuacao_melhor_individuo = str(i['somatorio']) + ' [' + ', '.join(str(e) for e in i['calculo_somario']) + ']'

            tela.show_status(len(populacao),
                             pontuacao_melhor_individuo,
                             self.melhor_fitness,
                             vida_individuo_melhor_finess
                             )

            #tempo de espera para trabalhar na proxima geração
            #time.sleep(.5)

            #Diminuindo populacao
            if len(populacao) > self.limite_populacional:
                tela.show_estado("Extinção")
                populacao = self.extincao_populacional(populacao)
                tela.show_tamanho_populacao(len(populacao))


            #mutacao
            tela.show_estado("Mutação")
            populacao = self.mutacao(populacao)



            tela.show_estado("Reprodução")
            novos_individuos = self.recombinacao_populacao_variavel(populacao, self.percentual_recombinacao)

            populacao = populacao + novos_individuos


            tempo = tempo + 1



        tela.show_estado("Finalizado")
        print("Fim")
        print("Relatório:")
        print('Individuo:', melhor_individuo)
        print('Geração atual: ', tempo)
        print('Tamanho população inicial: ', self.tamanho_inicial_populacao)
        print('Número máximo gerações: ', self.num_max_geracoes)
        print('Porcentagem de recombinação: ', self.percentual_recombinacao)
        print('Porcentagem de mutação: ', self.percentual_mutacao)
        print('Limite populacional: ', self.limite_populacional)
        print('Porcentagem de redução populacional: ', self.porcentagem_reducao_populacional)

        time.sleep(30)
















