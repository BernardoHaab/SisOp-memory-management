class BestFit:
    def __init__(self, tamanho_lista):
        self.lista = [None] * tamanho_lista

    def print_lista(self):
        print("{}".format(self.lista))

    def IN(self, elemento, tamanho):
        melhor_espaco = float('inf')
        posicao_inicial = -1
        passo =-1
        for i in range(len(self.lista)-1, 0, passo):
            # print("i: {}".format(i))
            if self.lista[i] is None:
                espaco_atual = 0
                j = i
                while j >= 0 and self.lista[j] is None:
                    # print("j: {}".format(j))
                    espaco_atual += 1
                    j -= 1
                # print("espaco_atual: {}".format(espaco_atual))
                if espaco_atual >= tamanho and espaco_atual < melhor_espaco:
                    melhor_espaco = espaco_atual
                    posicao_inicial = i

                # passo = espaco_atual

        # print("posicao_inicial: {}".format(posicao_inicial))
        if posicao_inicial == -1:
            print("IN({}, {}): Memory Overflow".format(elemento, tamanho))
        else:
            for i in range(posicao_inicial, posicao_inicial - tamanho, -1):
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
