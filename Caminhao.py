import Veiculo
class Caminhao ( Veiculo.Veiculo ):
    def __init__(self, chassi, marca, modelo, ano, eixo, cabine, tipoDeFreio ):
        super().__init__(chassi, marca, modelo, ano, eixo, cabine, tipoDeFreio)
        super().set_tipo("Caminhão")
        self.eixo = eixo
        self.cabine = cabine
        self.tipoDeFreio = tipoDeFreio
        self.marcha = 1
        
    def ligar( self ):
      return self.marcha
        
    def desligar( self ):
       self.marcha = 1
        
""" Aqui comeca o teste (alterar para fazer teste) """
CaminhaoNovo = Caminhao('8885AZKG01Z12A33921312', 'Scania', 'S2000', '2023', 3, 'Dupla', 'Freio Hidraulico')
print(CaminhaoNovo.eixo)
print(CaminhaoNovo.cabine)
print(CaminhaoNovo.tipoDeFreio)
print(CaminhaoNovo.ligar())
print(CaminhaoNovo.desligar())
