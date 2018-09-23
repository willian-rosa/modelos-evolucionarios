from algoritmo_genetico import AlgoritmoGenetico
import sys
# import sys
# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))


ag = AlgoritmoGenetico()





tipo_ag = 'elitista'

if tipo_ag == 'pv':
    # #argumentos
    # ag.tamanho_inicial_populacao = 1000
    # ag.num_max_geracoes = 100
    # ag.percentual_recombinacao = 100
    # ag.percentual_mutacao = 30
    # ag.limite_populacional = 5000
    # ag.porcentagem_reducao_populacional = 50
    #
    # populacao_inicial = ag.gerar_populacao_inicial(ag.gerar_individuo_modelo(), ag.tamanho_inicial_populacao)
    #
    # ag.tecnica_selecao_populacao_variavel(populacao_inicial)
    print("teste")

elif tipo_ag == 'elitista':
    #argumentos
    ag.tamanho_inicial_populacao = 400
    ag.altura_maxima = 3
    ag.num_max_geracoes = 2000

    ag.percentual_mutacao = 10
    ag.percentual_recombinacao = 100
    ag.porcentagem_reducao_populacional = 50

    populacao_inicial = ag.gerar_populacao_inicial()

    ag.tecnica_selecao_elitista(populacao_inicial)



else:
    print("Erro ao selecionar o tipo do algoritmo")
    sys.exit()






