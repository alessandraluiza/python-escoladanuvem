listaFrutas = ["banana", "melância", "uva"]
print("Minha lista de frutas original: ", listaFrutas)
print(type(listaFrutas))
print(listaFrutas[0])
print(listaFrutas[1])
print(listaFrutas[2])
listaFrutas[0] = "abacaxi"
print("Minha lista de frutas alterada: ", listaFrutas)

tuplaFrutas = ("banana", "melancia", "uva")
print("A minha TUPLA de frutas é: ", tuplaFrutas)
print("O tipo de dados da minha TUPLA é: ", type(tuplaFrutas))
print(tuplaFrutas[0])
print(tuplaFrutas[1])
print(tuplaFrutas[2])

dicioFrutas = {
    "Ricardo": "Limão",
    "Gustavo": "Uva",
    "Taciara": "Tangerina",
    "Carol": "Manga"
}
print("Meu dicionário de Pessoas e frutas preferidas é: ", dicioFrutas)
print(type(dicioFrutas))
print("A Carol gosta de", dicioFrutas["Carol"])
print(dicioFrutas["Gustavo"])
print(dicioFrutas["Ricardo"])
print(dicioFrutas["Taciara"])