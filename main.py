from utls import *
from ValidadorDigitos import *



def validador_cpf():

    capturar_tratar_input = input_user()
    excluir_digitos_e_tornar_outros_operaveis = remover_digitos_verificadores_e_converter_para_lista_de_inteiros(capturar_tratar_input)
    validaPrimeiroDigito = valida_digitos(excluir_digitos_e_tornar_outros_operaveis)
    validaSegundoDigito = valida_digitos(validaPrimeiroDigito)
    validaTodoCpf = valida_cpf_todo(capturar_tratar_input,validaSegundoDigito)
    print(validaTodoCpf)





def gerador_de_cpf_valido():

    cpf_gerado_random = gera_cpf_random()
    excluir_digitos_e_tornar_outros_operaveis = remover_digitos_verificadores_e_converter_para_lista_de_inteiros(cpf_gerado_random)
    validaPrimeiroDigito = valida_digitos(excluir_digitos_e_tornar_outros_operaveis)
    validaSegundoDigito = valida_digitos(validaPrimeiroDigito)
    cpf = cpf_gerado_validado(validaSegundoDigito)
    print(cpf)
    




# while True:

#     option = input("Gostaria de GerarCPF ou validar um cpf? [1/2] ")

#     if option == "1":

#         gerador_de_cpf_valido()
#     elif option == "2":

#         validador_cpf()
