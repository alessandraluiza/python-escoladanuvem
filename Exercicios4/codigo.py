'''3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.'''

senha = input("Digite uma senha alfanumerica: ")
tamanho_senha = len(senha) >= 8
numero_senha = any(s.isdigit() for s in senha)
if tamanho_senha and numero_senha:
    print("Senha válida")
else:
    print("Senha inválida.")