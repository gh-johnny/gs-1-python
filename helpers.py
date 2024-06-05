def limpar_tela(linhas=20):
    for i in range(linhas):
        print("\n")
    return


def meu_in(lista, buscar):
    for i in range(len(lista)):
        elem = lista[i]
        if elem == buscar:
            return True
    return False


def meu_index(lista, buscar):
    for i in range(len(lista)):
        elem = lista[i]
        if elem == buscar:
            return i
    return False


def forca_opcao(msg, lista, msg_erro):
    opcao = input(msg)
    while not meu_in(lista, opcao):
        limpar_tela()
        print(msg_erro)
        opcao = input(msg)
    return opcao


def verifica_numero(msg, msg_erro):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    return int(num)


def print_de_opcoes(lista, line_break=True):
    output = ''
    for i in range(len(lista)):
        if line_break:
            output += f'- {lista[i]}\n'
        else:
            prefix = ''
            if i > 0:
                prefix = ', '
            output += f'{prefix}{lista[i]}'
    if line_break:
        print(output)
    return output
