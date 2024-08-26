#Exercicio 04
#Dado um ano, retorne o século em que ele se encontra. O primeiro século abrange do ano 1 até e incluindo o ano 100, o segundo - do ano 101 até e incluindo o ano 200, etc.

x = int(input("Digite o ano: "))
if x % 100 == 0:
    seculo = x // 100
else:
    seculo = x // 100 + 1
print(f"O ano {x} está no século {seculo}")

# O código recebe um número inteiro e verifica se ele é divisível por 100, se for, 
# o século é o próprio número dividido por 100, se não for, o século é o número dividido 
# por 100 mais 1. Depois, imprime o ano e o século em que ele