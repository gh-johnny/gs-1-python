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

## Explicando o <a href="https://github.com/gh-johnny/gs-1-python/blob/main/helpers.py">Código</a> 🧑‍💻
 
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

## Explicando o <a href="https://github.com/gh-johnny/gs-1-python/blob/main/main.py">Código</a> 🧑‍💻

```c
from helpers import forca_opcao, limpar_tela
from sysfunctions import sys_dados, sys_doacao
from simulacao import tela_simulacao
```
Descrição: Importa as funções `forca_opcao` e `limpar_tela` do módulo `helpers`, as funções `sys_dados` e `sys_doacao` do módulo `sys_functions` e a função `tela_simulacao` do módulo `simulacao`.
<hr>

```c
nome_da_empresa = "Ocean Guardians"
lista_menu_opcao = ['1', '2', '3', '0']
lista_praias = ["Maresias", "Juquehy", "Ubatuba"]
```
Descrição: `lista_menu_opcao`: Contém as opções de menu principais ('1', '2', '3', '0'). `lista_praias`: Lista das praias monitoradas pelo sistema.
<hr>


```c
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
```
Descrição: O loop `while True` exibe continuamente o menu principal até que o usuário escolha sair (opção '0').
<br>
Passos no Loop:
Exibição do Menu:
O sistema exibe uma mensagem de boas-vindas e solicita ao usuário que escolha uma das opções disponíveis no menu.
<br>
Processamento da Escolha:
A função `forca_opcao` é usada para garantir que o usuário insira uma opção válida. Caso contrário, uma mensagem de erro é exibida.
<br>
Limpeza da Tela:
`limpar_tela` é chamada para limpar a tela antes de continuar com a ação selecionada.
<br>
Execução da Função Correspondente:
Dependendo da escolha do usuário, uma das três funções é chamada: Simulação: `tela_simulacao`; Dados Capturados: `sys_dados`; Doação: `sys_doacao`; Saída do Loop:
Se a escolha for '0', o loop é interrompido e o programa termina.
<hr>

## Explicando o <a href="https://github.com/gh-johnny/gs-1-python/blob/main/simulacao.py">Código</a> 🧑‍💻
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

## Explicando o <a href="https://github.com/gh-johnny/gs-1-python/blob/main/simulacao_paths.py">Código</a> 🧑‍💻

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
from helpers import forca_opcao, verifica_numero, meu_index, print_de_opcoes
```
Descrição: Importa as funções forca_opcao, verifica_numero, meu_index, print_de_opcoes do módulo helpers.
<hr>

```c
lista_tipo_dados = ['1', '2']
lista_dados_opcao = ['1', '0']
lista_dados_especificos = ['1', '2', '3', '4', '5', '6', '7']
lista_doacao_opcao = ['s', 'n', '0']
lista_praias = ["Maresias", "Juquehy", "Ubatuba"]
```
Descrição: Listas que contêm as opções que os usuários podem selecionar.
<hr>

```c
sensor_LDR = [90, 65, 47]
sensor_DHT_oxy = [7, 4, 2]
sensor_DHT_temp = [25, 20, 10]
sensor_pH = [8, 7.5, 6]
sensor_gas_CO2 = [50, 45, 30]
sensor_gas_CH4 = [1, 5, 15]
sensor_proximidade = [350, 150, 50]
total_doado = 0
```
Descrição: Listas que contêm valores capturados dos sensores dos drones em diferentes praias.
<hr>

```c
def sys_dados():
    def exibir_diagrama():
        print("\nDiagrama de informações:\n"
              "Luminosidade:\n - acima de 70% = normal\n - entre 50 e 69% = em alerta\n "
              "- abaixo de 50% = estado crítico / derramamento de óleo\n"
              "Oxigênio:\n - acima ou igual a 5mg/L = normal\n - entre 2.1 e 4.9mg/L = em alerta\n "
              "- abaixo ou igual a 2mg/L = estado crítico\n"
              "Temperatura:\n - entre 20 e 29ºC = normal\n - acima ou igual a 30ºC = temperatura elevada\n - abaixo ou igual a 19ºC = temperatura abaixo\n"
              "pH:\n - entre 7,5 e 8,4 = normal\n - abaixo de 7,5 = acidificação\n - acima de 8,4 = "
              "alcalinidade excessiva\n"
              "Gás Carbônico(CO2):\n - entre 45 e 55% = normal\n - caso contrário = concentração anormal\n"
              "Gás Metano(CH4):\n - entre 0 e 5% = normal\n - caso contrário = concentração excessiva\n"
              "Proximidade:\n - acima ou igual a 200m = lixo não detectado\n - abaixo ou igual a 199m = "
              "objeto detectado\n - abaixo ou igual a 50m = lixo detectado\n")
```
Descrição: Esta função permite ao usuário consultar dados ambientais das praias e a função interna exibe um diagrama de informações detalhando os intervalos normais, de alerta e críticos para cada tipo de dado.
<hr>

```c
    def exibir_resultado(local_praia):
        print(f"\nResultado: O mar da praia {lista_praias[local_praia]} está com uma luminosidade de "
              f"{sensor_LDR[local_praia]}%, oxigênio está em {sensor_DHT_oxy[local_praia]}mg/L, "
              f"temperatura está em {sensor_DHT_temp[local_praia]}ºC, o pH está em {sensor_pH[local_praia]}, "
              f"a quantia de CO2(Gás Carbônico) é de {sensor_gas_CO2[local_praia]}% e de CH4"
              f"(Gás Metano) é de {sensor_gas_CH4[local_praia]}%, e a distância do sensor de proximidade é de {sensor_proximidade[local_praia]} metros\n")
```
Descrição: Exibe todos os resultados de valores dos sensores para uma praia específica.
<hr>

```c
    def exibir_dado_especifico(local_praia, dado_especifico):
        if dado_especifico == '1':
            print("Luminosidade:\n - acima de 70% = normal\n - entre 50 e 69% = em alerta\n "
                  "- abaixo de 50% = estado crítico / derramamento de óleo\n"
                  f"\nLuminosidade está em {sensor_LDR[local_praia]}%")
        elif dado_especifico == '2':
            print("Oxigênio:\n - acima ou igual a 5mg/L = normal\n - entre 2.1 e 4.9mg/L = em alerta\n - abaixo ou igual a 2mg/L = estado crítico\n"
                  f"\nOxigênio está em {sensor_DHT_oxy[local_praia]}mg/L")
        elif dado_especifico == '3':
            print("Temperatura:\n - entre 20 e 29ºC = normal\n - acima ou igual a 30ºC = temperatura elevada\n - abaixo ou igual a 19ºC = temperatura abaixo\n"
                  f"\nTemperatura está em {sensor_DHT_temp[local_praia]}ºC")
        elif dado_especifico == '4':
            print("pH:\n - entre 7,5 e 8,4 = normal\n - abaixo de 7,5 = acidificação\n - acima de 8,4 = alcalinidade excessiva\n"
                  f"\npH está em {sensor_pH[local_praia]}")
        elif dado_especifico == '5':
            print("Gás Carbônico(CO2):\n - entre 45 e 55% = normal\n - caso contrário = concentração anormal\n"
                  f"\nQuantia de CO2(Gás Carbônico) é de {sensor_gas_CO2[local_praia]}%")
        elif dado_especifico == '6':
            print("Gás Metano(CH4):\n - entre 0 e 5% = normal\n - caso contrário = concentração excessiva\n"
                  f"\nQuantia de CH4(Gás Metano) é de {sensor_gas_CH4[local_praia]}%")
        elif dado_especifico == '7':
            print("Proximidade:\n - acima ou igual a 200m = lixo não detectado\n - abaixo ou igual a 199m = objeto detectado\n - abaixo ou igual a 50m = lixo detectado\n"
                  f"\nDistância do sensor de proximidade é de {sensor_proximidade[local_praia]} metros")
    while True:
        escolha_praia = forca_opcao(
            "Digite uma praia que deseja procurar dados\n --> ", lista_praias, "Opção Inválida!\nPor favor, escolha uma das praias disponíveis:\n" + print_de_opcoes(lista_praias))
        local_praia = meu_index(lista_praias, escolha_praia)
        escolha_tipo_dados = forca_opcao("Você deseja ver opções detalhadas ou específicas? (1 - opções detalhadas e 2 - opções específicas)\n--> ",
                                         lista_tipo_dados, "Digite apenas os números correspondentes ao caminho indicado")
        if escolha_tipo_dados == '1':
            exibir_diagrama()
            exibir_resultado(local_praia)
        elif escolha_tipo_dados == '2':
            dados_especifico = forca_opcao("Qual dado você deseja procurar?\n 1 - Luminosidade\n 2 - Oxigênio\n 3 - Temperatura\n 4 - pH\n 5 - Gás Carbônico(CO2)\n 6 - Gás Metano(CH4)\n 7 - Proximidade\n--> ",
                                           lista_dados_especificos, "Digite apenas os números correspondentes ao caminho indicado")
            exibir_dado_especifico(local_praia, dados_especifico)
        escolha_dados = forca_opcao("O que você deseja fazer?\n 1 - Nova pesquisa\n 0 - Voltar para o menu\n--> ",
                                    lista_dados_opcao, "Opção inválida! Digite apenas os números correspondentes ao caminho indicado")
        if escolha_dados == '1':
            continue
        elif escolha_dados == '0':
            break
```
Descrição: Exibe informações detalhadas e o valor de um sensor específico para a praia selecionada. 
<br>
Lógica Principal: Solicita ao usuário que selecione uma praia e o tipo de dados (detalhado ou específico) que deseja ver. Se o usuário selecionar "opções detalhadas", chama `exibir_diagrama()` e `exibir_resultado()`.
Se o usuário selecionar "opções específicas", solicita o dado específico e chama `exibir_dado_especifico()`. Após exibir os dados, pergunta se o usuário deseja fazer uma nova pesquisa ou voltar ao menu principal.
<hr>

```c
def sys_doacao():
    global total_doado
    while True:
        doacao = verifica_numero(
            "Digite a quantia que deseja doar\n--> ", "Digite apenas números inteiros!")
        if doacao <= 0:
            continue

        escolha_doacao = forca_opcao(f"Você deseja doar R${doacao:.2f} ?('s' para continuar, 'n' "
                                     "para voltar, 0 - para sair)\n--> ", lista_doacao_opcao,
                                     "Digite apenas os números correspondentes ao caminho indicado")
        if escolha_doacao == "s":
            total_doado += doacao
            print(f"\nMuitissímo obrigado pela sua doação de R${doacao:.2f} !!!\n"
                  f"Total doado: R${total_doado:.2f}\n")
            break
        elif escolha_doacao == "n":
            continue
        elif escolha_doacao == '0':
            break
```
Descrição: Esta função permite ao usuário fazer doações.
<br>
Lógica Principal: Solicita ao usuário que insira a quantia a ser doada. Pergunta ao usuário se ele deseja confirmar a doação, voltar ou sair. Se confirmado, adiciona a quantia ao `total_doado` e exibe uma mensagem de agradecimento. Se o usuário escolher voltar, solicita novamente a quantia da doação. Se o usuário escolher sair, a função termina.
<hr>

<center>Este projeto encontra sob a <a href="path">MIT License.</a></center>
