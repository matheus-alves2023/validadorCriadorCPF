from primeiroDigito import *

def recebe_trata_user_input():

    cpf_valido = False
    while cpf_valido is False: 
        
        
        cpf = input("Digite um cpf: ")
        
        if len(cpf) == 11 or len(cpf) == 14:

            cpf_valido = True
            
        
        else:
            print("Você digitou uma sequência de caracteres inválida. Tente novamente.")
            continue
    return cpf


prepara_cpf_var = prepara_cpf(recebe_trata_user_input())
