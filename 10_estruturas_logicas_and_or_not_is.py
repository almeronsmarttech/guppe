
ativo = True

email_verificado = False
logado = True
nome_usuario = "Nome do usuário"

if email_verificado and logado:
    print(f"Bem-vindo {nome_usuario}!")
elif logado and not email_verificado:
    print(f"Bem-vindo {nome_usuario}! Você precisa fazer a verificação do seu e-mail.")
elif not logado and email_verificado:
    print("Faça o login.")
else:
    print(f"Você precisa fazer o cadastro e a verificação do seu e-mail.")

"""
if not ativo:
    print("O usuário não está ativo.")

if logado:
    print("O usuário está logado.")
"""

num1 : int = int(input('Digite o primeiro número:'))
num2 : int = int(input('Digite o segundo número:'))

if num1 > num2:
    print("O primeiro número é maior que o segundo.")
elif num1 == num2:
    print("O primeiro número é igual ao segundo.")
else:
    print("O segundo número é maior que o primeiro.")


print(nome_usuario.isalnum())
numero_int = "12"
print(numero_int.isalnum())
numero_float = "12,15"
print(numero_float.isalnum())
print(numero_float.isnumeric())
print(numero_float.isdecimal())

numero_float1 = "12.15"
print(numero_float1.isalnum())
print(numero_float1.isnumeric())
print(numero_float1.isdecimal())
print(numero_float1.isalpha())