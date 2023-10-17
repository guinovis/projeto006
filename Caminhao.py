import Veiculo
class Caminhao ( Veiculo.Veiculo ):
    def __init__(self, chassi, marca, modelo, ano, eixo, cabine, tipoDeFreio ):
        super().__init__(chassi, marca, modelo, ano, eixo, cabine, tipoDeFreio)
        super().set_tipo("Caminhão")
        self.eixo = eixo
        self.cabine = cabine
        self.tipoDeFreio = tipoDeFreio
    def ligar( self ):
      pass 
    def desligar( self ):
      pass
""" Aqui comeca o teste (alterar para fazer teste) """
Caminhao = Caminhao('8885AZKG01Z12A33921312', 'JAC', 'J3', '2022', 2.0, 'HATCH')
print(CarroNovo.get_tipo())
print(CarroNovo.potencia)
print(CarroNovo.tipoCarro)
print(CarroNovo.ligar())
