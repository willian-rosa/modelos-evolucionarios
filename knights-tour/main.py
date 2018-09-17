from algoritmo_genetico import AlgoritmoGenetico
import sys
# import sys
# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))




ag = AlgoritmoGenetico()


tipo_ag = 'elitista'

if tipo_ag == 'pv':
    #argumentos
    ag.tamanho_inicial_populacao = 1000
    ag.num_max_geracoes = 100
    ag.percentual_recombinacao = 100
    ag.percentual_mutacao = 30
    ag.limite_populacional = 5000
    ag.porcentagem_reducao_populacional = 50

    populacao_inicial = ag.gerar_populacao_inicial(ag.gerar_individuo_modelo(), ag.tamanho_inicial_populacao)

    ag.tecnica_selecao_populacao_variavel(populacao_inicial)

elif tipo_ag == 'elitista':
    #argumentos
    ag.tamanho_inicial_populacao = 2000
    ag.num_max_geracoes = 200
    ag.percentual_recombinacao = 100
    ag.percentual_mutacao = 20
    ag.limite_populacional = 15000
    ag.porcentagem_reducao_populacional = 50

    populacao_inicial = ag.gerar_populacao_inicial(ag.gerar_individuo_modelo(), ag.tamanho_inicial_populacao)

    #populacao_inicial[410] = exemplo_funcional

    ag.tecnica_selecao_elitista(populacao_inicial)

else:
    print("Erro ao selecionar o tipo do algoritmo")
    sys.exit()






