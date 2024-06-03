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

i = 0
j = 0


def andar_mapa(direction):
    # mapa = [
    #     [0, 0], [0, 1], [0, 2],
    #     [1, 0], [1, 1], [1, 2],
    #     [2, 0], [2, 1], [2, 2],
    # ]

    global i
    global j

    if direction == '1':
        i -= 1
    elif direction == '3':
        i += 1
    elif direction == '2':
        j += 1
    elif direction == '4':
        j -= 1

    return_result = [str(i), str(j)]

    print(return_result)
    return return_result


def tela_simulacao(user_direction_command=-1):
    def each_step(allowed_command):
        comandos_disponiveis = print_de_opcoes(
            allowed_command, line_break=False)
        opcao_disp = f'As opções disponíveis são: {comandos_disponiveis}\n'
        return opcao_disp

    which_path_is_allowed = allowed_path()  # Começando em [0, 0]

    while True:
        limpar_tela()
        allowed_options = each_step(which_path_is_allowed)
        print(get_path(which_path_is_allowed, user_praia))
        user_direction = forca_opcao(
            'Para onde gostaria de ir?\n--> ', which_path_is_allowed,
            'Por favor\n' + allowed_options)
        which_path_is_allowed = allowed_path(andar_mapa(user_direction))


tela_simulacao()
