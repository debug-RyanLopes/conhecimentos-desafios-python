class ContaBancaria:
    def __init__(self, numeroDaConta, nomeTitular):
        self.numeroDaConta = numeroDaConta
        self.nomeTitular = nomeTitular
        self.saldo = 0

    def depositar(self, valorDoDeposito):
        self.saldo += valorDoDeposito
        return (
            f"Depósito no valor de: R${valorDoDeposito} realizado com sucesso no nome de: Sr(a){self.nomeTitular}, na conta: {self.numeroDaConta} ! \n"
            f"O Saldo atual da sua conta é de: R${self.saldo} "
            )
        

    def sacar(self, valorDoSaque):
        if valorDoSaque > self.saldo:
            print(f"Saque no valor de {valorDoSaque} foi NEGADO: SALDO INSUFICIENTE")
        else:
            self.saldo -= valorDoSaque
            return f"Saque no valor de: R${valorDoSaque} realizado com sucesso, Sr(a){self.nomeTitular}, na conta: {self.numeroDaConta} ! o Saldo atual da sua conta é de: R${self.saldo} "
    

teste = ContaBancaria(12345, "Ryan Lopes")
print(teste.depositar(200))
