def num_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) +1):
        if numero % i == 0:
            return False
    return True

numeros_primos = []
for n in range(1, 251):
    if num_primo(n):
        numeros_primos.append(n)

print("Numeros primos entre 1 e 250:") 
print(numeros_primos)