import os

menu = """
[D]eposito
[S]aque
[E]xtrato
[F]inalizar
[V]erificar Saldo

Digite sua opção:
"""

saldo = 0
LIMITE = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3
loop = True

while loop:
    op = input(menu)

    if op == 'f' or op == 'F':
        loop = False
        break

    if op == 'd' or op == 'D':

        os.system('cls' if os.name == 'nt' else 'clear')
        valor_dep = float(input("Add o valor de seu deposito: "))

        if valor_dep > 0:
            saldo += valor_dep
            extrato += f"Deposito ---> R$ {valor_dep:,.2f}\n".replace(",",".")
            continue

        else:

            print("Valor de depósito deve ser maior que zero!")
            continue

    elif op == 's' or op == 'S':
        os.system('cls' if os.name == 'nt' else 'clear')

        if num_saques < LIMITE_SAQUES:

            if saldo > 0:
                valor_saq = float(input("Add o valor que deseja sacar: "))

                if valor_saq <= 0:
                    print("Valor de saque deve ser maior que zero!")
                    continue

                if valor_saq > saldo:
                    print("Valor de saque excede o saldo disponível")
                    continue

                num_saques += 1
                saldo -= valor_saq
                extrato += f"Saque <--- R$ {valor_saq:,.2f}\n".replace(",",".")
                continue

            else:

                print("\n=== LIMITE DE SAQUES ATINGIDO ===\n")
                continue
    
    elif op == 'v' or op == 'V':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Seu saldo é: R$ {saldo:,.2f}')
        continue

    elif op == 'e' or op == 'E':

        if extrato != "":  
            os.system('cls' if os.name == 'nt' else 'clear')
            print(extrato)
            continue

        else:
            print("Seu extrato se encontra vazio!")

    else:
        print("Opcao invalida, tente novamente")