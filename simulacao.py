from helpers import print_de_opcoes, forca_opcao, limpar_tela


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

##


def tela_simulacao():
    print(f'{user_praia}:\t\t 0. Para Voltar\n\n'
          '   \t  1.\n'
          '   \t^\n'
          '   \t|\n'
          '4.   \t|\t 2.\n'
          ' < - -     - - > \n'
          '   \t|\n'
          '   \t|\n'
          '   \tv\n'
          '   \t  3.')
    return


limpar_tela()
tela_simulacao()
