def prepara_cpf(cpf_input):

        cpf_sem_digitosEInteiro = []

        for v in cpf_input:
            if v not in "-.":
                v = int(v)
                cpf_sem_digitosEInteiro.append(v)

            if len(cpf_sem_digitosEInteiro) == 9 or len(cpf_sem_digitosEInteiro) == 10:
                break
        return cpf_sem_digitosEInteiro


def transformar_cpf_string(cpf_iteravel):
        cpf_gerado = ''
        for v in cpf_iteravel:
          cpf_gerado += str(v)
        return cpf_gerado

def valida_cpf_todo(cpfdigitado,cpfgerado):
     
     if cpfdigitado == cpfgerado:
          return "O cpf digitado é válido."
     
     else:
          return "O cpf digitado não é válido!"
    
