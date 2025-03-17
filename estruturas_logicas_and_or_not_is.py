
ativo = True
logado = True
nome_usuario = "Nome do usuário"

if ativo and logado:
    print(f"Bem-vindo {nome_usuario}!")
else:
    print(f"Você precisa ativar a sua conta. Por favor, verifique o seu e-mail ou reenvie a verificação.")

if not ativo:
    print("O usuário não está ativo.")

if logado:
    print("O usuário está logado.")