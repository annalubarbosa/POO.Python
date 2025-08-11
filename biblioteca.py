class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

def main():
    #criar lista de livros disponiveis
    livros = [
        Livro("Dom Casmurro", "Machado de Assis"),
        Livro("Senhor dos Anéis", "J. R. R. Tolkien"),
        Livro("Harry Potter", "J. K. Rowling"),
        Livro("Frankeinsten", "Mary Shelley"),
        Livro("A menina que roubava livros", "Markus Zusak"),
        Livro("Assassinato no Expresso do Oriente", "Agatha Christie"),
        Livro("Fogo e sangue", "George RR Martin"),
        Livro("O Pequeno Príncipe","Antoine de Saint-Exupéry"),
        Livro("Jogos Vorazes", "Suzanne Collins"),
        Livro("Quem é Você, Alasca?", "John Green")

    ]
    #solicitar nome do usuário

    nome = input("Digite o seu nome: ")

    #exibir lista de livros disponíveis
    print("\n Livros disponíveis para empréstimo: ")
    for i, livro in enumerate (livros, start=1):
        print(f" {i}. {livro.titulo} - {livro.autor}") 

    #solicitar a escolha do livro pelo usuario

    while True:
        escolha = int(input("\n Digite o nº do livro que deseja pegar emprestado: "))
        if 1 <= escolha <= len(livros):
            livro_selecionado = livros[ escolha - 1]
            break
        else:
            print("Por favor, digite um número entre 1 e {len(livros)}.")

    print(f"\n Empréstimo confirmado!")
    print(f"{nome} pegou emprestado o livro '{livro_selecionado.titulo}' de {livro_selecionado.autor}.")

main()

