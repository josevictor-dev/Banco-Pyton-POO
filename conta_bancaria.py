menu = """
╔══════════════════════════════════╗
║        💳 BANCO PYTHON S.A       ║
╠══════════════════════════════════╣
║  [l]  Login                      ║
║  [c]  Criar conta                ║
║                                  ║
║  [d]  Depositar                  ║
║  [s]  Sacar                      ║
║  [e]  Extrato                    ║
║                                  ║
║  [q]  Sair                       ║
╚══════════════════════════════════╝
"""


class ContaBancaria:
    def __init__(self, cpf, senha, titular, saldo):
        self.cpf = cpf
        self.titular = titular
        self.saldo = saldo
        self.extrato = []
        self.senha = senha



    def contaregistrada(self):
        return f'Titular: {self.titular} | Saldo: {self.saldo}'
    


    def depositar(self, valor):
        if valor > 0:
            self.extrato.append(f'+ {valor}')
            self.saldo += valor
            print(f'O valor de R$ {valor} foi depositado com sucesso')
        else:
            print('Valor abaixo do limite')



    def sacar(self, valor):
        if valor > self.saldo:
            print("Valor execedido")
            return
        else:
            self.extrato.append(f'- {valor}')
            self.saldo -= valor



    def extrato_conta(self):
        for i, percorrer in enumerate(self.extrato):
            print(f'{i}) {percorrer}') 


        
        
        
contas = { "123": ContaBancaria("123", "456", "José", 2000)
    
}
conta_atual = None        



while True:   
    print(menu)    
    opcoes = input ('Qual opção deseja selcionar? ').lower()


    if opcoes == "l":
        cpf = input("Digite seu CPF: ")
        senha = input("Digite sua senha: ")
        conta = contas.get(cpf)

        if conta and conta.senha == senha:
            conta_atual = conta
            print(f"{conta_atual.contaregistrada()}!")
            print(f"Bem-vindo, {conta_atual.titular}!")     
          
        else:
            print("CPF OU SENHA INVÁLIDA")


    if opcoes == 'd':
        
        if conta_atual:
            try:
                valor = float(input('Qual valor deseja depositar? '))
                conta_atual.depositar(valor)
            except:
               print('Digite um valor válido')
        else:
            print('Faça login primeiro')

    if opcoes == 's':
        if conta_atual:
            try:
                valor = float(input('Qual o valor deseja sacar? '))
                conta_atual.sacar(valor)
            except:
                print('Digite um valor válido')
        else:
            print('Faça login primeiro')

    if opcoes == 'e':
        if conta_atual:
            conta_atual.extrato_conta()
        else:
            print('Faça login primeiro')

    if opcoes == 'q':
        if conta_atual:
            conta_atual = None
            sair =input('Deseja sair do sistema? S/N').lower()
            if sair == 's':
                break
            else:
                continue
        else:
            print('Faça login primeiro')

    if opcoes == "c":
        nome = input("Qual seu nome? ")
        cpf = input("Informe seu CPF: ")
        senha = input("Crie uma senha: ")
        saldo = float(input("Qual o valor de depósito inicial: "))

        contas[cpf] = ContaBancaria(cpf, senha, nome, saldo)
        print("Conta criada com sucesso!")
