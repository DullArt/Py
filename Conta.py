class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo. Local da memoria{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do Titular {}".format(self.saldo,self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.pode_sacar(valor)):
            self.saldo -= valor
        else:
            print("O valor, {},passou do limite {}".format(valor))

    def transfere(self, valor, destino):
        self.sacar(valor)
        destino.deposita(valor)

    #gets e sets

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular


    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    #static
    @staticmethod
    def codigo_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}
