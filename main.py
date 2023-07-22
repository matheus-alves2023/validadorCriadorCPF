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

    
    cpf_iteravel_digitado = prepara_cpf(cpf_digitado)
    cpf_iteravel_gerado = prepara_cpf(cpf_iteravel)
    print(cpf_iteravel_digitado)

program()