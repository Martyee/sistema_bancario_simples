import os
from datetime import datetime

# Constantes para mensagens
MENSAGENS = {
    "erro_valor": "❌ Valor deve ser maior que zero!",
    "erro_saldo": "❌ Saldo insuficiente para realizar saques!",
    "erro_opcao": "❌ Opção inválida, tente novamente",
    "sucesso_deposito": "✅ Depósito realizado com sucesso!",
    "sucesso_saque": "✅ Saque realizado com sucesso!",
    "erro_limite_saque": "❌ Valor excede o limite de R$ 500,00 por saque!",
    "erro_limite_diario": "❌ Limite de saques diários atingido!",
    "extrato_vazio": "📭 Seu extrato se encontra vazio!"
}

# Função para formatação de moeda brasileira
def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Função para limpeza de tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

menu = """
╔══════════════════════════════════════════════════════╗
║                    SISTEMA BANCÁRIO                  ║
╠══════════════════════════════════════════════════════╣
║  [D] - Depósito                                      ║
║  [S] - Saque                                         ║
║  [E] - Extrato                                       ║
║  [V] - Verificar Saldo                               ║
║  [F] - Finalizar                                     ║
╚══════════════════════════════════════════════════════╝

Digite sua opção: """

saldo = 0
LIMITE = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3
loop = True

while loop:
    op = input(menu).upper()  # Converter para maiúscula uma vez só

    if op == 'F':
        loop = False
        break

    elif op == 'D':
        limpar_tela()
        print("💰 OPERAÇÃO DE DEPÓSITO 💰\n")
        
        try:
            valor_dep = float(input("Digite o valor para depósito: R$ "))
            
            if valor_dep > 0:
                saldo += valor_dep
                timestamp = datetime.now().strftime("%d/%m %H:%M")
                extrato += f"[{timestamp}] Depósito ---> {formatar_moeda(valor_dep)}\n"
                
                print(f"\n{MENSAGENS['sucesso_deposito']}")
                print(f"💰 Valor depositado: {formatar_moeda(valor_dep)}")
                print(f"💰 Novo saldo: {formatar_moeda(saldo)}")
            else:
                print(f"\n{MENSAGENS['erro_valor']}")
                
        except ValueError:
            print("\n❌ Erro: Digite um valor numérico válido!")
        
        input("\nPressione ENTER para continuar...")

    elif op == 'S':
        limpar_tela()
        print("💸 OPERAÇÃO DE SAQUE 💸\n")
        
        # Verificar limites primeiro (mais eficiente)
        if num_saques >= LIMITE_SAQUES:
            print(f"\n{MENSAGENS['erro_limite_diario']}")
            input("\nPressione ENTER para continuar...")
            continue
            
        if saldo <= 0:
            print(f"\n{MENSAGENS['erro_saldo']}")
            input("\nPressione ENTER para continuar...")
            continue
        
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
        
        input("\nPressione ENTER para continuar...")
    
    elif op == 'V':
        limpar_tela()
        print("💳 CONSULTA DE SALDO 💳\n")
        
        print(f"💰 Saldo atual: {formatar_moeda(saldo)}")
        print(f"📊 Limite por saque: {formatar_moeda(LIMITE)}")
        print(f"🔄 Saques realizados hoje: {num_saques}/{LIMITE_SAQUES}")
        
        input("\nPressione ENTER para continuar...")

    elif op == 'E':
        limpar_tela()
        print("📋 EXTRATO BANCÁRIO 📋\n")
        
        if extrato != "":  
            print("📊 RESUMO:")
            print(f"💰 Saldo atual: {formatar_moeda(saldo)}")
            print(f"📋 Total de transações: {extrato.count('---') + extrato.count('<---')}\n")
            
            print("📝 HISTÓRICO DE TRANSAÇÕES:")
            print("=" * 60)
            print(extrato)
        else:
            print(f"{MENSAGENS['extrato_vazio']}")
        
        input("\nPressione ENTER para continuar...")

    else:
        print(f"\n{MENSAGENS['erro_opcao']}")
        input("\nPressione ENTER para continuar...")

# Mensagem de despedida
limpar_tela()
print("👋 Obrigado por usar nosso sistema bancário!")
print("🚀 Até a próxima!")