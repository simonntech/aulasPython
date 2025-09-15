class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, decremento):
        self.velocidade -= decremento

    def status(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} km/h'
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, potencia):
        super().__init__(marca, modelo, ano)
        self.potencia = potencia

    def acelerar(self, incremento):
        self.velocidade += incremento + self.potencia

class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo

    def status(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Tipo:{self.tipo}, Velocidade: {self.velocidade} km/h'
    
carro1 = Carro('Volwkswagen', 'Gol', 2014, 100)
bicicleta1= Bicicleta('Caloi', 'Bikezinha dos Cria', 1990, 'Barra Fote Zika')

carro1.acelerar(50)
bicicleta1.acelerar(20)

print('Status do Carro:')
print(carro1.status())

print('\nStatus da bike:')
print(bicicleta1.status())