
def allowed_path(coordinates=['0', '0']):
    # mapa = [
    #     [0, 1, 2],
    #     [3, 4, 5],
    #     [6, 7, 8],
    # ]

    # if 0 -> right or down
    # if 1 -> left, right or down
    # if 2 -> left or down

    # if 3 -> right, up or down
    # if 4 -> all directions
    # if 5 -> left, up or down

    # if 6 -> right or up
    # if 7 -> left, right or up
    # if 8 -> left or up

    allow = []

    if coordinates == ['0', '0']:
        allow = ['2', '3']
    elif coordinates == ['0', '1']:
        allow = ['2', '3', '4']
    elif coordinates == ['0', '2']:
        allow = ['3', '4']

    elif coordinates == ['1', '0']:
        allow = ['1', '2', '3']
    elif coordinates == ['1', '1']:
        allow = ['1', '2', '3', '4']
    elif coordinates == ['1', '2']:
        allow = ['1', '3', '4']

    elif coordinates == ['2', '0']:
        allow = ['1', '2']
    elif coordinates == ['2', '1']:
        allow = ['1', '2', '4']
    elif coordinates == ['2', '2']:
        allow = ['1', '4']

    return allow


def get_path(allow_list, user_praia):
    commands = [0, 1, 2, 3, 4]

    # 0
    map_0 = (f'{user_praia}:\t\t '
             f'{commands[0]}. Para Voltar\n\n'
             f'   \t    \n'
             '   \t \n'
             '   \t \n'
             f'     \t \t {commands[2]}.\n'
             '           - - > \n'
             '   \t|\n'
             '   \t|\n'
             '   \tv\n'
             f'   \t  {commands[3]}. '
             '\n')

    # 1
    map_1 = (f'{user_praia}:\t\t '
             f'{commands[0]}. Para Voltar\n\n'
             f'   \t    \n'
             '   \t \n'
             '   \t \n'
             f'{commands[4]}.   \t \t {commands[2]}.\n'
             ' < - -     - - > \n'
             '   \t|\n'
             '   \t|\n'
             '   \tv\n'
             f'   \t  {commands[3]}. '
             '\n')

    # 2
    map_2 = (f'{user_praia}:\t\t '
             f'   Para Voltar\n\n'
             f'   \t    \n'
             '   \t \n'
             '   \t \n'
             f'{commands[4]}.   \t \t   \n'
             ' < - -           \n'
             '   \t|\n'
             '   \t|\n'
             '   \tv\n'
             f'   \t  {commands[3]}. '
             '\n')

    # 3
    map_3 = (f'{user_praia}:\t\t '
             f'{commands[0]}. Para Voltar\n\n'
             f'   \t  {commands[1]}.\n'
             '   \t^\n'
             '   \t|\n'
             f'     \t|\t {commands[2]}.\n'
             '           - - > \n'
             '   \t|\n'
             '   \t|\n'
             '   \tv\n'
             f'   \t  {commands[3]}. '
             '\n')

    # 4
    map_4 = (f'{user_praia}:\t\t '
             f'{commands[0]}. Para Voltar\n\n'
             f'   \t  {commands[1]}.\n'
             '   \t^\n'
             '   \t|\n'
             f'{commands[4]}.   \t|\t {commands[2]}.\n'
             ' < - -     - - > \n'
             '   \t|\n'
             '   \t|\n'
             '   \tv\n'
             f'   \t  {commands[3]}. '
             '\n')

    # 5
    map_5 = (f'{user_praia}:\t\t '
             f'{commands[0]}. Para Voltar\n\n'
             f'   \t  {commands[1]}.\n'
             '   \t^\n'
             '   \t|\n'
             f'{commands[4]}.   \t|\t   \n'
             ' < - -           \n'
             '   \t|\n'
             '   \t|\n'
             '   \tv\n'
             f'   \t  {commands[3]}. '
             '\n')

    # 6
    map_6 = (f'{user_praia}:\t\t '
             f'{commands[0]}. Para Voltar\n\n'
             f'   \t  {commands[1]}.\n'
             '   \t^\n'
             '   \t|\n'
             f'     \t|\t {commands[2]}.\n'
             '           - - > \n'
             '   \t \n'
             '   \t \n'
             '   \t \n'
             f'   \t     '
             '\n')

    # 7
    map_7 = (f'{user_praia}:\t\t '
             f'{commands[0]}. Para Voltar\n\n'
             f'   \t  {commands[1]}.\n'
             '   \t^\n'
             '   \t|\n'
             f'{commands[4]}.   \t|\t {commands[2]}.\n'
             ' < - -     - - > \n'
             '   \t \n'
             '   \t \n'
             '   \t \n'
             f'   \t     '
             '\n')

    # 8
    map_8 = (f'{user_praia}:\t\t '
             f'{commands[0]}. Para Voltar\n\n'
             f'   \t  {commands[1]}.\n'
             '   \t^\n'
             '   \t|\n'
             f'{commands[4]}.   \t|\t   \n'
             ' < - -           \n'
             '   \t \n'
             '   \t \n'
             '   \t \n'
             f'   \t     '
             '\n')

    # left_detected_path = (f'{user_praia}:\t\t '
    #                       f'{commands[0]}. Para Voltar\n\n'
    #                       f'   \t  {commands[1]}.\n'
    #                       '   \t^\n'
    #                       '   \t|\n'
    #                       f'{commands[4]}.(?)   |\t {commands[2]}.\n'
    #                       ' < - -     - - > \n'
    #                       '   \t|\n'
    #                       '   \t|\n'
    #                       '   \tv\n'
    #                       f'   \t  {commands[3]}. ')
    #
    # no_left_with_something_path = (f'{user_praia}:\t\t '
    #                                f'{commands[0]}. Para Voltar\n\n'
    #                                f'   \t  {commands[1]}.\n'
    #                                '   \t^\n'
    #                                '   \t|\n'
    #                                f'{commands[4]}. \t|\t {
    #                                    commands[2]}.\n'
    #                                '🪨          - - > \n'
    #
    #
    #                                '   \t|\n'
    #                                '   \t|\n'
    #                                '   \tv\n'
    #                                f'   \t  {commands[3]}. '
    #                                '\n'
    #                                f'\n Digite [{commands[4]
    #                                              }.] para denunciar o lixo')

    if (len(allow_list) == 2 and allow_list[0] == '2'
            and allow_list[1] == '3'):
        return_path = map_0
    elif (len(allow_list) == 2 and allow_list[0] == '3'
          and allow_list[1] == '4'):
        return_path = map_2
    elif (len(allow_list) == 2 and allow_list[0] == '1'
          and allow_list[1] == '2'):
        return_path = map_6
    elif (len(allow_list) == 2 and allow_list[0] == '1'
          and allow_list[1] == '4'):
        return_path = map_8
    elif (len(allow_list) == 3 and allow_list[0] == '2'
          and allow_list[1] == '3' and allow_list[2] == '4'):
        return_path = map_1
    elif (len(allow_list) == 3 and allow_list[0] == '1'
          and allow_list[1] == '2' and allow_list[2] == '3'):
        return_path = map_3
    elif (len(allow_list) == 3 and allow_list[0] == '1'
          and allow_list[1] == '3' and allow_list[2] == '4'):
        return_path = map_5
    elif (len(allow_list) == 3 and allow_list[0] == '1'
          and allow_list[1] == '2' and allow_list[2] == '4'):
        return_path = map_7
    elif (allow_list[0] == '1' and allow_list[1] == '2'
          and allow_list[2] == '3' and allow_list[3] == '4'):
        return_path = map_4

    # elif coordinates == 'no_left_with_something':
    #     return_path = no_left_with_something_path
    # elif coordinates == 'left_detected_path':
    #     return_path = left_detected_path
    else:
        return_path = 'NO_PATH'
    print(allow_list)

    return return_path
