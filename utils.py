import os

def limparTela():
    if (os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

def pausar():
    input('Aperte Enter para continuar...')
