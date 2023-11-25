class BestFit:
    def __init__(self, tamanho_lista):
        self.lista = [None] * tamanho_lista

    def print_lista(self):
        print("{}".format(self.lista))

    def IN(self, elemento, tamanho):
        melhor_espaco = float('inf')
        posicao_inicial = -1
        passo =-1
        espacos_livres = 0
        for i in range(len(self.lista)-1, -1, passo):
            if self.lista[i] is None:
                espacos_livres = espacos_livres + 1
            else:
              if espacos_livres >= tamanho and espacos_livres <= melhor_espaco:
                melhor_espaco = espacos_livres
                posicao_inicial = i + 1
              espacos_livres = 0
        if espacos_livres >= tamanho and espacos_livres <= melhor_espaco:
          posicao_inicial = 0
        if posicao_inicial == -1:
            print("IN({}, {}): Memory Overflow".format(elemento, tamanho))
        else:
            for i in range(posicao_inicial, posicao_inicial + tamanho, 1):
                self.lista[i] = elemento
            print("IN({}, {}): {}".format(elemento, tamanho, self.lista))

    def OUT(self, elemento):
        if elemento not in self.lista:
            print("OUT({}): Elemento {} não está na lista".format(elemento, elemento))
        else:
            for i in range(len(self.lista)):
                if self.lista[i] == elemento:
                    self.lista[i] = None
            print("OUT({}):   {}".format(elemento, self.lista))
