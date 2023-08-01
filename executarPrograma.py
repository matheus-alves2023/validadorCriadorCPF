from main import *



while True:

    option = input("Gostaria de GerarCPF ou validar um cpf? [1/2] ")

    if option == "1":

        gerador_de_cpf_valido()
    elif option == "2":

        validador_cpf()
