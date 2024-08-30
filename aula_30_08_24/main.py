import os

def limpar_tela():
    os.system('cls')

def mensaguem_inicial():
    print('Bem-vindo ao programa de soma de dois números\n')

def ler_numero():
    try:
        x = input('Digite um número: ')
        return int(x)
    except ValueError as erro:
        print('\n-------------------Digite um número válido--------------')
        print(f'vc digitou "{x}" entre com o nr correto\n\n')
        #print(erro, '\n')
        return ler_numero()

def soma(n1, n2):
    return n1 + n2

def exibir_intervalo(ini=0, fim=10, passo=1):
    for item in range(ini, fim, passo):
        print(item)


def main():
    # limpar_tela()
    # mensaguem_inicial()
    # n1 = ler_numero()
    # n2 = ler_numero()
    # print(f'\nA soma de {n1} + {n2} = {soma(n1, n2)}\n')
    print('Exibindo intervalos do 0 ao 10')
    exibir_intervalo(1, 10, 2)
    print('Exibindo intervalos do 0 ao 10 com passo 2')
    exibir_intervalo(fim = 11, passo = 2)

main()