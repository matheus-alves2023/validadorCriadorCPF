
import re

def input_user():

    while True:

        cpf_user = input("Digite um cpf para validá-lo: ")
        cpf_user_trat = re.sub(r'\D','',cpf_user)

        if len(cpf_user_trat) == 11 and cpf_user_trat.isnumeric():
            break
            
        else:
            print("Você digitou um cpf com formato inválido. Tente novamente. ")

    return cpf_user_trat


def remover_digitos_verificadores_e_converter_para_lista_de_inteiros(cpf_user_trat):

    cpf_s_digitos_lista_iteravel = []
    
    for v in cpf_user_trat:

        v = int(v)
        cpf_s_digitos_lista_iteravel.append(v)

        if len(cpf_s_digitos_lista_iteravel) == 9 or len(cpf_s_digitos_lista_iteravel) == 10:
            break
    return cpf_s_digitos_lista_iteravel
 
       




def valida_cpf_todo(cpf_user_input, cpf_formado):

    cpf_formadoComp = ""

    for v in cpf_formado:

        cpf_formadoComp += str(v)

    
    if cpf_formadoComp == cpf_user_input:

        return "O CPF é válido."
    else:

        return "O CPF é inválido!"