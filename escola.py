from abc import ABC, abstractmethod 
#from <módulo> import <nome>
# módulo: nome do módulo ou pacote que você irá importar
#nome: nome da função, classe, variável o submódulo que deseja impportar
# import : React from react

'''Classe abstrata: classe que não pode ser instanciada diretamente
(não consigo criar) objetos diretamete nela. Definimos regras que devem ser obedecidas'''

#Curso no Geral
class Curso(ABC):
    def __init__(self,nome):
        self.nome = nome
        self.alunos = []
        
    def inscrever_alunos(self,aluno):
        self.alunos.append(aluno)
        print(f"Aluno (a) {aluno} inscrito no curso {self.nome}.")
     
    @abstractmethod   
    def info_curso(self):
        pass # é uma espécie de break da função
 #Curso Específico   
class CursoMatematica(Curso):
    def info_curso(self):
      print(f"Curso de {self.nome}: Foco em Álgebra e Geometria")
      
#Curso específico
class CursoHistoria(Curso):
    def info_curso(self):
        print(f"Curso de {self.nome}: foco em História Mundial e Cultura")
        
#testar
curso1 = CursoMatematica("Matemática")
curso2 = CursoHistoria("História")

curso1.inscrever_alunos("Beatriz")
curso1.inscrever_alunos("Sophia")
curso1.info_curso()

curso2.inscrever_alunos("Anna Luiza")
curso2.info_curso()