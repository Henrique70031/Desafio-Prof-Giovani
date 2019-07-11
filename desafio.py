from menu import rodarMenu;

###################################################

dicionarios = criarDicionario();
lista_desordenada = criarListaDesordenada(dicionarios);
contagemFuncionarios = contadorFuncionarios(dicionarios);
mediaSalarios, maiorSalario = pesquisaSalarios(dicionarios, contagemFuncionarios);

informacoes = {
    "num_funcionarios": contagemFuncionarios,
    "media_salarios": mediaSalarios,
    "maior_salario": maiorSalario,
    "dicionarios": dicionarios,
    "lista_desordenada": lista_desordenada
}

rodarMenu(informacoes);