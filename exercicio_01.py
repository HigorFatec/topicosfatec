#exercicio 1
import os
os.system('cls')
print("Exercicio 01")
produto = input("Digite o nome do produto: ")
valor = float(input("Digite o valor do produto: "))


if valor >= 50 and valor < 200:
    desconto = valor * 0.05
elif valor >= 200 and valor < 500:
    desconto = valor * 0.06
elif valor >= 500 and valor < 1000:
    desconto = valor * 0.07
elif valor >= 1000:
    desconto = valor * 0.08
elif valor < 0:
    print("Valor inválido")
    exit()
else:
    desconto = "Valor não tem desconto "

os.system('cls')
print(f"Produto {produto}\nValor sem desconto R${valor:.2f}\nCom desconto R${valor - desconto}")

