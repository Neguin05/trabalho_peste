def letra_do_meio(palavra):
    if len(palavra) % 2 == 1:
        meio = len(palavra) // 2
        return palavra[meio]
    else:
        return "A palavra deve ter tamanho ímpar"
resultado = letra_do_meio("ano")
print(resultado)
resultado2 = letra_do_meio("natal")
print(resultado2)