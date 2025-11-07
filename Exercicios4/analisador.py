'''4 - Criar um código que serve para analisar números digitados pelo usuário, 
classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.'''

quantidade_pares = 0
quantidade_impares = 0

while True:
    numero = input("Digite um número inteiro (ou 'sair' para encerrar): ")
    if numero.lower() == 'sair':
        break
    #numero.isdigit(): verifica se é um número positivo.
    #numero.startswith('-') and numero[1:].isdigit(): verifica se é um número negativo.
    if not numero.isdigit() and not (numero.startswith('-') and numero[1:].isdigit()):
        print("Por favor, digite um número inteiro válido.")
        continue
    numero = int(numero)
    if numero % 2 == 0:
        print(f"{numero} é PAR.")
        quantidade_pares += 1
    else:
        print(f"{numero} é ÍMPAR.")
        quantidade_impares += 1

print("\nResultado:")
print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")

