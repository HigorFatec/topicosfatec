import os

def limpar_tela():
    os.system('cls')

def imc(peso, altura):
    return peso / altura ** 2

def ler_peso():
    try:
        x = input(f'Digite o seu peso (em kg): ')
        return float(x)
    except ValueError:
        print('Digite um peso válido')
        return ler_peso()

def ler_altura():
    try:
        y = input(f'Digite a sua altura (em metros): ')
        return float(y)
    except ValueError:
        print('Digite uma altura válida')
        return ler_altura()
    
def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return float(imc)


def main():
    while True:
        limpar_tela()
        peso = ler_peso()
        altura = ler_altura()
        print(f'\nSeu IMC é: {calcular_imc(peso, altura)}\n')
        a = input('\nDeseja calcular o IMC de outra pessoa? (s/n)')
        if a == 's':
            continue
        else:
            break

main()
        