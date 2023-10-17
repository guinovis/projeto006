import Veiculo
class onibus ( Veiculo.Veiculo ):
    def __init__(self, chassi, marca, modelo, ano, eixo, lugares):
        super().__init__(chassi, marca, modelo, ano, eixo, lugares)
        super().set_tipo("Onibus")
        self.eixo = eixo
        self.lugares = lugares
        self.marcha = 1
        
    def ligar( self ):
      return self.marcha
        
    def desligar( self ):
       self.marcha = 1

    def dirigir(self):
        return f"{self.marca} {self.modelo} está acelerando."
        
""" Aqui comeca o teste (alterar para fazer teste) """
CaminhaoNovo = Caminhao('8885AZKG01Z12A33921312', 'MercedesBens', '500 R Super Padron', '2023', 2, 42 lugares)
print(OnibusNovo.eixo)
print(OnibusNovo.lugares)
print(CaminhaoNovo.ligar())
print(CaminhaoNovo.desligar())
