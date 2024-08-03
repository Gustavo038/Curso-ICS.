class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R$ {valor:2} realizado. Novo saldo: R$ {self.saldo:2}')
        else:
            print('Valor de depósito deve ser positivo.')

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}')
        else:
            print('Saque inválido. Verifique o valor e seu saldo.')


class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo=0, taxa_rendimento=0.01):
        super().__init__(titular, saldo)  # Chama o construtor da classe base
        self.taxa_rendimento = taxa_rendimento

    def calcular_rendimento(self):
        rendimento = self.saldo * self.taxa_rendimento
        print(f'O rendimento da conta é: R$ {rendimento:.2f}')
        return rendimento


# Exemplo de uso
conta = ContaBancaria("João")
conta.depositar(100)
conta.sacar(50)

conta_poupanca = ContaPoupanca("Maria", 200, 0.05)
conta_poupanca.calcular_rendimento()
conta_poupanca.depositar(100)
conta_poupanca.sacar(50)

