class ContaBancaria(object):
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        self.consultar_saldo()

    def sacar(self, valor):
        self.saldo -= valor
        self.consultar_saldo()

    def consultar_saldo(self):
        print(self.saldo)


class ContaPoupanca(ContaBancaria):
    rentabilidade_total = 1.5

    def _consulta_rentabilidade(self):
        return self.rentabilidade_total

    def rentabilidade(self):
        rentabilidade = self._consulta_rentabilidade()

        if rentabilidade < 0.5:
            print('Fale com seu gerente.')
        else:
            print(rentabilidade)

    def depositar(self, valor):
        self.saldo += valor

        if self.saldo >= 1000:
            self.rentabilidade_total += 0.1
            print('Sua rentabilidade aumentou para:')
            self.rentabilidade()


conta_poupanca = ContaPoupanca()
conta_poupanca.rentabilidade()
conta_poupanca.depositar(2000)
conta_poupanca.sacar(50)
conta_poupanca.consultar_saldo()