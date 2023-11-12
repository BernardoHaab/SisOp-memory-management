from BestFit import BestFit
from CircularFit import CircularFit
from FirstFit import FirstFit
from WorstFit import WorstFit


def main():
    print('')
    print("TP2 Sisop - Trabalho sobre Gerenciamento de Memória")
    print('')
    escolha = None
    while escolha not in [1, 2, 3, 4]:
        try:
            escolha = int(input("""
################################
#    1 - Best Fit              #
#    2 - Circular Fit          #
#    3 - First Fit             #
#    4 - Wordt Fit             #
################################

Escolha a opção: """))
        except ValueError:
            print("Entrada inválida!")
            print('')
    mem_tam = int(input("Digite o tamanho da memória: "))
    if mem_tam & (mem_tam - 1) != 0:
        print("O tamanho da memória deve ser potência de 2!")
        return
    # Solicitar o nome do arquivo de texto
    nome_arquivo = input("Digite o nome do arquivo de texto: ")

    # Abrir o arquivo com o nome fornecido pelo usuário
    with open(nome_arquivo, 'r') as arquivo:
            if escolha == 1:
                bf = BestFit(mem_tam)
                print('\nTamanho da memória: ','(', mem_tam, ')\n')
                for linha in arquivo:
                    if linha[0:2] == 'IN':
                        elemento_1 = linha.split(',')
                        elemento_2 = elemento_1[1].strip().strip(')')
                        bf.IN(linha[3], int(elemento_2))
                    else:bf.OUT(linha[4])
            elif escolha == 2:
                print('\nTamanho da memória: ','(', mem_tam, ')\n')
                cf = CircularFit(mem_tam)
                for linha in arquivo:
                    if linha[0:2] == 'IN':
                        elemento_1 = linha.split(',')
                        elemento_2 = elemento_1[1].strip().strip(')')
                        cf.IN(linha[3], int(elemento_2))
                    else:cf.OUT(linha[4])
            if escolha == 3:
                ff = FirstFit(mem_tam)
                print('\nTamanho da memória: ','(', mem_tam, ')\n')
                for linha in arquivo:
                    if linha[0:2] == 'IN':
                        elemento_1 = linha.split(',')
                        elemento_2 = elemento_1[1].strip().strip(')')
                        ff.IN(linha[3], int(elemento_2))
                    else:ff.OUT(linha[4])
            if escolha == 4:
                ff = WorstFit(mem_tam)
                print('\nTamanho da memória: ','(', mem_tam, ')\n')
                for linha in arquivo:
                    if linha[0:2] == 'IN':
                        elemento_1 = linha.split(',')
                        elemento_2 = elemento_1[1].strip().strip(')')
                        ff.IN(linha[3], int(elemento_2))
                    else:ff.OUT(linha[4])
if __name__ == "__main__":
    main()