'''userReply = input("Você precisa enviar um pacote ? (Digite SIM ou NÃO)")
if userReply == "SIM":
    print("Podemos ajuda-lo a enviar este pacote.")
else:
    print("Por favor, volte quando você precisar enviar um pacote.")'''

usuario = input("Você deseja comprar selos, comprar envelope ou tirar uma cópia ? (Digite: Selo ou Envelope ou Copia)")
if usuario == "selo":
    print("Temos muitos designers para você escolher.")
elif usuario == "envelope":
    print("Temos vários tamanhos de envelopes para você escolher.")
elif usuario == "copia":
    copias = input("Quantas cópias deseja fazer ? (digite o número de cópias)")
    print("Aqui está {} cópias".format(copias))
else:
    print("Opção inválida. Retorne ao menu.")