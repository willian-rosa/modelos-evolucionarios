from algoritmo_genetico import AlgoritmoGenetico
# import sys
# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))

#argumentos
tamanho_inicial_populacao = 20
num_max_geracoes = 100
percentual_recombinacao = 50
percentual_mutacao = 5


ag = AlgoritmoGenetico()


#exemplo_funcional = [63, 20, 3, 24, 59, 36, 5, 26, 2, 23, 64, 37, 4, 25, 58, 35, 19, 62, 21, 50, 55, 60, 27, 6, 22, 1, 54, 61, 38, 45, 34, 57, 53, 18, 49, 44, 51, 56, 7, 28, 12, 15, 52, 39, 46, 31, 42, 33, 17, 48, 13, 10, 43, 40, 29, 8, 14, 11, 16, 47, 30, 9, 32, 41]


populacao_inicial = ag.gerar_populacao_inicial(ag.gerar_individuo_modelo(), tamanho_inicial_populacao)

ag.tecnica_selecao_populacao_variavel(populacao_inicial, num_max_geracoes, percentual_recombinacao, percentual_mutacao)

