from helpers import forca_opcao, limpar_tela
from sysfunctions import sys_dados, sys_doacao

nome_provisorio = "NOME PROVISORIO"
lista_menu_opcao = ['1', '2', '3', '0']
lista_praias = ["Maresias", "Juquehy", "Ubatuba"]

print(f"Seja bem-vindo a {nome_provisorio}!!!")
while True:
    caminho = forca_opcao("Por qual caminho você deseja seguir:\n" 
                            "1 - Simulação\n"
                            "2 - Dados capturados\n" 
                            "3 - Doação\n" 
                            "0 - Sair\n--> ", lista_menu_opcao, "Opção inválida! Digite apenas os números correspondentes ao caminho indicado")
    limpar_tela()
    if caminho == '1':
        #Johnny part  
        print("Bem-vindo ao sistema de escaneamento...!")
    elif caminho == '2':
        print(f"Bem-vindo ao banco de dados {nome_provisorio}, aqui você encontrará todos os tipos de dados " 
              "capturados pelos nossos sensores oceânicos!\n")
        sys_dados()
    elif caminho == '3':
        print(f"Bem-vindo a seção de doação {nome_provisorio}, aqui você pode fazer doações de quantias " 
              "de sua preferência para nos ajudar a manter os oceanos sempre monitorados e saudáveis!")
        sys_doacao()
    elif caminho == '0':
        break

