
# Lista Telefonica que grava e le de arquivo de texto

ARQUIVO = "lista_telefonica.txt" # Nome do arquivo de texto

def le_arquivo():                # Função que le o arquivo de texto
    try:                         # Tratamento de erro
        arq = open(ARQUIVO,"r+") # Abre o arquivo para leitura
        print( '\n'+arq.read() ) # Quebra linha e mostra o conteudo
        arq.close()              # Fecha o arquivo
    except IOError:              # Tratamento de erro
        print('\nArquivo não encontrado!')

def escreve_arquivo(texto):        # Função que le e escreve no arquivo
    try:                           # Tratamento de erro
        arq = open(ARQUIVO,"a+")   # Abre o arquivo para gravação no final do arquivo
        arq.writelines('\n'+texto) # Escreve no arquivo o parametro 'texto'
        arq.close()                # Fecha o arquivo
        print('\nRegistro gravado com sucesso')
    except IOError:                # Tratamento de erro
        print('\nErro ao abrir o arquivo!') # Mostra na tela uma mensagem de erro

while(True):                     # Loop infinito
    print('\nEscolha a opcao:')
    print('1-Cadastrar Telefone')
    print('2-Listar Telefones')
    print('0-Sair')
    vOpcao = int(input('Digite a sua opcao:')) # Entrada da opcao pelo teclado

    if vOpcao == 1:                           # Se a opcao for 1
        nome = input('\nDigite o nome:')      # Entrada do nome pelo teclado
        telefone = input('Digite o telefone:')# Entrada do telefone pelo teclado
        nome = (nome+' - '+telefone)          # Recebe o nome + o telefone
        escreve_arquivo(str(nome))            # Chama a função que grava em arquivo
    elif vOpcao == 2:             # Se a opcao for 2
        le_arquivo()              # Chama a função que le o arquivo
    elif vOpcao == 0:             # Se a opcao for 0
        break   
