cima = '1'
direita = '2'
baixo = '3'
esquerda = '4'


def allowed_path(coordenadas=['0', '0']):
    # mapa = [
    #     (*)
    #     [0, 1, 2],
    #     [3, 4, 5],
    #     [6, 7, 8](***),
    #     (**)
    # ]

    # if 0 -> cima(extra*), direita ou baixo
    # if 1 -> esquerda, direita ou baixo
    # if 2 -> esquerda ou baixo

    # if 3 -> direita, cima ou baixo
    # if 4 -> all directions
    # if 5 -> esquerda, cima ou baixo

    # if 6 -> direita baixo(extra**),ou cima
    # if 7 -> esquerda, direita ou cima
    # if 8 -> esquerda, direita(extra***) ou cima

    # mapa = [
    #         [[-1, 0]]
    #         [[0, 0], [0, 1], [0, 2]],
    #         [[1, 0], [1, 1], [1, 2]],
    #         [[2, 0], [2, 1], [2, 2], [2, 3]],
    #         [[3, 0]]
    # ]

    permitir = []

    if coordenadas == ['0', '0']:
        permitir = [cima, direita, baixo]  # + 1 pra cima
    elif coordenadas == ['0', '1']:
        permitir = [direita, baixo, esquerda]
    elif coordenadas == ['0', '2']:
        permitir = [baixo, esquerda]

    elif coordenadas == ['1', '0']:
        permitir = [cima, direita, baixo]
    elif coordenadas == ['1', '1']:
        permitir = [cima, direita, baixo, esquerda]
    elif coordenadas == ['1', '2']:
        permitir = [cima, baixo, esquerda]

    elif coordenadas == ['2', '0']:  # + 1 pra baixo
        permitir = [cima, direita, baixo]
    elif coordenadas == ['2', '1']:
        permitir = [cima, direita, esquerda]
    elif coordenadas == ['2', '2']:  # + 1 pra direita
        permitir = [cima, direita, esquerda]

    elif coordenadas == ['-1', '0']:
        permitir = [baixo]
    elif coordenadas == ['2', '3']:
        permitir = [esquerda]
    elif coordenadas == ['3', '0']:
        permitir = [cima]

    return permitir


def get_path(coordenadas, user_praia):
    COMMANDOS = ['1.', '2.', '3.', '4.']
    info_cima = (f'{user_praia}:\t\t '
                 f'0. Para Voltar\n\n')
    lixo_achado = False

    emoji_tronco = "🪵 (Tronco)"
    emoji_peixe = "🐟 (Peixe)"
    emoji_lixo = "🪨 (Lixo!!)"
    lixo_achado_texto = '(Digite "achei" para reportar)'

    label_cima = f'\t  {COMMANDOS[0]}\n'
    label_esquerda = f'{COMMANDOS[3]}\n'
    label_direita = f' {COMMANDOS[1]}\n'
    label_esquerda_direita = f'{COMMANDOS[3]}   \t \t{label_direita}'
    label_esquerda_direita_com_algo_na_direita = f'{
        COMMANDOS[3]}   \t \t{COMMANDOS[1]}(?)\n'
    label_baixo = f'\t  {COMMANDOS[2]} \n'

    seta_cima = ('\t^\n'
                 '\t|\n'
                 '\t|\t')

    seta_cima_sem_meio = ('\t^\n'
                          '\t|\n')

    seta_esquerda_com_meio = f'{COMMANDOS[3]}   \t|\n'

    seta_esquerda = ' < - -\n'
    seta_direita = '\t    - - > \n'
    seta_esquerda_direita = ' < - -     - - > \n'

    seta_baixo = ('\t|\n'
                  '\t|\n'
                  '\tv\n')

    algo_pra_cima = f'\t  {COMMANDOS[0]}(?)\n'
    algo_pra_baixo = f'\t  {COMMANDOS[2]}(?)\n'

    nada_cima = '\n\n\n'
    nada_baixo = '\n\n\n\n'

    # 0
    mapa_0 = (info_cima + algo_pra_cima
              + seta_cima + label_direita +
              seta_direita + seta_baixo + label_baixo)

    # 1
    mapa_1 = (info_cima + nada_cima +
              label_esquerda_direita + seta_esquerda_direita +
              seta_baixo + label_baixo)

    # 2
    mapa_2 = (info_cima + nada_cima +
              label_esquerda + seta_esquerda +
              seta_baixo + label_baixo)

    # 3
    mapa_3 = (info_cima + label_cima + seta_cima + label_direita +
              seta_direita + seta_baixo + label_baixo)

    # 4
    mapa_4 = (info_cima + label_cima + seta_cima_sem_meio +
              label_esquerda_direita + seta_esquerda_direita
              + seta_baixo + label_baixo)

    # 5
    mapa_5 = (info_cima + label_cima +
              seta_cima_sem_meio + seta_esquerda_com_meio +
              seta_esquerda +
              seta_baixo + label_baixo)

    # 6
    mapa_6 = (info_cima + label_cima + seta_cima + label_direita +
              seta_direita + seta_baixo + algo_pra_baixo)

    # 7
    mapa_7 = (info_cima + label_cima + seta_cima_sem_meio +
              label_esquerda_direita + seta_esquerda_direita + nada_baixo)

    # 8
    mapa_8 = (info_cima + label_cima + seta_cima_sem_meio +
              label_esquerda_direita_com_algo_na_direita +
              seta_esquerda_direita + nada_baixo)

    mapa_extra_cima_tronco = (info_cima +
                              f'   \t    {emoji_tronco}\n'
                              + nada_baixo + seta_baixo + label_baixo)

    mapa_extra_cima_peixe = (info_cima +
                             f'   \t    {emoji_peixe}\n'
                             + nada_baixo + seta_baixo + label_baixo)

    mapa_extra_cima_lixo = (info_cima +
                            f'   \t    {emoji_lixo}\n\n'
                            f'   \t{lixo_achado_texto}\n\n\n'
                            + seta_baixo + label_baixo)

    mapa_extra_direita_peixe = (info_cima + nada_cima +
                                f'{COMMANDOS[3]}   \t \t {emoji_peixe}\n'
                                ' < - -           \n'
                                + nada_baixo)

    mapa_extra_direita_tronco = (info_cima + nada_cima +
                                 f'{COMMANDOS[3]}   \t \t {emoji_tronco}\n'
                                 + seta_esquerda + nada_baixo)

    mapa_extra_direita_lixo = (info_cima + nada_cima +
                               f'{COMMANDOS[3]}   \t \t {emoji_lixo}\n'
                               f' < - -           {lixo_achado_texto}\n'
                               + nada_baixo)

    mapa_extra_baixo_tronco = (info_cima + label_cima +
                               seta_cima + nada_baixo
                               + f'   \t   {emoji_tronco}\n')

    mapa_extra_baixo_peixe = (info_cima + label_cima +
                              seta_cima + nada_baixo
                              + f'   \t   {emoji_peixe}\n')

    mapa_extra_baixo_lixo = (info_cima + label_cima + seta_cima + nada_baixo +
                             f'   \t   {emoji_lixo}\n{lixo_achado_texto}\n')

    if coordenadas == ['0', '0']:
        return_path = mapa_0
    elif coordenadas == ['0', '1']:
        return_path = mapa_1
    elif coordenadas == ['0', '2']:
        return_path = mapa_2

    elif coordenadas == ['1', '0']:
        return_path = mapa_3
    elif coordenadas == ['1', '1']:
        return_path = mapa_4
    elif coordenadas == ['1', '2']:
        return_path = mapa_5

    elif coordenadas == ['2', '0']:
        return_path = mapa_6
    elif coordenadas == ['2', '1']:
        return_path = mapa_7
    elif coordenadas == ['2', '2']:
        return_path = mapa_8

    elif coordenadas == ['-1', '0']:
        if user_praia == 'praia1':
            return_path = mapa_extra_cima_peixe
        elif user_praia == 'praia2':
            return_path = mapa_extra_cima_tronco
        else:
            return_path = mapa_extra_cima_lixo
            lixo_achado = True

    elif coordenadas == ['2', '3']:
        if user_praia == 'praia1':
            return_path = mapa_extra_direita_tronco
        elif user_praia == 'praia2':
            return_path = mapa_extra_direita_lixo
            lixo_achado = True
        else:
            return_path = mapa_extra_direita_peixe

    elif coordenadas == ['3', '0']:
        if user_praia == 'praia1':
            return_path = mapa_extra_baixo_lixo
            lixo_achado = True
        elif user_praia == 'praia2':
            return_path = mapa_extra_baixo_peixe
        else:
            return_path = mapa_extra_baixo_tronco

    else:
        return_path = 'NO_PATH'

    return return_path, lixo_achado
