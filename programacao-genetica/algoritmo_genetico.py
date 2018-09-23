import random
import math
import sys
import time
from interface import Application
from no import No
from individuo import Individuo
import copy



class AlgoritmoGenetico:

    def __init__(self):
        self.operadores = ['+', '-', '*', '%']
        self.termos = ['x', -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

        self.possiveis_valores = self.operadores + self.termos

        self.tamanho_inicial_populacao = 100
        self.altura_maxima = 10
        self.num_max_geracoes = 100
        self.porcentagem_reducao_populacional = 80

        self.percentual_recombinacao = 50
        self.percentual_mutacao = 50

        #########################
        self.melhor_individuo = None #type Individuo



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
        individuo.fitness(self.altura_maxima)

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

    def tree2list(self, raiz:No, lista:list):

        lista.append(raiz)

        if raiz.direito:
            lista = self.tree2list(raiz.direito, lista)

        if raiz.esquerdo:
            lista = self.tree2list(raiz.esquerdo, lista)

        return lista


    def permutacao(self, individual1:Individuo, individual2:Individuo):

        novo_individual1 = copy.deepcopy(individual1)
        novo_individual2 = copy.deepcopy(individual2)

        lista_nos1 = self.tree2list(novo_individual1.raiz, [])
        ponto_troca1 = random.randint(1, len(lista_nos1)-1)

        lista_nos2 = self.tree2list(novo_individual2.raiz, [])
        ponto_troca2 = random.randint(1, len(lista_nos2)-1)

        no_itercambio1 = lista_nos1[ponto_troca1] # type:No
        no_itercambio2 = lista_nos2[ponto_troca2] # type:No

        pai_aux = no_itercambio1.pai

        no_itercambio1.pai = no_itercambio2.pai
        no_itercambio2.pai = pai_aux

        if no_itercambio1.pai.esquerdo == no_itercambio2:
            no_itercambio1.pai.esquerdo = no_itercambio1
        else:
            no_itercambio1.pai.direito = no_itercambio1

        if no_itercambio2.pai.esquerdo == no_itercambio1:
            no_itercambio2.pai.esquerdo = no_itercambio2
        else:
            no_itercambio2.pai.direito = no_itercambio2

        novo_individual1.altura()
        novo_individual1.fitness(self.altura_maxima)

        novo_individual2.altura()
        novo_individual2.fitness(self.altura_maxima)



        return [novo_individual1, novo_individual2]




    def recombinacao_populacao(self, populacao:list, percentual_recombinacao:int):

        tamanho_populacao = len(populacao)

        num_recombinacao = int((tamanho_populacao*percentual_recombinacao)/100)

        posicoes_aleatorias = list(range(tamanho_populacao))
        random.shuffle(posicoes_aleatorias)

        novos_individuos = []

        for i in range(int(num_recombinacao / 2)):

            individual1 = populacao[posicoes_aleatorias[i]]
            individual2 = populacao[posicoes_aleatorias[(num_recombinacao - 1) - i]]

            novos_individuos = novos_individuos + self.permutacao(individual1, individual2)

        return novos_individuos

    def mutacao(self, populacao):

        tamanho_populacao = len(populacao)

        num_mutacao = int(tamanho_populacao - (tamanho_populacao*self.percentual_mutacao)/100)

        for i in range(0, num_mutacao):
            indece = random.randint(0, (tamanho_populacao-1))

            novo_individual1 = populacao[indece]

            lista_nos1 = self.tree2list(novo_individual1.raiz, [])
            ponto_troca1 = random.randint(1, len(lista_nos1) - 1)

            no_itercambio1 = lista_nos1[ponto_troca1]  # type:No

            operador = random.choice(self.operadores)

            raiz = No(operador)

            novo_individual_gerado = Individuo(raiz)

            self.gerar_subarvore(novo_individual_gerado.raiz)

            pai_aux = no_itercambio1.pai

            novo_individual_gerado.raiz.pai = pai_aux


            if no_itercambio1.pai.esquerdo == pai_aux:
                no_itercambio1.pai.esquerdo = novo_individual_gerado.raiz
            else:
                no_itercambio1.pai.direito = novo_individual_gerado.raiz


            novo_individual1.altura()
            novo_individual1.fitness(self.altura_maxima)

        return populacao


    def tecnica_selecao_elitista(self, populacao_inicial:list):


        tela = Application()
        tela.start()

        tempo = 1

        populacao = populacao_inicial
        self.melhor_individuo = populacao[0]

        while tempo < self.num_max_geracoes and self.melhor_individuo.resultado != 0:

            #tela.show_geracao(tempo)

            #seleção
            #tela.show_estado("Seleção")
            populacao = self.selecao_elitista(populacao)


            #Gerando estatisticas
            #tela.show_estado("Estatistica")

            for i in populacao:
                if self.melhor_individuo.resultado > i.resultado:
                    self.melhor_individuo = copy.deepcopy(i)
                    print(self.melhor_individuo.altura(), self.altura_maxima)

                    tela.show_geracao(tempo)

                    tela.show_status(len(populacao),
                                     self.melhor_individuo.resultado,
                                     self.melhor_individuo.formula(),
                                     0
                                     )

            #mutacao
            #tela.show_estado("Mutação")
            populacao = self.mutacao(populacao)

            #reprodução
            #tela.show_estado("Reprodução")

            novos_individuos = self.recombinacao_populacao(populacao, self.percentual_recombinacao)

            populacao = populacao + novos_individuos


            tempo = tempo + 1



        tela.show_estado("Finalizado")
        print("Fim")
        print("Relatório:")
        print('Individuo:', str(self.melhor_individuo.resultado)+ ' - ('+self.melhor_individuo.formula()+')')
        print('Geração atual: ', tempo)
        print('Tamanho população inicial: ', self.tamanho_inicial_populacao)
        print('Número máximo gerações: ', self.num_max_geracoes)
        print('Porcentagem de recombinação: ', self.percentual_recombinacao)
        # print('Porcentagem de mutação: ', self.percentual_mutacao)
        #print('Limite populacional: ', self.limite_populacional)
        print('Porcentagem de redução populacional: ', self.porcentagem_reducao_populacional)
