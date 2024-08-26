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



#Exercicio 2
# – Na área da eletrônica, em um circuito em série
# temos que a resistência equivalente (total) desse circuito é
# obtida mediante a soma de todas as resistências existentes
# (RE = r1 + r2 + ... + rn).
# – Faça uma aplicação que receba o valor de quatro
# resistências ligadas em série, calcule e mostre a
# resistência equivalente, a maior e a menor resistência. 

os.system('cls')
print("Exercicio 02")

resistencia1 = float(input("Digite o valor da resistência 1: "))
resistencia2 = float(input("Digite o valor da resistência 2: "))
resistencia3 = float(input("Digite o valor da resistência 3: "))
resistencia4 = float(input("Digite o valor da resistência 4: "))
resistencia_total = resistencia1 + resistencia2 + resistencia3 + resistencia4

if resistencia1 > resistencia2 and resistencia1 > resistencia3 and resistencia1 > resistencia4:
    maior = resistencia1
    print(f"Resistência total: {resistencia_total}\nMaior resistência: {maior}")
elif resistencia2 > resistencia1 and resistencia2 > resistencia3 and resistencia2 > resistencia4:
    maior = resistencia2
    print(f"Resistência total: {resistencia_total}\nMaior resistência: {maior}")
elif resistencia3 > resistencia1 and resistencia3 > resistencia2 and resistencia3 > resistencia4:
    maior = resistencia3
    print(f"Resistência total: {resistencia_total}\nMaior resistência: {maior}")
else:
    maior = resistencia4
    print(f"Resistência total: {resistencia_total}\nMaior resistência: {maior}")

if resistencia1 < resistencia2 and resistencia1 < resistencia3 and resistencia1 < resistencia4:
    menor = resistencia1
    print(f"Menor resistência: {menor}")
elif resistencia2 < resistencia1 and resistencia2 < resistencia3 and resistencia2 < resistencia4:
    menor = resistencia2
    print(f"Menor resistência: {menor}")
elif resistencia3 < resistencia1 and resistencia3 < resistencia2 and resistencia3 < resistencia4:
    menor = resistencia3
    print(f"Menor resistência: {menor}")
else:
    menor = resistencia4
    print(f"Menor resistência: {menor}")
