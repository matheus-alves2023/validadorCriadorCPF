from utls import *
from ValidadorDigitos import *



def execucao():

    capturar_tratar_input = input_user()
    excluir_digitos_e_tornar_outros_operaveis = remover_digitos_verificadores_e_converter_para_lista_de_inteiros(capturar_tratar_input)
    validaPrimeiroDigito = valida_digitos(excluir_digitos_e_tornar_outros_operaveis)
    validaSegundoDigito = valida_digitos(validaPrimeiroDigito)
    validaTodoCpf = valida_cpf_todo(capturar_tratar_input,validaSegundoDigito)
    print(validaTodoCpf)


execucao()


