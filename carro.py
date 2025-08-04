class Carro:
    def __init__(self, ano, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.velocidade = 0
        self.som_ligado = False
        
    def buzinar(self):
        print(f"O {self.modelo} está buzinando: BEEP BEEP!")
    
    def acelerar(self,incremento=10):
        self.velocidade += incremento
        print(f"O {self.modelo} acelerou e está a {self.velocidade} km/h! OMG")
        
        
        
        
    def cavalinho_de_pau(self):
        if self.velocidade > 0:
            print(f"O {self.modelo} fez um cavalinho de pau a {self.velocidade} km/h! OMG")
        else:
            print(f" {self.modelo} está parado e não pode fazer um cavalnho de pau. ")
    
    
    def ligar_som(self):
        if not self.som_ligado:
            self.som_ligado = True
            print(f"O som do {self.modelo} está ligado")
        else:
            print(f"O som do {self.modelo} já está ligado")
            
    def desligar_som(self):
        if self.som_ligado:
            self.som_ligado = False
            print(f"O som do {self.modelo} está desligado")
        else:
            print(f"o som do {self.modelo} já está desligado.")
            
meu_carro = Carro(2008, "Monza", "Preto")

meu_carro.buzinar()
meu_carro.acelerar(90)
meu_carro.cavalinho_de_pau()
meu_carro.ligar_som()
meu_carro.ligar_som()
meu_carro.desligar_som()
meu_carro.desligar_som()
            
        
                