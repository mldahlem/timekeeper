"""
Programa para mensurar o tempo gasto em projetos.
Marcelo Luis Dahlem
"""

from datetime import datetime
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

FILE_PROJECTS = "D:\\Apps\\DataFiles\\projects.dat"
FILE_TIMES = "D:\\Apps\\DataFiles\\project_times.dat"
FILE_VALUES = "D:\\Apps\\DataFiles\\project_values.dat"


def menu() -> str:
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


def project_list(arq: str) -> list:
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


def create_project(arq: str) -> None:
    """
            Solicita que o usuário digite um novo nome de projeto e
            adiciona-o no arquivo que contém a relação de projetos do usuário.

            :param arq: string -> nome do arquivo, está definido no início do programa

            :return None
    """
    os.system('cls')
    print("\n  A opção escolhida foi para inclusão de um novo projeto \n")
    nome = input("  Digite a identificação que gostaria de dar para o projeto: ")
    f = open(arq, "a")
    f.write(nome + "\n")
    f.close()
    return


def add_tempo(arq: str, projeto: str) -> None:
    """
            Inicia uma nova contagem de tempo para o projeto selecionado quando o usuário
            digita '0' e finaliza a contagem de tempo quando o usuário digita 'fim'.
            Após, faz o cálculo do tempo em segundos e registra no arquivo 'project_times.dat'.

            :param arq: string -> nome do arquivo, está definido no início do programa
            :param projeto: string

            :return None
    """
    inicio = datetime.now()
    print(f"\n  A contagem do tempo começou agora, exatamente às {inicio.strftime('%d/%m/%Y %H:%M')}\n")
    opcao = ''
    while opcao.lower() != 'fim':
        opcao = input("  Para encerrar a contagem, digite 'fim': ")

    fim = datetime.now()
    tempo = fim - inicio
    f = open(arq, "a")
    f.write(fim.strftime('%d/%m/%Y') + ',' + projeto.strip('\n') + ',' +
            str(tempo.total_seconds()) + ',' + 'segundos\n')
    f.close()
    return


def calcula_tempo(arq: str, projeto: str) -> float:
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


def calcula_custo(arq: str, projeto: str, horas: float) -> float:
    """
            Calcula o custo total de um projeto selecionado com base no parâmetro horas e com
            o custo de hora unitária definido no arquivo 'project_values.dat'.

            :param arq: string -> nome do arquivo, está definido no início do programa
            :param projeto: string
            :param horas: float

            :return float(valor) * horas: float
    """
    f = open(arq, "r")
    linhas = f.readlines()
    valor = 0
    for linha in linhas:
        plan = linha.split(',')
        if plan[0] in projeto:
            valor = plan[1]
    return float(valor) * horas


def new_time_count() -> None:
    """
        Função utilizada apenas para organizar o código. Esta função é chamada quando o
        usuário escolhe a opção 2 no menu inicial.
    """
    lista_projetos = project_list(FILE_PROJECTS)
    os.system('cls')
    print("\n  Você escolheu definir um projeto já existente, favor digitar o número referente ao projeto escolhido\n")
    contador = 0

    for linha in lista_projetos:
        print(f"  {contador}: {linha}")
        contador += 1

    projeto = str(contador + 1)

    while int(projeto) >= contador:
        projeto = input("\n  Digite a opção ou 'x' para sair: ")
        if projeto.lower() == 'x':
            sys.exit()

    project_name = lista_projetos[int(projeto)]
    os.system('cls')
    print(f"\n  Você escolheu o projeto: {project_name}")

    opcao = '1'
    while opcao != '0':
        opcao = input("\n  Para iniciar a contagem do tempo, digite 0: ")

    add_tempo(FILE_TIMES, project_name)
    return


def time_and_cost_calculation() -> None:
    """
        Função utilizada apenas para organizar o código. Esta função é chamada quando o
        usuário escolhe a opção 3 no menu inicial.
    """
    lista_projetos = project_list(FILE_PROJECTS)
    os.system('cls')
    print("\n  Você escolheu calcular o tempo total, favor digitar o número referente ao projeto escolhido\n")
    contador = 0

    for linha in lista_projetos:
        print(f"  {contador}: {linha}")
        contador += 1

    projeto = str(contador + 1)

    while int(projeto) >= contador:
        projeto = input("\n  Digite a opção ou 'x' para sair: ")
        if projeto.lower() == 'x':
            sys.exit()

    project_name = lista_projetos[int(projeto)]
    horas = calcula_tempo(FILE_TIMES, project_name) / 3600
    os.system('cls')
    print(f"\n  Você escolheu o projeto: {project_name}\n")
    print(f'  O tempo total deste projeto até o momento é de {horas:,.2f} horas.')
    print(f'  O tempo total deste projeto até o momento é de {horas * 60:,.2f} minutos.')
    print(f'  O tempo total deste projeto até o momento é de {horas * 3600:,.2f} segundos.')
    print(f'\n  O valor total de acordo com o custo hora definido para este projeto foi de: R$ '
          f'{calcula_custo(FILE_VALUES, project_name, horas):,.2f}')
    input("\n  Pressione enter para continuar: ")
    return


def main() -> None:
    """
        Função principal do programa.
    """
    opcao = menu()

    if opcao == "1":
        create_project(FILE_PROJECTS)
        main()

    elif opcao == "2":
        new_time_count()

    elif opcao == "3":
        time_and_cost_calculation()

    elif opcao.lower() == 'x':
        sys.exit()

    return


"""
A seguir, comando para que o programa fique em loop até 
que a opção de saída seja escolhida pelo usuário.
"""
x = 1
while x:
    main()
