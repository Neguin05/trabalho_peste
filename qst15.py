def maiuscula_inicial(palavra):
    if palavra:
        return palavra[0].upper() + palavra[1:]
    return palavra 
resultado1 = maiuscula_inicial("gatinho")
print(resultado1)