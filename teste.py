
# #746.824.890-70

# def recebe_trata_user_input():

#     cpf_valido = False
#     while cpf_valido is False: 
        
        
#         cpf = input("Digite um cpf: ")
        
#         if len(cpf) == 11 or len(cpf) == 14:

#             cpf_valido = True
            
        
#         else:
#             print("Você digitou uma sequência de caracteres inválida. Tente novamente.")
#             continue
#     return cpf
        

# def prepara_cpf(cpf_input):

#         cpf_sem_digitosEInteiro = []

#         for v in cpf_input:
#             if v not in "-.":
#                 v = int(v)
#                 cpf_sem_digitosEInteiro.append(v)

#             if len(cpf_sem_digitosEInteiro) == 9:
#                 break
#         return cpf_sem_digitosEInteiro
        

    
    
    
# def validador_primeirodigito(prepara_cpf):
#     soma = 0
    
#     for i in range(len(prepara_cpf)):

#         v = prepara_cpf[i]

#         c = 10 - i

#         soma += v * c

#     m = soma * 10

    
#     digito =  m % 11

#     novo_digito = digito if digito <= 9 else digito

#     return novo_digito

# def programa():

#     cpf_tratado = recebe_trata_user_input()
#     cpf_sem_digitos = prepara_cpf(cpf_tratado)
#     print(validador_primeirodigito(cpf_sem_digitos))
    
# programa()    





lista = [7, 0, 3, 7, 4, 4, 0, 5, 1, 5, 8]


print(*lista,type(lista))