# Prática de utilização da funções Name|Path|is_dir()|is_file()|stat()

import os

try:
    entradas = os.scandir("meu_diretorio")


    for obj in entradas:
        print(obj)
        print("Nome: ", obj.name)
        print("Caminho: ", obj.path)
        print("É diretório? ", obj.is_dir())
        print("É arquivo? ", obj.is_file())
        if obj.is_file():
            print("Tamanho: ", obj.stat().st_size, "B")
        print("=" * 35)

except FileNotFoundError as erro:
    print("O caminho não existe")
    print("Descrição: ", erro)
except NotADirectoryError as erro:
    print("O caminho não é de um diretório.")
    print("Descrição: ", erro)