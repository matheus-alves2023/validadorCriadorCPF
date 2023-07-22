def prepara_cpf(cpf_input):

        cpf_sem_digitosEInteiro = []

        for v in cpf_input:
            if v not in "-.":
                v = int(v)
                cpf_sem_digitosEInteiro.append(v)

            if len(cpf_sem_digitosEInteiro) == 9 or len(cpf_sem_digitosEInteiro) == 10:
                break
        return cpf_sem_digitosEInteiro