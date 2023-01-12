from random import randint
import os
print('## Verificador de CPF validos ##')


def menu():
    while True:
        print('1 - validar\n2 - gerar')
        op = input('Dígite o número da opção desejada: ')
        if op == '1':
            os.system('cls') if os.name == 'nt' else os.system('clear')
            cpf = str(input('Digite o CPF: '))
            cpf = cpf.replace('.', '')
            print(cpf)
            if verificador(cpf[:9]) == cpf[-2:]:
                print('VERDADEIRO!')
            else:
                print('FALSO!')
        elif op == '2':
            os.system('cls') if os.name == 'nt' else os.system('clear')
            gerado = gerar()
            verificado = verificador(gerado)
            print(gerado[0:3] + '.' + gerado[3:6] + '.' + gerado[6:9] + '-' + gerado[9:10] + verificado)
        else:
            print('Digite um número do menu.')
        input('Aperte qualquer tecla.')
        os.system('cls') if os.name == 'nt' else os.system('clear')


def gerar():
    nine_dig = ''
    for i in range(9):
        dig = randint(0, 9)
        nine_dig += str(dig)
    return nine_dig


def verificador(cpf):
    dig_verif = ''
    total = 0
    cont = 10
    for dig in cpf:
        sub_t = int(cont) * int(dig)
        cont -= 1
        total += sub_t
    total *= 10
    total %= 11
    total = total if total <= 9 else 0
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
    total = total if total <= 9 else 0
    dig_verif += str(total)
    return dig_verif


if __name__ == '__main__':
    menu()
