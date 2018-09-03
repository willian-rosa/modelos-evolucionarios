from tkinter import *
  
class Application:
    def start(self, master=None):
        self.root = Tk()

        self.root.update_idletasks()
        self.root.update()


        self.primeiroContainer = Frame(self.root)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(self.root)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(self.root)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(self.root)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Estatística de Gerações do Algoritmo Genetico")
        self.titulo["font"] = ("Arial", "15", "bold")
        self.titulo.pack()

        self.geracao = self.generate_label("Geração atual: 0")
        self.tamanho_populacao = self.generate_label("Tamanho população: 0")
        self.pontuacao_melhor_individuo = self.generate_label("Pontuação melhor individuo: 0")
        self.melhor_fitness = self.generate_label("Melhor Fitness: 0")
        self.vida_individuo_melhor_finess = self.generate_label("Expectativa de vida do melhor idividuo: 0")

        self.estado = self.generate_label("Estado: inicial")

        self.refresh()

    def generate_label(self, text):
        variavel = Label(self.primeiroContainer, text=text)
        variavel["font"] = ("Arial", "10", "bold")
        variavel.pack()

        return variavel



    def refresh(self):
        self.root.update_idletasks()
        self.root.update()

    def show_status(self,
                    tamanho_populacao,
                    pontuacao_melhor_individuo,
                    melhor_fitness,
                    vida_individuo_melhor_finess):


        self.show_tamanho_populacao(tamanho_populacao)
        self.pontuacao_melhor_individuo.configure(text="Pontuação melhor individuo: " + str(pontuacao_melhor_individuo))
        self.melhor_fitness.configure(text="Melhor Fitness: " + str(melhor_fitness))
        self.vida_individuo_melhor_finess.configure(text="Expectativa de vida do melhor idividuo: " + str(vida_individuo_melhor_finess))
        self.refresh()


    def show_estado(self, text):
        self.estado.configure(text="Estado: " + text)
        self.refresh()

    def show_geracao(self, geracao_atual):
        self.geracao.configure(text="Geração atual: " + str(geracao_atual))
        self.refresh()

    def show_tamanho_populacao(self, tamanho_populacao):
        self.tamanho_populacao.configure(text="Tamanho população: " + str(tamanho_populacao))
        self.refresh()






