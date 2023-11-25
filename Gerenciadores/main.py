from BestFit import BestFit
from CircularFit import CircularFit
from FirstFit import FirstFit
from WorstFit import WorstFit


def encontrar_espacos_livres(lista):
    tamanho = 0
    espacos = []

    for item in lista:
        if item is None:
            tamanho += 1
        else:
            if tamanho > 0:
                espacos.append(str(tamanho))
                tamanho = 0

    if tamanho > 0:
        espacos.append(str(tamanho))

    return ' | '.join(espacos)

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
#    4 - Worst Fit             #
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
    espacos_contiguos = ""
    with open(nome_arquivo, 'r') as arquivo:
            if escolha == 1:
                bf = BestFit(mem_tam)
                espacos_contiguos += str("\n | " + encontrar_espacos_livres(bf.lista)) + " | \n"
                print('\nTamanho da memória: ','(', mem_tam, ')\n')
                for linha in arquivo:
                    if linha[0:2] == 'IN':
                        elemento_1 = linha.split(',')
                        elemento_2 = elemento_1[1].strip().strip(')')
                        bf.IN(linha[3], int(elemento_2))
                    else:bf.OUT(linha[4])
                    operacao = linha.strip()
                    espacos_contiguos += operacao + ":  | " + encontrar_espacos_livres(bf.lista) + " | \n"
                print(espacos_contiguos)
            elif escolha == 2:
                print('\nTamanho da memória: ','(', mem_tam, ')\n')
                cf = CircularFit(mem_tam)
                espacos_contiguos += str("\n | " + encontrar_espacos_livres(cf.lista)) + " | \n"
                for linha in arquivo:
                    if linha[0:2] == 'IN':
                        elemento_1 = linha.split(',')
                        elemento_2 = elemento_1[1].strip().strip(')')
                        cf.IN(linha[3], int(elemento_2))
                    else:cf.OUT(linha[4])
                    operacao = linha.replace('\n', ': ')
                    espacos_contiguos += operacao + " | " + encontrar_espacos_livres(cf.lista) + " | \n"
                print(espacos_contiguos)
            if escolha == 3:
                ff = FirstFit(mem_tam)
                espacos_contiguos += str("\n | " + encontrar_espacos_livres(ff.lista)) + " | \n"
                print('\nTamanho da memória: ','(', mem_tam, ')\n')
                for linha in arquivo:
                    if linha[0:2] == 'IN':
                        elemento_1 = linha.split(',')
                        elemento_2 = elemento_1[1].strip().strip(')')
                        ff.IN(linha[3], int(elemento_2))
                    else:ff.OUT(linha[4])
                    operacao = linha.replace('\n', ': ')
                    espacos_contiguos += operacao + " | " + encontrar_espacos_livres(ff.lista) + " | \n"
                print(espacos_contiguos)
            if escolha == 4:
                wf = WorstFit(mem_tam)
                espacos_contiguos += str("\n | " + encontrar_espacos_livres(wf.lista)) + " | \n"
                print('\nTamanho da memória: ','(', mem_tam, ')\n')
                for linha in arquivo:
                    if linha[0:2] == 'IN':
                        elemento_1 = linha.split(',')
                        elemento_2 = elemento_1[1].strip().strip(')')
                        wf.IN(linha[3], int(elemento_2))
                    else:wf.OUT(linha[4])
                    operacao = linha.replace('\n', ': ')
                    espacos_contiguos += operacao + " | " + encontrar_espacos_livres(wf.lista) + " | \n"
                print(espacos_contiguos)
if __name__ == "__main__":
    main()