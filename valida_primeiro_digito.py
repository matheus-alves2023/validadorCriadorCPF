
def validador_primeirodigito(cpf_iteravel):
    soma = 0
    
    for i in range(len(cpf_iteravel)):

        v = cpf_iteravel[i]

        c = 10 - i

        soma += v * c

    m = soma * 10

    
    digito =  m % 11

    novo_digito = digito if digito <= 9 else digito

    return novo_digito
