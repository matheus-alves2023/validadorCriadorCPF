from cp_utils import *
from valida_primeiro_digito import *
from valida_segundo_digito import *


cpf_digitado = []


def recebe_trata_user_input():

    cpf_valido = False
    while cpf_valido is False: 
        
        
        cpf = input("Digite um cpf: ")
        
        if len(cpf) == 11 or len(cpf) == 14:

            cpf_valido = True
            
        
        else:
            print("Você digitou uma sequência de caracteres inválida. Tente novamente.")
            continue

    cpf_digitado.append(cpf)
    return cpf


def program():

    trat_inicial_cpf = recebe_trata_user_input()
    cpf_iteravel = prepara_cpf(trat_inicial_cpf)
    primeiro_digito = validador_primeirodigito(cpf_iteravel)
    cpf_iteravel.append(primeiro_digito)
    segundo_digito = validador_segundo_digito(cpf_iteravel)
    cpf_iteravel.append(segundo_digito)
    cpf_gerado = transformar_cpf_string(cpf_iteravel)
    cpf_digitado_str = transformar_cpf_string(cpf_digitado)

    print(valida_cpf_todo(cpf_digitado_str,cpf_gerado)) 
    

program()




# 77689062768,
# 00045024936,
# 01182101062,
# 21316016897,
# 26616776824,
# 72002557853,
# 90678117934,
# 82272182100,
# 82272387187,
# 82271577187