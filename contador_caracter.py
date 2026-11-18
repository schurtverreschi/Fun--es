def contar_caracteres(texto):
    return len(texto.strip())


palavra = input("Digite uma palavra: ")
caracteres = contar_caracteres(palavra)

print(f"Essa palavra tem {caracteres} caracteres.")


# Faça como eu fiz: contador de caracteres

# Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.

# Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.

# Exemplo de entrada:

# Digite uma palavra: tecnologia

# Saída esperada:

# Essa palavra tem 10 caracteres.
