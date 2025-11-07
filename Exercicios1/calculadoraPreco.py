'''4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.'''

print("___Calculadora de Preço Total___")
print("Nome do produto: Cadeira Infantil \nPreço unitário: R$ 12.40 \nQuantidade: 3")

preco_unitario = 12.40
quantidade = 3
calculo = preco_unitario*quantidade


print(f"Total: {calculo}")