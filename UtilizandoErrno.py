import os
import errno

try:
    os.rmdir("meu_diretorio")
    print("Diretório removido")
except OSError as erro:
    print(erro.errno)
    if erro.errno == errno.ENOTEMPTY:
        print("O diretório não está vazio")
    else:
        print("descrição", erro)
    
print("término do programa.")