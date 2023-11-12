class CircularFit:
    def __init__(self, tamanho_lista):
        self.lista = [None] * tamanho_lista
        self.posicao_atual = 0
    
    def encontrar_espaco_disponivel(self, tamanho):
        segmento_atual = 0
        inicio_atual = -1
        for i in range(self.posicao_atual, self.posicao_atual + len(self.lista)):
            if self.lista[i % len(self.lista)] is None:
                if segmento_atual == 0:
                    inicio_atual = i % len(self.lista)
                segmento_atual += 1
                if segmento_atual >= tamanho:
                    return inicio_atual
            else:
                segmento_atual = 0
        if len(self.lista) - self.posicao_atual + inicio_atual >= tamanho:
            return inicio_atual
        if self.posicao_atual >= tamanho:
            return 0
        return None

    def IN(self, elemento, tamanho):
        espaco_disponivel = self.encontrar_espaco_disponivel(tamanho)
        if espaco_disponivel is None:
            print("IN({}, {}): Memory Overflow".format(elemento, tamanho))
        else:
            for i in range(espaco_disponivel, espaco_disponivel + tamanho):
                if self.lista[i % len(self.lista)] is not None:
                    print("IN({}, {}): Memory Overflow".format(elemento, tamanho))
                    return
            for i in range(espaco_disponivel, espaco_disponivel + tamanho):
                self.lista[i % len(self.lista)] = elemento
            self.posicao_atual = (espaco_disponivel + tamanho) % len(self.lista)
            print("IN({}, {}): {}".format(elemento, tamanho, self.lista))

    def OUT(self, elemento):
        if elemento not in self.lista:
            print("OUT({}): Elemento {} não está na lista.".format(elemento, elemento))
        else:
            self.posicao_atual = self.lista.index(elemento)
            for i in range(len(self.lista)):
                if self.lista[i] == elemento:
                    self.lista[i] = None
            print("OUT({}):   {}".format(elemento, self.lista))
