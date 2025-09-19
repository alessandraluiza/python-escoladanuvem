# Variavel que armazena insulina humana
preproInsulin ="malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

print("Sequência pré-pró-insulina: " + preproInsulin)
print("Comprimento da sequência pré-pró-insulina: ", len(preproInsulin), "caracteres\n")


lsInsulina = "malwmrllpllallalwgpdpaaa"
bInsulina = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulina = "giveqcctsicslyqlenycn"
cInsulina = "rreaedlqvgqvelgggpgagslqplalegslqkr"
insulina = bInsulina + aInsulina

print("Sequência LS: ", lsInsulina, "tamanho:", len(lsInsulina), "caracteres\n")
print("Sequência A: ", lsInsulina, "tamanho:", len(aInsulina), "caracteres\n")
print("Sequência B: ", lsInsulina, "tamanho:", len(bInsulina), "caracteres\n")
print("Sequência C: ", lsInsulina, "tamanho:", len(cInsulina), "caracteres\n")
print("Sequência da insulina (B + A):")
print(insulina)
print("Comprimento da insulina: ", len(insulina), "caracteres.")