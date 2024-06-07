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

```


















## Explicando o <a href="path">Código</a> 🧑‍💻







 
<center>Este projeto encontra sob a <a href="path">MIT License.</a></center>
