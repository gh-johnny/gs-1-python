from helpers import forca_opcao, verifica_numero, meu_index, print_de_opcoes

lista_tipo_dados = ['1', '2']
lista_dados_opcao = ['1', '0']
lista_dados_especificos = ['1', '2', '3', '4', '5', '6', '7']
lista_doacao_opcao = ['s', 'n', '0']
lista_praias = ["Maresias", "Juquehy", "Ubatuba"]
sensor_LDR = [90, 65, 47]
sensor_DHT_oxy = [7, 4, 2]
sensor_DHT_temp = [25, 20, 10]
sensor_pH = [8, 7.5, 6]
sensor_gas_CO2 = [50, 45, 30]
sensor_gas_CH4 = [1, 5, 15]
sensor_proximidade = [350, 150, 50]
total_doado = 0


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

    def exibir_resultado(local_praia):
        print(f"\nResultado: O mar da praia {lista_praias[local_praia]} está com uma luminosidade de "
              f"{sensor_LDR[local_praia]}%, oxigênio está em {
                  sensor_DHT_oxy[local_praia]}mg/L, "
              f"temperatura está em {sensor_DHT_temp[local_praia]}ºC, o pH está em {
                  sensor_pH[local_praia]}, "
              f"a quantia de CO2(Gás Carbônico) é de {
            sensor_gas_CO2[local_praia]}% e de CH4"
            f"(Gás Metano) é de {sensor_gas_CH4[local_praia]}%, e a distância do sensor de proximidade é de {sensor_proximidade[local_praia]} metros\n")

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
            print(f"Muitissímo obrigado pela sua doação de R${doacao:.2f} !!!\n"
                  f"Total doado: R${total_doado:.2f}")
            break
        elif escolha_doacao == "n":
            continue
        elif escolha_doacao == '0':
            break
