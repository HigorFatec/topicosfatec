def receber_numeros():
    """Recebe números do usuário até que ele decida parar."""
    valores = []
    print("Digite os números que deseja armazenar. Digite 'sair' para finalizar.")

    while True:
        entrada = input("Digite um número (ou 'sair' para encerrar): ")

        if entrada.lower() == 'sair':
            break
        
        try:
            numero = float(entrada)
            valores.append(numero)
        except ValueError:
            print("Por favor, digite um número válido ou 'sair'.")

    return valores

def contar_pares(valores):
    """Retorna a quantidade de números pares."""
    return sum(1 for v in valores if v % 2 == 0)

def listar_impares(valores):
    """Retorna uma lista de números ímpares."""
    return [v for v in valores if v % 2 != 0]

def encontrar_maior(valores):
    """Retorna o maior número."""
    return max(valores) if valores else None

def encontrar_menor(valores):
    """Retorna o menor número."""
    return min(valores) if valores else None

def calcular_media(valores):
    """Retorna a média dos números."""
    return sum(valores) / len(valores) if valores else 0

def main():
    valores = receber_numeros()

    # Cálculos e resultados
    quantidade_pares = contar_pares(valores)
    impares = listar_impares(valores)
    maior = encontrar_maior(valores)
    menor = encontrar_menor(valores)
    media = calcular_media(valores)

    # Apresentação dos resultados
    print("\nResultados:")
    print(f"Quantidade de números pares: {quantidade_pares}")
    print(f"Números ímpares: {impares}")
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
    print(f"Média dos números: {media:.2f}")

if __name__ == "__main__":
    main()