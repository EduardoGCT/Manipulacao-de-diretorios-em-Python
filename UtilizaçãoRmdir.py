import os

try:
    os.rmdir("meu_diretorio")
    print("Diretório removido com sucesso!")
except PermissionError as erro:
    print("Sem permissão para remover diretório... Por favor verifique as permissões do arquivo e tente novamente.\n")
    print("Descrição", erro)
except FileNotFoundError as erro:
    print("Diretório inexistente... Só é possível remover caso o diretório já tenha sido criado.\n")
    print("Descrição", erro)
except OSError as erro:
    print("Outro erro...")
    print("O diretório está vazio?")
    print("Descrição", erro)

print("Término do programa..")