import random
import math
import sys
import time
from interface import Application
from no import No
from individuo import Individuo



class AlgoritmoGenetico:

    def __init__(self):
        self.operadores = ['+', '-', '*', '%']
        self.termos = ['x', -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

        self.possiveis_valores = self.operadores + self.termos

        self.tamanho_inicial_populacao = 100
        self.altura_maxima = 10
        self.num_max_geracoes = 100
        self.porcentagem_reducao_populacional = 80

        #########################
        self.melhor_fitness = 99999



    def gerar_subarvore(self, raiz):

        v1 = random.choice(self.possiveis_valores)
        noEsquerdo = No(v1, raiz)

        raiz.esquerdo = noEsquerdo

        if self.operadores.count(noEsquerdo.valor):
            self.gerar_subarvore(raiz.esquerdo)

        v2 = random.choice(self.possiveis_valores)
        noDireito = No(v2, raiz)

        raiz.direito = noDireito

        if self.operadores.count(noDireito.valor):
            self.gerar_subarvore(raiz.direito)

        return raiz

    def gerar_individuo(self):

        operador = random.choice(self.operadores)

        raiz = No(operador)

        individuo = Individuo(raiz)

        self.gerar_subarvore(individuo.raiz)

        individuo.altura()
        individuo.fitness()

        return individuo

    def gerar_populacao_inicial(self):
        individuals = []

        individuo = self.gerar_individuo()

        if individuo.altura() <= self.altura_maxima:
            individuals.append(individuo)


        while len(individuals) < self.tamanho_inicial_populacao:
            individuo = self.gerar_individuo()

            if individuo.altura() <= self.altura_maxima:
                individuals.append(individuo)

        return individuals

    def ordenacao_populacao(self, populacao:list):

        for item in range(len(populacao) - 1, 0, -1):
            for i in range(item):
                if populacao[i].resultado > populacao[i + 1].resultado:
                    temp = populacao[i]
                    populacao[i] = populacao[i + 1]
                    populacao[i + 1] = temp

        return populacao

    def selecao_elitista(self, populacao:list):

        populacao = self.ordenacao_populacao(populacao)

        tamanho_populacao = len(populacao)

        corte = int(tamanho_populacao - (tamanho_populacao * self.porcentagem_reducao_populacional) / 100)

        return populacao[:corte]


    def tecnica_selecao_elitista(self, populacao_inicial:list):

        # teste = populacao_inicial[0] # type:Individuo

        tela = Application()
        tela.start()

        tempo = 1

        populacao = populacao_inicial
        melhor_individuo = None


        while tempo < self.num_max_geracoes and self.melhor_fitness != 0:

            tela.show_geracao(tempo)

            #seleção
            tela.show_estado("Seleção")
            populacao = self.selecao_elitista(populacao)


            #Gerando estatisticas
            tela.show_estado("Estatistica")

            self.melhor_fitness = 9999
            pontuacao_melhor_individuo = 0
            vida_individuo_melhor_finess = 0

            # for i in populacao:
            #     if self.melhor_fitness < i['fitness']:
            #         self.melhor_fitness = i['fitness']
            #         vida_individuo_melhor_finess = i['vida']
            #         melhor_individuo = i
            #         pontuacao_melhor_individuo = str(i['somatorio']) + ' [' + ', '.join(str(e) for e in i['calculo_somario']) + ']'
            #
            # tela.show_status(len(populacao),
            #                  pontuacao_melhor_individuo,
            #                  self.melhor_fitness,
            #                  vida_individuo_melhor_finess
            #                  )

            #mutacao
            tela.show_estado("Mutação")
            # populacao = self.mutacao(populacao)

            #reprodução
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
