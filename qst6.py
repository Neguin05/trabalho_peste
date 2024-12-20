def alterna_letras(palavra):
    resultado = ''
    for i, letra in enumerate(palavra):
        if i % 2 == 0:
            resultado += letra.lower()
        else:
            resultado += letra.upper()
    return resultado
resultado = alterna_letras("Feliz Ano Novo ")
print(resultado)
