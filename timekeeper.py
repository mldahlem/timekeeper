"""
Programa para mensurar o tempo gasto em projetos.
Marcelo Luis Dahlem
"""

import time
import os
import sys

"""Define o nome e os locais dos arquivos de dados.
O arquivo 'project_values.dat' deve ser criado contendo uma 
linha por nome de projeto com o seguinte template:

nome_do_projeto,valor

sendo o valor digitado com '.' como separador de decimais,
por exemplo: caso o nome do projeto seja XYZ e o custo da hora seja R$ 200 ficará assim:

XYZ,200.00

Os demais arquivos serão criados automaticamente. Em outra versão irei
automatizar o arquivo 'project_values.dat' também.
"""
arq_projetos = "D:\\Apps\\DataFiles\\projects.dat"
arq_tempos = "D:\\Apps\\DataFiles\\project_times.dat"
arq_valores = "D:\\Apps\\DataFiles\\project_values.dat"


def menuInicial():
    """
        Função que chama o menu inicial e retorna a opção escolhida.

        :return opcao
    """
    os.system('cls')
    print("\n  Escolha a opção:\n")
    print("  1 - Novo projeto")
    print("  2 - Abre projeto existente")
    print("  3 - Calcula o tempo total de um projeto")
    print("  X - Sair\n")
    opcao = input("  Qual sua opção? ")
    return opcao


def projectList(arq):
    """
        Gera uma lista com todos os nomes de projetos contidos no arquivo 'projects.dat'.

        :param arq: string -> nome do arquivo, está definido no início do programa

        :return projects: lista com os nomes dos projetos
    """
    f = open(arq, "r")
    linhas = f.readlines()
    projects = []
    for linha in linhas:
        projects.append(linha.strip('\n'))
    f.close()
    return projects


def createProject(arq):
    """
            Solicita que o usuário digite um novo nome de projeto e
            adiciona-o no arquivo que contém a relação de projetos do usuário.

            :param arq: string -> nome do arquivo, está definido no início do programa

            :return null
    """
    os.system('cls')
    print("\n  A opção escolhida foi para inclusão de um novo projeto \n")
    nome = input("  Digite a identificação que gostaria de dar para o projeto: ")
    f = open(arq, "a")
    f.write(nome + "\n")
    f.close()


def addTempo(arq, projeto):
    """
            Inicia uma nova contagem de tempo para o projeto selecionado quando o usuário
            digita '0' e finaliza a contagem de tempo quando o usuário digita 'fim'.
            Após, faz o cálculo do tempo em segundos e registra no arquivo 'project_times.dat'.

            :param arq: string -> nome do arquivo, está definido no início do programa
            :param projeto: string

            :return null
    """
    inicio = time.time()
    os.system('cls')
    print(f"\n  A contagem do tempo começou agora, exatamente às {time.ctime()}\n")
    opcao = ''
    while opcao.lower() != 'fim':
        opcao = input("  Para encerrar a contagem, digite 'fim': ")

    fim = time.time()
    tempo = fim - inicio
    f = open(arq, "a")
    f.write(time.ctime() + ',' + projeto.strip('\n') + ',' + str(tempo) + ',' + 'segundos\n')
    f.close()


def calculaTempo(arq, projeto):
    """
            Calcula o tempo total de um projeto selecionado a partir do arquivo de dados.

            :param arq: string -> nome do arquivo, está definido no início do programa
            :param projeto: string

            :return soma: float
    """
    f = open(arq, "r")
    linhas = f.readlines()
    soma = 0
    for linha in linhas:
        plan = linha.split(',')
        if plan[1] in projeto:
            soma = soma + float(plan[2])
    return soma


def calculaCusto(arq, projeto, horas):
    """
            Calcula o custo total de um projeto selecionado com base no parâmetro horas e com
            o custo de hora unitária definido no arquivo 'project_values.dat'.

            :param arq: string -> nome do arquivo, está definido no início do programa
            :param projeto: string
            :param horas: float

            :return float(valor) * horas
    """
    f = open(arq, "r")
    linhas = f.readlines()
    valor = 0
    for linha in linhas:
        plan = linha.split(',')
        if plan[0] in projeto:
            valor = plan[1]
    return float(valor) * horas


def newTimeCount():
    """
        Função utilizada apenas para organizar o código. Esta função é chamada quando o
        usuário escolhe a opção 2 no menu inicial.
    """
    listaProjetos = projectList(arq_projetos)
    os.system('cls')
    print("\n  Você escolheu definir um projeto já existente, favor digitar o número referente ao projeto escolhido\n")
    contador = 0

    for linha in listaProjetos:
        print(f"  {contador}: {linha}")
        contador += 1

    projeto = str(contador + 1)

    while int(projeto) >= contador:
        projeto = input("\n  Digite a opção ou 'x' para sair: ")
        if projeto.lower() == 'x':
            sys.exit()

    projectName = listaProjetos[int(projeto)]
    os.system('cls')
    print(f"\n  Você escolheu o projeto: {projectName}")

    opcao = '1'
    while opcao != '0':
        opcao = input("\n  Para iniciar a contagem do tempo, digite 0: ")

    addTempo(arq_tempos, projectName)


def timeAndCostCalculation():
    """
        Função utilizada apenas para organizar o código. Esta função é chamada quando o
        usuário escolhe a opção 3 no menu inicial.
    """
    listaProjetos = projectList(arq_projetos)
    os.system('cls')
    print("\n  Você escolheu calcular o tempo total, favor digitar o número referente ao projeto escolhido\n")
    contador = 0

    for linha in listaProjetos:
        print(f"  {contador}: {linha}")
        contador += 1

    projeto = str(contador + 1)

    while int(projeto) >= contador:
        projeto = input("\n  Digite a opção ou 'x' para sair: ")
        if projeto.lower() == 'x':
            sys.exit()

    projectName = listaProjetos[int(projeto)]
    horas = calculaTempo(arq_tempos, projectName) / 3600
    os.system('cls')
    print(f"\n  Você escolheu o projeto: {projectName}\n")
    print(f'  O tempo total deste projeto até o momento é de {horas:,.2f} horas.')
    print(f'  O tempo total deste projeto até o momento é de {horas * 60:,.2f} minutos.')
    print(f'  O tempo total deste projeto até o momento é de {horas * 3600:,.2f} segundos.')
    print(f'\n  O valor total de acordo com o custo hora definido para este projeto foi de: R$ '
          f'{calculaCusto(arq_valores, projectName, horas):,.2f}')
    input("\n  Pressione enter para continuar: ")


def main():
    """
        Função principal do programa.
    """
    opcao = menuInicial()

    if opcao == "1":
        createProject(arq_projetos)
        main()

    elif opcao == "2":
        newTimeCount()

    elif opcao == "3":
        timeAndCostCalculation()

    elif opcao.lower() == 'x':
        sys.exit()


"""
A seguir, comando para que o programa fique em loop até 
que a opção de saída seja escolhida pelo usuário.
"""
opcao = '1'
while opcao != '0':
    main()
