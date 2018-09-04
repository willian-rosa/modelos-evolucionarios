from algoritmo_genetico import AlgoritmoGenetico
import sys
# import sys
# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))




ag = AlgoritmoGenetico()



#exemplo_funcional = [63, 20, 3, 24, 59, 36, 5, 26, 2, 23, 64, 37, 4, 25, 58, 35, 19, 62, 21, 50, 55, 60, 27, 6, 22, 1, 54, 61, 38, 45, 34, 57, 53, 18, 49, 44, 51, 56, 7, 28, 12, 15, 52, 39, 46, 31, 42, 33, 17, 48, 13, 10, 43, 40, 29, 8, 14, 11, 16, 47, 30, 9, 32, 41]
exemplo_funcional = [20, 63, 3, 24, 59, 36, 5, 26, 2, 23, 64, 37, 4, 25, 58, 35, 19, 62, 21, 50, 55, 60, 27, 6, 22, 1, 54, 61, 38, 45, 34, 57, 53, 18, 49, 44, 51, 56, 7, 28, 12, 15, 52, 39, 46, 31, 42, 33, 17, 48, 13, 10, 43, 40, 29, 8, 14, 11, 16, 47, 30, 9, 32, 41]


#populacao_inicial[410] = exemplo_funcional




tipo_ag = 'elitista'

if tipo_ag == 'pv':
    #argumentos
    ag.tamanho_inicial_populacao = 500
    ag.num_max_geracoes = 200
    ag.percentual_recombinacao = 70
    ag.percentual_mutacao = 10
    ag.limite_populacional = 15000
    ag.porcentagem_reducao_populacional = 40

    populacao_inicial = ag.gerar_populacao_inicial(ag.gerar_individuo_modelo(), ag.tamanho_inicial_populacao)

    ag.tecnica_selecao_populacao_variavel(populacao_inicial)

elif tipo_ag == 'elitista':
    #argumentos
    ag.tamanho_inicial_populacao = 4000
    ag.num_max_geracoes = 800
    ag.percentual_recombinacao = 100
    ag.percentual_mutacao = 15
    ag.limite_populacional = 15000
    ag.porcentagem_reducao_populacional = 50

    populacao_inicial = ag.gerar_populacao_inicial(ag.gerar_individuo_modelo(), ag.tamanho_inicial_populacao)

    #populacao_inicial[410] = exemplo_funcional

    ag.tecnica_selecao_elitista(populacao_inicial)

else:
    print("Erro ao selecionar o tipo do algoritmo")
    sys.exit()






