produtos = input("Digite os produtos separados por vírgula: ").split(",")
precos = input(
    "Digite os preços separados por vírgula(utilizar ponto para os centavos): "
).split(",")

largura_coluna = max(len(p.strip()) for p in produtos) + 2


if len(produtos) != len(precos):
    print("Erro: A quantidade de produtos e preços deve ser igual.")
else:
    print()
    for produto, preco in zip(produtos, precos):
        nome_alinhado = produto.strip().ljust(largura_coluna)
        valor = float(preco.strip())
        print(f"{nome_alinhado}| R$ {valor:.2f}")


# Faça como eu fiz: juntando listas de produtos

# Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas: uma contendo os nomes dos produtos e outras com seus respectivos preços. Para facilitar a organização, ela precisa combinar essas listas de forma que cada produto seja associado ao seu preço.

# Crie um programa que junte as listas e exiba o resultado no formato produto: preço

# Exemplo de entrada:

# Digite os produtos separados por vírgula: maçã, banana, pera
# Digite os preços separados por vírgula: 2.5, 1.2, 3.0

# Saída esperada:

# maçã: 2.5
# banana: 1.2
# pera: 3.0
