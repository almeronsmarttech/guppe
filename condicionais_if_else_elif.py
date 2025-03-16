
idade = 12

"""
Estrutura condicional em c:
if (idade < 18){
    printf("Menor de idade.");
}
else{
    printf("Maior de idade.");
}

Estrutura condicional em c#:
if (idade < 18){
    console.print("Menor de idade.");
}
else{
    console.print("Maior de idade.");
}
"""

if idade < 18:
    print("Menor de idade.")
    print(idade)
    # mais instruções
elif idade == 18:
    print("Está entrando na maioridade.")
else:
    print("Maior de idade.")
    print(idade)
    # mais instruções