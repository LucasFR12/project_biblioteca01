class Livro:

    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nAno: {self.ano}"


class Biblioteca:

    def __init__(self):
        self.livros = []
         
    def adicionar_livro(self, livro):
        if not self.livros:
            self.livros.append(livro)
            print(f"Livro '{livro.titulo}' adicionado com sucesso.")
        else:
            for x in self.livros:
                if x.titulo.lower() == livro.titulo.lower():
                    print(f"'{livro.titulo}' já existe na biblioteca.")
                    return
            self.livros.append(livro)
            print(f"Livro '{livro.titulo}' adicionado com sucesso.")

    def remover_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                self.livros.remove(livro)
                print(f"'{livro.titulo}' removido com sucesso.")
                return
        print(f"Livro '{titulo}' não encontrado.")

    def procurar_livro(self, titulo_livro):
        for livro in self.livros:
            if livro.titulo.lower() == titulo_livro.lower():
                print(f"Livro encontrado:\n{livro}")
                return
        print(f"Livro '{titulo_livro}' não encontrado.")

    def lista_livros(self):
        if not self.livros:
            print("Biblioteca vazia.")
        else:
            print("Lista de livros:\n")
            for livro in self.livros:
                print(f"{livro}\n")