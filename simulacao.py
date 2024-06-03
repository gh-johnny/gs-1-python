from helpers import forca_opcao, limpar_tela, print_de_opcoes
from simulacao_paths import get_path, allowed_path


simulacao_welcome_msg = ("Olá, seja bem vindo ao nosso sistema de "
                         "simulação de ajuda litorânea!!\n"
                         "Aqui, você pode nos ajudar a encontrar resíduos "
                         "espalhados pela praia de sua escolha.\n"
                         "Nossos escâners irão lhe ajudar a encontrar "
                         "lixos na área, para que então você possa reportar "
                         "para o nosso aplicativo.\n"
                         "Além de ajudar o meio ambiente "
                         "você ajuda a si mesmo "
                         "e outras pessoas atualizando-as sobre o "
                         "estado ambiental daquela região")


praias = ['praia1', 'praia2', 'praia3']
print_de_praias = print_de_opcoes(praias)

msg_escolha_praia = 'Escolha um praia para escanear!\n--> '
msg_erro_escolha_praia = ('Por favor, escolha exatamente uma praia '
                          'da lista:\n'
                          f'{print_de_praias}')

user_praia = forca_opcao(msg_escolha_praia, praias, msg_erro_escolha_praia)

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


def tela_simulacao(user_direction_command=-1):
    def each_step(allowed_command):
        comandos_disponiveis = print_de_opcoes(
            allowed_command, line_break=False)
        opcao_disp = f'As opções disponíveis são: {comandos_disponiveis}\n'
        return opcao_disp

    which_path_is_allowed = allowed_path()  # Começando em [0, 0]

    while True:
        allowed_options = each_step(which_path_is_allowed)
        current_path = get_path(which_path_is_allowed, user_praia)
        ask_user_text = 'Para onde gostaria de ir?\n--> '
        error_msg = 'Por favor...\n' + allowed_options + '\n' + current_path

        limpar_tela()
        print(each_step(which_path_is_allowed))
        print(current_path)
        user_direction = forca_opcao(ask_user_text, which_path_is_allowed,
                                     error_msg)
        which_path_is_allowed = allowed_path(andar_mapa(user_direction))


tela_simulacao()
