class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome # atributo público
        self.__idade = idade # atributo privado
        
    def mostar_idade(self):
        print(f"Idade: {self.__idade}")
        
p = Pessoa("Anna Luiza", 18)
print(p.nome) #acesso público 
p.mostrar_idade() #acesso privado via método
        