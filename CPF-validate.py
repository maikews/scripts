print('## Verificador de CPF validos ##')
#cpf = input('Dígite o CPF sem os 2 últimos dígitos e caracteres especiais: ')
cpf = '356465825'  # -31


def verificador():
    global cpf
    dig_verif = ''
    total = 0
    cont = 10
    for dig in cpf:
        sub_t = int(cont) * int(dig)
        cont -= 1
        total += sub_t
    total *= 10
    total %= 11
    dig_verif += str(total)

    ########################################
    cont = 11
    cpf_10 = cpf+str(total)
    total = 0
    for dig in cpf_10:
        sub_t = int(cont) * int(dig)
        cont -= 1
        total += sub_t
    total *= 10
    total %= 11
    dig_verif += str(total)
    return dig_verif

cod = str(verificador())
print(cod)
cpf_inteiro = cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:10] + cod
print(f'CPF: {cpf_inteiro}')