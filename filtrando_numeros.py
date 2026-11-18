def converter_valores(texto):
    valores_texto = texto.split()

    if not valores_texto:
        raise ValueError(
            "\nA entrada não pode estar vazia. Digite ao menos um número.\n"
        )

    try:
        return [int(valor) for valor in valores_texto]
    except ValueError:
        raise ValueError(
            "\nEntrada inválida. Digite somente números inteiros separados por espaço.\n"
        )


def eh_par(lista):
    nova_lista = []

    for valor in lista:
        if valor % 2 == 0:
            nova_lista.append(valor)

    return nova_lista


entrada = input("Digite os números separados por espaço: ")


try:
    lista_convertida = converter_valores(entrada)
    pares = eh_par(lista_convertida)
    print("\nNúmeros pares: ", *pares, "\n")
except ValueError as erro:
    print(erro)


# Faça como eu fiz: filtrando números pares

# Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário.

# Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().

# Exemplo de entrada:

# Digite os números separados por espaço: 1 2 3 4 5 6

# Saída esperada:

# Números pares: 2 4 6
