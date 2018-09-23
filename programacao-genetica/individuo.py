from no import No
import math


import time


class Individuo:

    raiz = None

    def __init__(self, raiz:No):
        self.raiz = raiz
        self._ordem_calculo = []
        self.resultado = 99999


    def altura(self, raiz = None):

        if raiz == None:
            raiz = self.raiz

        if raiz == None:
            return -1
        else:

            alturaDireita = -1
            alturaEsquerda = -1

            if raiz.direito:
                alturaDireita = self.altura(raiz.direito)

            if raiz.esquerdo:
                alturaEsquerda = self.altura(raiz.esquerdo)

            if alturaEsquerda < alturaDireita:
                return alturaDireita + 1
            else:
                return alturaEsquerda + 1

    def pos_ordem(self, no:No):

        if not no:
            return

        self.pos_ordem(no.esquerdo)

        self._ordem_calculo.append(no.valor)

        self.pos_ordem(no.direito)


    def _resultado_funcao(self, valor_x):

        self._ordem_calculo = []

        self.pos_ordem(self.raiz)

        formula = ''

        for i in self._ordem_calculo:
            if i == 'x':
                i = valor_x
            formula = formula + ' ' + str(i)

        try:
            return eval(formula)
        except ZeroDivisionError:
            return 9999
        except:
            pass



    def fitness(self, altura_maxima):

        if self.altura() > altura_maxima:
            self.resultado = 99999
        else:
            y = [0.67, 2.00, 4.00, 6.67, 10.00, 14.00, 18.67, 24.00, 30.00, 36.67]

            somatorio = 0

            for i in range(1, 11):
                resultado_x = self._resultado_funcao(i)
                resultado_pacial = y[i-1] - resultado_x
                somatorio = (resultado_pacial * resultado_pacial) + somatorio


            resultado_comparacao = math.sqrt(somatorio)

            self.resultado = resultado_comparacao

    def formula(self):

        self._ordem_calculo = []

        self.pos_ordem(self.raiz)

        formula = ''

        for i in self._ordem_calculo:
            formula = formula + ' ' + str(i)

        return formula

