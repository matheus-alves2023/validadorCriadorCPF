
def valida_digitos(cpf_operavel):
    cpf_formado = cpf_operavel
    if len(cpf_operavel) == 9:

        soma_do_produto = 0
        for i in range(len(cpf_operavel)):
            v = cpf_operavel[i]
            c = 10 - i
            
            soma_do_produto += v * c

    elif len(cpf_operavel) == 10:

        soma_do_produto = 0
        for i in range(len(cpf_operavel)):

            v = cpf_operavel[i]
            c = 11 - i
            soma_do_produto += v * c

    digito = soma_do_produto * 10
    digito_formado = digito % 11
    digito_formado = digito_formado if digito_formado <= 9 else 0
    cpf_formado.append(digito_formado)

    return cpf_formado









