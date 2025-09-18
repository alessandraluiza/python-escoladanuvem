myString = "Isso é uma string"
print(myString)
print(type(myString))
print(myString + " do tipo de dado " + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("Qual é o seu nome ? ")
color = input("Qual sua cor favorita? ")
animal = input("Qual seu animal favorito ? ")
print("{}, você gosta da cor {} e do animal {}!".format(name, color, animal))