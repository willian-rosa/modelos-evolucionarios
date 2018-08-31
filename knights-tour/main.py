from algoritmo_genetico import AlgoritmoGenetico
# import sys
# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))

#argumentos
tamanho_inicial_populacao = 20
num_max_geracoes = 100


ag = AlgoritmoGenetico()

#populacao_inicial = ag.gerar_populacao_inicial(ag.gerar_individuo_modelo(), tamanho_inicial_populacao)

#ag.tecnica_selecao_populacao_variavel(populacao_inicial, num_max_geracoes)



matriz = ag.vetor2matriz(ag.gerar_individuo_modelo())


s = ag.fitness(matriz)

print(s)


