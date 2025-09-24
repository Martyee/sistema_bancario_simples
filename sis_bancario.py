import os
from datetime import datetime

menu = """
╔══════════════════════════════════════════════════════╗
║                    SISTEMA BANCÁRIO                  ║
╠══════════════════════════════════════════════════════╣
║  [D] - Depósito                                      ║
║  [S] - Saque                                         ║
║  [E] - Extrato                                       ║
║  [V] - Verificar Saldo                               ║
║  [NC] - Nova Conta                                   ║
║  [NU] - Novo Usuario                                 ║
║  [LC] - Listar Contas                                ║
║  [F] - Finalizar                                     ║
╚══════════════════════════════════════════════════════╝

Digite sua opção: """

usuarios = {}

contas = []

# Variaveis
saldo = 0
LIMITE = 500
valor_saq = 0
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3
num_trans = 0
LIMITE_TRANS = 10
dia = datetime.now().strftime("%d")
LIMITE_DIARIO = False
loop = True
AGENCIA = "0001"
dia_block = dia

#Função cria usuário
def Cria_user():

    cpf_usuario = input("Informe o CPF: ").strip()
    if cpf_usuario in usuarios:
        print("Erro usuario já cadastrado!")
    
    else:
        nome_usuario = input("Informe seu nome: ")
        nasc_usuario = input("Informe sua data de nascimento dd-mm-aa : ")
        end_usuario = input("Informe seu endereco Logradouro - bairro - cidade/sigla estado: ")
    
    usuarios [cpf_usuario] = {
        "Nome": nome_usuario, 
        "Data de Nascimento": nasc_usuario, 
        "Endereco": end_usuario 
    }
    print(f"{usuarios[cpf_usuario]["Nome"]}, seu usuario foi cadastrado com sucesso!!!" )
    input("\nPressione ENTER para continuar...")   

#Função cria contas
def Cria_conta(contas):

    num_conta = len(contas)+1
    busca_cpf = input("Informe o numero de seu cpf: ")

    if busca_cpf in usuarios:
        print(f"Seja bem vindo {usuarios[busca_cpf]["Nome"]}")
        nova_conta = {
            "Agencia": AGENCIA, 
            "Numero Conta": num_conta, 
            "Usuario": usuarios[busca_cpf]["Nome"],
        }
        contas.append(nova_conta)

        print(f"Conta criada com sucesso! \n sua conta eh a de numero: {num_conta}")

    else:
        print("O CPF informado esta incorreto!, encerrando criação de contas")

    input("\nPressione ENTER para continuar...")   
    return contas

#Função lista contas
def Lista_contas(contas):
    if not contas:
        print("Nenhuma conta adicionada ate o momento!")
    else:
        for i, contas in enumerate(contas,1):
            print(f"CONTA {i}:")
            print(f" Usuário: {contas['Usuario']}")
            print(f" Agência: {contas['Agencia']}")
            print(f" Número da Conta: {contas['Numero Conta']}")
            print("-" * 40)

# Função formatação
def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Função bloqueia limite 
def bloqueia_limite(dia, trans):
    global LIMITE_DIARIO
    global dia_block
    if trans >= LIMITE_TRANS and dia == dia_block:
        dia_block = dia
        LIMITE_DIARIO = True

# Constantes mensagens
MENSAGENS = {
    "erro_valor": "❌ Valor deve ser maior que zero!",
    "erro_saldo": "❌ Saldo insuficiente para realizar saques!",
    "erro_opcao": "❌ Opção inválida, tente novamente",
    "sucesso_deposito": "✅ Depósito realizado com sucesso!",
    "sucesso_saque": "✅ Saque realizado com sucesso!",
    "erro_limite_saque": "❌ Valor excede o limite de R$ 500,00 por saque!",
    "erro_limite_diario": "❌ Limite de saques diários atingido!",
    "extrato_vazio": "📭 Seu extrato se encontra vazio!",
    "erro_limite_trans": f"Limite de transações do dia {dia_block} atingidas!"
}

# Função saldo
def Verifica_saldo(saldo, LIMITE, num_saques, LIMITE_SAQUES):
    limpar_tela()
    print("💳 CONSULTA DE SALDO 💳\n")
    
    print(f"💰 Saldo atual: {formatar_moeda(saldo)}")
    print(f"📊 Limite por saque: {formatar_moeda(LIMITE)}")
    print(f"🔄 Saques realizados hoje: {num_saques}/{LIMITE_SAQUES}")
    
    input("\nPressione ENTER para continuar...")

# Função depósito
def Deposito(saldo, valor, extrato, /):

    limpar_tela()
    print("💰 OPERAÇÃO DE DEPÓSITO 💰\n")

    if LIMITE_TRANS == True:
        print(f"={MENSAGENS['erro_limite_trans']}")
        input("\nPressione ENTER para continuar...")
        return saldo, extrato, num_trans

    else:

        try:
            valor_dep = float(input("Digite o valor para depósito: R$ "))
            
            if valor_dep > 0:
                saldo += valor_dep
                timestamp = datetime.now().strftime("%d/%m %H:%M")
                extrato += f"[{timestamp}] Depósito ---> {formatar_moeda(valor_dep)}\n"
                
                print(f"\n{MENSAGENS['sucesso_deposito']}")
                print(f"💰 Valor depositado: {formatar_moeda(valor_dep)}")
                print(f"💰 Novo saldo: {formatar_moeda(saldo)}")
                num_trans+=1

            else:
                print(f"\n{MENSAGENS['erro_valor']}")
                return saldo, extrato, num_trans
                
        except ValueError:
            print("\n❌ Erro: Digite um valor numérico válido!")
            return saldo, extrato, num_trans
        
    input("\nPressione ENTER para continuar...")
    return saldo, extrato, num_trans

# Função saque
def Saque(*, saldo,extrato, valor_saq, num_saques, LIMITE_SAQUES, LIMITE_TRANS):
    limpar_tela()

    print("💸 OPERAÇÃO DE SAQUE 💸\n")

    if LIMITE_TRANS == True:
        print(f"={MENSAGENS['erro_limite_trans']}")
        input("\nPressione ENTER para continuar...")
        return saldo, extrato, num_saques

    else:

        if num_saques >= LIMITE_SAQUES:
            print(f"\n{MENSAGENS['erro_limite_diario']}")
            input("\nPressione ENTER para continuar...")
            return saldo, extrato, num_saques
            
        if saldo <= 0:
            print(f"\n{MENSAGENS['erro_saldo']}")
            input("\nPressione ENTER para continuar...")
            return saldo, extrato, num_saques
        
        try:
            print(f"💰 Saldo disponível: {formatar_moeda(saldo)}")
            print(f"📊 Limite por saque: {formatar_moeda(LIMITE)}")
            print(f"🔄 Saques restantes hoje: {LIMITE_SAQUES - num_saques}\n")
            
            valor_saq = float(input("Digite o valor para saque: R$ "))
            
            if valor_saq <= 0:
                print(f"\n{MENSAGENS['erro_valor']}")
            elif valor_saq > saldo:
                print(f"\n{MENSAGENS['erro_saldo']}")
            elif valor_saq > LIMITE:
                print(f"\n{MENSAGENS['erro_limite_saque']}")
            else:
                num_saques += 1
                saldo -= valor_saq
                timestamp = datetime.now().strftime("%d/%m %H:%M")
                extrato += f"[{timestamp}] Saque <--- {formatar_moeda(valor_saq)}\n"
                
                print(f"\n{MENSAGENS['sucesso_saque']}")
                print(f"💸 Valor sacado: {formatar_moeda(valor_saq)}")
                print(f"💰 Saldo restante: {formatar_moeda(saldo)}")
                print(f"🔄 Saques restantes hoje: {LIMITE_SAQUES - num_saques}")
                
        except ValueError:
            print("\n❌ Erro: Digite um valor numérico válido!")
            return saldo, extrato, num_saques
    
    input("\nPressione ENTER para continuar...")
    return saldo, extrato, num_saques 

#Função extrato
def Mostra_extrato(saldo, /, *, extrato, num_trans):

    limpar_tela()

    print("📋 EXTRATO BANCÁRIO 📋\n")

    if extrato != "":  
        print("📊 RESUMO:")
        print(f"💰 Saldo atual: {formatar_moeda(saldo)}")
        print(f"📋 Total de transações: {num_trans}")
        
        print("📝 HISTÓRICO DE TRANSAÇÕES:")
        print("=" * 60)
        print(extrato)

    else:
        print(f"{MENSAGENS['extrato_vazio']}")
        input("\nPressione ENTER para continuar...")



# Função para limpeza de tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

while loop:
    op = input(menu).upper()

    bloqueia_limite(dia, num_trans)

    if op == 'F':
        loop = False
        break

    if op == 'D':
        saldo, extrato, num_trans = Deposito(saldo, extrato, LIMITE_TRANS, num_trans)
        continue

    elif op == 'S':
       saldo, extrato, num_saques = Saque(saldo=saldo, extrato=extrato, valor_saq=valor_saq, num_saques=num_saques, LIMITE_SAQUES=LIMITE_SAQUES, LIMITE_TRANS=LIMITE_TRANS)
       continue
    
    elif op == "NC":
        contas = Cria_conta(contas)
        continue
    elif op == "NU":
        Cria_user()
        continue

    elif op == 'LC':
        Lista_contas(contas)
        continue

    elif op == 'V':
        Verifica_saldo(saldo, LIMITE, num_saques, LIMITE_SAQUES)
        continue

    elif op == 'E':
        Mostra_extrato(saldo, extrato=extrato, num_trans=num_trans)
        continue

    else:
        print(f"\n{MENSAGENS['erro_opcao']}")
        input("\nPressione ENTER para continuar...")
        continue

# Mensagem de despedida
limpar_tela()
print("👋 Obrigado por usar nosso sistema bancário!")
print("🚀 Até a próxima!")