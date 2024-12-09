from library import Livro, Biblioteca
import os
from time import sleep

b1 = Biblioteca()
while True:
    os.system('cls')
    print("=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=")
    print("1 - Adicionar Livro.")
    print("2 - Remover Livro.")
    print("3 - Procurar Livro.")
    print("4 - Lista de Livros.")
    print("0 - Sair.")
    print("=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=")
    menu = ['0', '1', '2', '3', '4']
    while True:
        op = input("Digite a opção desejada: ")
        if op in menu:
            break
        else:
            print("Valor inválido!")
    print("=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=")
    os.system('cls')
    if '0' in op:
        print("Saindo...")
        sleep(1.5)
        os.system('cls')
        break
    if '1' in op:
        titulo = input("Informe o Título do Livro: ")
        autor = input("Informe o nome do Autor do Livro: ")
        try:
            ano = int(input("Informe o Ano do Livro: "))
            livro = Livro(titulo, autor, ano)
            b1.adicionar_livro(livro)
        except ValueError:
            print("Ano inválido! Por favor, insira um número.")
        sleep(1.5)
    if '2' in op:
        titulo = input("Informe o título do livro que deseja remover: ")
        b1.remover_livro(titulo)
        sleep(1.5)
    if '3' in op:
        titulo = input("Informe o título do livro que deseja acessar: ")
        b1.procurar_livro(titulo)
        input("\nPressione 'Enter' para retornar ao menu principal...")
    if '4' in op:
        b1.lista_livros()
        input("Pressione 'Enter' para retornar ao menu principal...")
