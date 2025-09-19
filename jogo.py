import random #random é um modulo útil em aplicações que requerem aleatoriedade

print("Bem-vindo ao jogo: ADIVINHE O NÚMERO!")
print("A regra é simples: Pensarei em um número e seu objetivo é advinha-lo.")
numero = random.randint(1, 10) #A função randint() aceita dois argumentos: o limite inferior e o limite superior do intervalo
isGuessRigth = False
while isGuessRigth != True:
    adivinha = input("Digite um número de 1 a 10: ")
    if int(adivinha) == numero:
        print("Você adivinhou {}. O número está correto! Você ganhou!".format(adivinha))
        isGuessRigth = True
    else:
        print("Você digitou {}. Desculpe, não é isso. Tente novamente.".format(adivinha))