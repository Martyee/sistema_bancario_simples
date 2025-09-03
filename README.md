# 🏦 Sistema Bancário Simples

Um sistema bancário em Python com funcionalidades básicas e interface otimizada.

## ✨ **Funcionalidades Principais**

- **💰 Depósito**: Adicionar dinheiro à conta
- **💸 Saque**: Retirar dinheiro (com limites de segurança)
- **💳 Consulta de Saldo**: Ver saldo atual
- **📋 Extrato**: Histórico completo de transações
- **🚪 Sair**: Finalizar o sistema

## 🚀 **Como Executar**

### **1. Executar o Sistema**
```bash
python sis_bancario.py
```

### **2. Funcionalidades Disponíveis**
- **D** - Realizar depósito
- **S** - Realizar saque
- **E** - Visualizar extrato
- **V** - Verificar saldo
- **F** - Finalizar sistema

## 🎯 **Características do Sistema**

### **Limites de Segurança**
- **Limite por saque**: R$ 500,00
- **Limite diário**: 3 saques por dia
- **Validação**: Verificação de saldo antes de operações

### **Formatação e Interface**
- **Moeda brasileira**: Formatação R$ 1.234,56
- **Timestamps**: Data e hora em cada transação
- **Menu visual**: Interface com bordas e emojis
- **Feedback claro**: Mensagens de sucesso e erro

## 🔧 **Otimizações Implementadas**

### **1. Validação Robusta**
- ✅ Tratamento de erros para entradas inválidas
- ✅ Verificação de limites antes de operações
- ✅ Validação de valores negativos

### **2. Interface Melhorada**
- ✅ Menu com bordas e formatação profissional
- ✅ Emojis para melhor experiência visual
- ✅ Títulos claros para cada operação
- ✅ Mensagens de feedback informativas

### **3. Funcionalidades Avançadas**
- ✅ Formatação de moeda brasileira
- ✅ Timestamps nas transações
- ✅ Contagem de transações no extrato
- ✅ Informações detalhadas de saldo e limites

### **4. Estrutura de Código**
- ✅ Constantes centralizadas para mensagens
- ✅ Funções auxiliares reutilizáveis
- ✅ Lógica otimizada de verificação
- ✅ Tratamento de exceções

## 💰 **Exemplos de Uso**

### **Depósito**
```
💰 OPERAÇÃO DE DEPÓSITO 💰

Digite o valor para depósito: R$ 150,50

✅ Depósito realizado com sucesso!
💰 Valor depositado: R$ 150,50
💰 Novo saldo: R$ 150,50
```

### **Saque**
```
💸 OPERAÇÃO DE SAQUE 💸

💰 Saldo disponível: R$ 150,50
📊 Limite por saque: R$ 500,00
🔄 Saques restantes hoje: 3

Digite o valor para saque: R$ 50,00

✅ Saque realizado com sucesso!
💸 Valor sacado: R$ 50,00
💰 Saldo restante: R$ 100,50
🔄 Saques restantes hoje: 2
```

### **Extrato**
```
📋 EXTRATO BANCÁRIO 📋

📊 RESUMO:
💰 Saldo atual: R$ 100,50
📋 Total de transações: 2

📝 HISTÓRICO DE TRANSAÇÕES:
============================================================
[15/12 14:30] Depósito ---> R$ 150,50
[15/12 14:35] Saque <--- R$ 50,00
```

## 🎨 **Interface Visual**

O sistema apresenta uma interface moderna com:
- **Bordas e linhas** para organização visual
- **Emojis** para identificação rápida das operações
- **Cores e símbolos** para feedback visual
- **Layout limpo** e fácil de navegar

## 🔒 **Segurança e Validação**

### **Validações Implementadas**
- **Valores negativos**: Bloqueados automaticamente
- **Saldo insuficiente**: Verificado antes de saques
- **Limites de saque**: Respeitados rigorosamente
- **Entradas inválidas**: Tratadas com mensagens claras

### **Controles de Acesso**
- **Limite diário**: Máximo de 3 saques por dia
- **Limite por operação**: Máximo de R$ 500,00 por saque
- **Verificação de saldo**: Antes de qualquer saque

## 📱 **Compatibilidade**

- **Sistemas Operacionais**: Windows, Linux, macOS
- **Python**: Versão 3.6 ou superior
- **Terminais**: Suporte a caracteres especiais e emojis

## 🚀 **Próximas Melhorias Sugeridas**

### **Funcionalidades Futuras**
1. **Persistência de dados** em arquivo
2. **Múltiplas contas** com sistema de login
3. **Transferências** entre contas
4. **Relatórios** em diferentes formatos
5. **Interface gráfica** (GUI)

### **Melhorias Técnicas**
1. **Banco de dados** para armazenamento
2. **Sistema de logs** para auditoria
3. **Validação avançada** com regex
4. **Testes automatizados** mais abrangentes

## 🤝 **Contribuições**

Sinta-se à vontade para contribuir com melhorias:
1. **Fork** do repositório
2. **Criar branch** para sua feature
3. **Implementar** as melhorias
4. **Testar** o sistema
5. **Pull Request**

## 📄 **Licença**

Este projeto é de código aberto e está disponível sob a licença MIT.

---

**🎉 Sistema bancário otimizado e profissional! Execute `python sis_bancario.py` para experimentar!**
