# lista = [7,4,6,8,2,4,8,9,0]



lista = [7,4,6,8,2,4,8,9,0]
soma = 0
for i in range(len(lista)):

    v = lista[i]
    
    c = 10 - i

    soma += c * v


print(soma)