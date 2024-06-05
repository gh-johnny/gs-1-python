from helpers import forca_opcao, limpar_tela, print_de_opcoes
from simulacao_paths import pegar_mapa, caminho_permitido

y_axis = 0
x_axis = 0


def andar_mapa(direction):
    global y_axis
    global x_axis

    if direction == '1':
        y_axis -= 1
    elif direction == '3':
        y_axis += 1
    elif direction == '2':
        x_axis += 1
    elif direction == '4':
        x_axis -= 1

    updates_coordinates = [str(y_axis), str(x_axis)]
    return updates_coordinates


def tela_simulacao():
    simulacao_welcome_msg = ("Olá, seja bem vindo ao nosso sistema de "
                             "simulação de ajuda litorânea!!\n"
                             "Aqui, você pode nos ajudar a encontrar resíduos "
                             "espalhados pela praia de sua escolha.\n"
                             "Nossos escâners irão lhe ajudar a encontrar "
                             "resíduos na área, para que então "
                             "você possa reportar "
                             "para o nosso aplicativo.\n"
                             "Além de ajudar o meio ambiente "
                             "você ajuda a si mesmo "
                             "e outras pessoas atualizando-as sobre o "
                             "estado ambiental daquela região.")

    praias = ['Maresias', 'Juquehy', 'Ubatuba']
    print_de_praias = print_de_opcoes(praias)

    msg_escolha_praia = 'Escolha um praia para escanear!\n--> '
    msg_erro_escolha_praia = ('Por favor, escolha exatamente uma praia '
                              'da lista:\n'
                              f'{print_de_praias}')

    user_praia = forca_opcao(msg_escolha_praia, praias, msg_erro_escolha_praia)

    print(simulacao_welcome_msg)

    def each_step(allowed_command):
        comandos_disponiveis = print_de_opcoes(
            allowed_command, line_break=False)
        opcao_disp = f'As opções disponíveis são: 0, {comandos_disponiveis}\n'
        return opcao_disp

    qual_caminho_permitido = caminho_permitido()  # Começando em [0, 0]
    caminho_atual, lixo_achado = pegar_mapa(['0', '0'], user_praia)
    botao_de_voltar = '0'
    botao_de_reportar_lixo = 'achei'
    lixo_foi_achado = False

    while True:
        if lixo_achado:
            qual_caminho_permitido.append(botao_de_reportar_lixo)

        allowed_options = each_step(qual_caminho_permitido)
        perguntar_user_texto = 'Para onde gostaria de ir?\n--> '
        error_msg = 'Por favor...\n' + allowed_options + '\n' + caminho_atual

        limpar_tela()
        print(each_step(qual_caminho_permitido))
        print(caminho_atual)

        if lixo_foi_achado:
            user_direction = forca_opcao(perguntar_user_texto,
                                         [botao_de_reportar_lixo] +
                                         [botao_de_voltar] +
                                         qual_caminho_permitido,
                                         error_msg)
        else:
            user_direction = forca_opcao(perguntar_user_texto,
                                         [botao_de_voltar] +
                                         qual_caminho_permitido,
                                         error_msg)

        if user_direction == botao_de_voltar:  # Quando o usuário quiser sair
            break
        elif user_direction == botao_de_reportar_lixo:
            print('Lixo reportado para o aplicativo '
                  'e para as autoridades locais')
            return 1
            break

        pegar_coordenadas = andar_mapa(user_direction)
        qual_caminho_permitido = caminho_permitido(pegar_coordenadas)
        caminho_atual, lixo_achado = pegar_mapa(pegar_coordenadas, user_praia)
        lixo_foi_achado = lixo_achado
