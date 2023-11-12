class FirstFit:
    def __init__(self, tamanho_lista):
        self.lista = [None] * tamanho_lista
    def print_lista(self):
        print("{}".format(self.lista))
    def IN(self, elemento, tamanho):
        posicao_inicial = -1
        for i in range(len(self.lista)):
            if self.lista[i] is None:
                espaco_atual = 1
                j = i + 1
                while j < len(self.lista) and self.lista[j] is None:
                    espaco_atual += 1
                    j += 1
                if espaco_atual >= tamanho:
                    posicao_inicial = i
                    break
        if posicao_inicial == -1:
            print("IN({}, {}): Memory Overflow".format(elemento, tamanho))
        else:
            for i in range(posicao_inicial, posicao_inicial + tamanho):
                self.lista[i] = elemento
            print("IN({}, {}): {}".format(elemento, tamanho, self.lista))
    def OUT(self, elemento):
        if elemento not in self.lista:
            print("OUT({}): Elemento {} não está na lista.".format(elemento, elemento))
        else:
            for i in range(len(self.lista)):
                if self.lista[i] == elemento:
                    self.lista[i] = None
            print("OUT({}):   {}".format(elemento, self.lista))
