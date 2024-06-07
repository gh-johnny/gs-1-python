# GS - Computational Thinking With Python

## Integrantes 👋
<ul>
    <li>João Marcelo Furtado Romero (RM555199)</li>
    <li>Kayky Silva Stiliano (RM555148)</li>
</ul>

## Instruções
O arquivo ```main.py``` é o arquivo principal que deve ser rodado e é recomendado usar o terminal no tamanho 75% ou tela cheia.

## Explicação do Projeto 📖
Um app em Python, com o tema de poluição marinha, que dá ao usuário escolhas de seção onde há uma simulação em formato de "mini-game" que usuário escolhe uma praia e procura por coisas, uma seção de dados capturados pelos drones que novamente é escolhida a praia desejada no qual haverá duas opções de display das informações sendo uma "opções detalhadas" com todas os resultados encontrados para aquela praia e outra "opções específicas" onde o usuário escolhe qual dado ele deseja ver tendo a possibilidade de fazer novas pesquisas também. Por fim há uma seção de doação onde o usuário pode doar uma quantia para a empresa que ajuda diretamente na salvação dos oceanos.

 
## Dependências 📦
<ul>
    <li>helpers.py</li>
    <li>simulacao.py</li>
    <li>simulacao_paths.py</li>
    <li>sysfunctions.py</li>
</ul>
 
<br>

## Explicando o <a href="path">Código</a> 🧑‍💻
 
```c
def limpar_tela(linhas=20):
    for i in range(linhas):
        print("\n")
    return
```
Essa função imprime várias linhas em branco para "limpar" a tela do console.
Parâmetros: `linhas`: Número de linhas em branco a serem impressas. O padrão é 20.
<br>
Descrição: O loop `for` imprime uma nova linha (`\n`) a cada iteração, criando a impressão de uma tela limpa.
<hr>

```c
def meu_in(lista, buscar):
    for i in range(len(lista)):
        elem = lista[i]
        if elem == buscar:
            return True
    return False
```
Essa função verifica se um elemento está presente em uma lista.
Parâmetros: `lista`: A lista onde será feita a busca. 
<br>
`buscar`: O elemento a ser buscado na lista.
<br>
Descrição: Itera sobre cada elemento da lista. Se o elemento é igual ao buscado, retorna `True`.
Se o loop termina sem encontrar o elemento, retorna `False`.
<hr>

```c
def meu_index(lista, buscar):
    for i in range(len(lista)):
        elem = lista[i]
        if elem == buscar:
            return i
    return False
```
Essa função retorna o índice de um elemento em uma lista ou `False` se não for encontrado.
Parâmetros: `lista`: A lista onde será feita a busca. 
<br>
`buscar`: O elemento a ser buscado na lista.
<br>
Descrição: Itera sobre cada elemento da lista. Se o elemento é igual ao buscado, retorna seu índice.
Se o loop termina sem encontrar o elemento, retorna `False`.
<hr>

```c
def forca_opcao(msg, lista, msg_erro):
    opcao = input(msg)
    while not meu_in(lista, opcao):
        limpar_tela()
        print(msg_erro)
        opcao = input(msg)
    return opcao
```
Essa função força o usuário a escolher uma opção válida a partir de uma lista.
Parâmetros: `msg`: Mensagem a ser exibida ao solicitar a entrada do usuário. 
<br>
`lista`: Lista de opções válidas.
<br>
`msg_erro`: Mensagem de erro a ser exibida se a opção não for válida.
<br>
Descrição: Solicita a entrada do usuário. Se a entrada não estiver na lista, limpa a tela e mostra uma mensagem de erro, repetindo a solicitação até que uma opção válida seja inserida.
<br>
Retorno: A opção válida escolhida pelo usuário.
<hr>

```c
def verifica_numero(msg, msg_erro):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    return int(num)
```
Essa função força o usuário a inserir um número válido.
Parâmetros: `msg`: Mensagem a ser exibida ao solicitar a entrada do usuário.
<br>
`msg_erro`: Mensagem de erro a ser exibida se a entrada não for um número.
<br>
Descrição: Solicita a entrada do usuário. Se a entrada não for numérica, exibe uma mensagem de erro e repete a solicitação até que um número seja inserido.
<br>
Retorno: O número inserido pelo usuário, convertido para inteiro.
<hr>

```c
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
```
Essa função imprime uma lista de opções formatada, com ou sem quebras de linha.
Parâmetros: `lista`: A lista de opções a serem impressas.
<br>
`line_break`: Booleano que determina se as opções devem ser impressas com quebras de linha (`True`) ou em uma única linha (`False`).
<br>
Descrição: Itera sobre a lista, adicionando cada elemento a uma string de saída.
Se line_break é `True`, adiciona uma nova linha após cada elemento. Caso contrário, adiciona os elementos em uma linha, separados por vírgulas.
<br>
Retorno: A string formatada com as opções.
<hr>

## Explicando o <a href="path">Código</a> 🧑‍💻
```c
from helpers import forca_opcao, limpar_tela, print_de_opcoes
from simulacao_paths import pegar_mapa, caminho_permitido
```
Descrição: Importa as funções forca_opcao, limpar_tela e print_de_opcoes do módulo helpers e as funções pegar_mapa e caminho_permitido do módulo simulacao_paths.
<hr>

```c
y_axis = 0
x_axis = 0
```
Descrição: Define variáveis globais para manter a posição atual do usuário no mapa.
<hr>

```c
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
```
Parâmetros: `direction`: A direção em que o usuário deseja se mover ('1', '2', '3', '4').
<br>
Descrição: Atualiza as coordenadas `y_axis` e `x_axis` com base na direção fornecida.
Retorna as novas coordenadas como uma lista de strings.
<hr>

```c
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
```
Descrição: Exibe uma mensagem de boas-vindas. Mostra uma lista de praias disponíveis e força o usuário a escolher uma praia válida. Exibe a mensagem de boas-vindas após a seleção da praia.
<hr>

```c
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
```
Parâmetros: `allowed_command`: Lista de comandos permitidos.
<br>
Descrição:Formata e retorna uma string com as opções de comandos permitidos.
<hr>

```c
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
```
Descrição: Inicializa variáveis para rastrear os caminhos permitidos, o caminho atual e se o lixo foi encontrado.
Define constantes para os botões de voltar e reportar lixo.
<br>
Loop infinito que continua até o usuário decidir sair ou reportar lixo.
Atualiza as opções de comandos permitidos com base na situação atual.
Limpa a tela e exibe as opções disponíveis e o caminho atual.
Força o usuário a escolher uma direção válida.
Se o usuário escolhe voltar, o loop termina.
Se o usuário escolhe reportar lixo, uma mensagem é exibida e o loop termina.
Atualiza as coordenadas e os caminhos permitidos com base na escolha do usuário.
Verifica se o lixo foi encontrado e atualiza a variável correspondente.
<hr>

## Explicando o <a href="path">Código</a> 🧑‍💻

```c
cima = '1'
direita = '2'
baixo = '3'
esquerda = '4'
```
Descrição: Define constantes para representar as direções de movimento.
<hr>


```c
def caminho_permitido(coordenadas=['0', '0']):
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
```
Parâmetros: `coordenadas`: Coordenadas atuais do usuário no mapa, com valor padrão ['0', '0'].
<br>
Descrição: Define os movimentos permitidos com base nas coordenadas atuais do usuário.
Retorna uma lista de direções permitidas.
<hr>

```c
def pegar_mapa(coordenadas, user_praia):
    COMMANDOS = ['1.', '2.', '3.', '4.']
    praia1 = 'Maresias'
    praia2 = 'Juquehy'

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
    label_esquerda_direita_com_algo_na_direita = f'{COMMANDOS[3]}   \t \t{COMMANDOS[1]}(?)\n'
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
        retornar_mapa = mapa_0
    elif coordenadas == ['0', '1']:
        retornar_mapa = mapa_1
    elif coordenadas == ['0', '2']:
        retornar_mapa = mapa_2

    elif coordenadas == ['1', '0']:
        retornar_mapa = mapa_3
    elif coordenadas == ['1', '1']:
        retornar_mapa = mapa_4
    elif coordenadas == ['1', '2']:
        retornar_mapa = mapa_5

    elif coordenadas == ['2', '0']:
        retornar_mapa = mapa_6
    elif coordenadas == ['2', '1']:
        retornar_mapa = mapa_7
    elif coordenadas == ['2', '2']:
        retornar_mapa = mapa_8

    elif coordenadas == ['-1', '0']:
        if user_praia == praia1:
            retornar_mapa = mapa_extra_cima_peixe
        elif user_praia == praia2:
            retornar_mapa = mapa_extra_cima_tronco
        else:
            retornar_mapa = mapa_extra_cima_lixo
            lixo_achado = True

    elif coordenadas == ['2', '3']:
        if user_praia == praia1:
            retornar_mapa = mapa_extra_direita_tronco
        elif user_praia == praia2:
            retornar_mapa = mapa_extra_direita_lixo
            lixo_achado = True
        else:
            retornar_mapa = mapa_extra_direita_peixe

    elif coordenadas == ['3', '0']:
        if user_praia == praia1:
            retornar_mapa = mapa_extra_baixo_lixo
            lixo_achado = True
        elif user_praia == praia2:
            retornar_mapa = mapa_extra_baixo_peixe
        else:
            retornar_mapa = mapa_extra_baixo_tronco

    else:
        retornar_mapa = 'SEM_MAPA'

    return retornar_mapa, lixo_achado
```
Parâmetros: `coordenadas`: Coordenadas atuais do usuário no mapa.
`user_praia`: Nome da praia associada ao usuário.
<br>
Descrição: Define as variáveis e constantes usadas para criar os mapas.
Com base nas coordenadas e no nome da praia do usuário, retorna um mapa formatado e um indicador se o lixo foi encontrado.
<br>
Retorno:
`retornar_mapa`: Mapa formatado.
`lixo_achado`: Booleano indicando se o lixo foi encontrado.
<hr>

## Explicando o <a href="path">Código</a> 🧑‍💻

```c

```




 
<center>Este projeto encontra sob a <a href="path">MIT License.</a></center>
