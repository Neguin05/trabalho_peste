def compara_tamanho(palavra1, palavra2):
    if len(palavra1) > len(palavra2):
        return f"{palavra1}"
    elif len(palavra1) < len(palavra2):
        return f"{palavra2}"

resultado1 = compara_tamanho("Abacaxi", "banana")
print(resultado1)


