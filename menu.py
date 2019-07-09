menu_dict = {
    "menu_inicial": {
        '1': 'Menu de opções, digite o número da opção desejada.',
        '2': 'Pesquisa de informações:\n',
        '3': '1 - Quantidade de funcionários',
        '4': '2 - Pesquisa de funcionários',
        '5': '3 - Listar média de salários',
        '6': '4 - Listar maior salário',
        '7': '5 - Ordenar lista de salários',
        '8': '6 - Sair do programa'
    },
    "menu_pesquisa": {
        '1': 'Menu de opções, digite o número da opção desejada.',
        '2': 'Pesquisar funcionários pelo:\n',
        '3': '1 - Nome',
        '4': '2 - Cargo',
        '5': '3 - Órgão',
        '6': '4 - Voltar'
    },
    "menu_ordenacoes": {
        '1': 'Menu de opções, digite o número da opção desejada.',
        '2': 'Ordenar lista usando:\n',
        '3': '1 - Bubble sort',
        '4': '2 - Selection sort',
        '5': '3 - Merge sort',
        '6': '4 - Voltar'
    }
}

# printa um menu de opções
def printMenu(menu: str):
    if (menu in menu_dict.keys()):
        for key in sorted(menu_dict[menu].keys()):
            print(menu_dict[menu][key])
