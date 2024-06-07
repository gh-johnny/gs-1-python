from helpers import forca_opcao, limpar_tela
from sysfunctions import sys_dados, sys_doacao
from simulacao import tela_simulacao

nome_da_empresa = "Ocean Solution "
lista_menu_opcao = ['1', '2', '3', '0']
lista_praias = ["Maresias", "Juquehy", "Ubatuba"]

while True:
    print(f"Seja bem-vindo à {nome_da_empresa}!!!")
    caminho = forca_opcao("Por qual caminho você deseja seguir:\n"
                          "1 - Simulação\n"
                          "2 - Dados capturados\n"
                          "3 - Doação\n"
                          "0 - Sair\n--> ", lista_menu_opcao, "Opção inválida! Digite apenas os números correspondentes ao caminho indicado")
    limpar_tela()
    if caminho == '1':
        tela_simulacao()
    elif caminho == '2':
        print(f"Bem-vindo ao banco de dados {nome_da_empresa},\n aqui você encontrará todos os tipos de dados "
              "capturados pelos nossos sensores oceânicos!\n")
        sys_dados()
    elif caminho == '3':
        print(f"Bem-vindo a seção de doação {nome_da_empresa}, \naqui você pode fazer doações de quantias "
              "de sua preferência para nos ajudar a manter os oceanos sempre monitorados e saudáveis!\n")
        sys_doacao()
    elif caminho == '0':
        break
