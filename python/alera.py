# alera - motor logico (sprint 2 - computational thinking with python)

# Daniel Souza Gomes, rm575813
# Victor Santos Ferreira de Morais, rm575508
# Diego Ramos Pereira Gonzalez, rm574620
# Diego Alejandro Ribeiro Olalla, rm575447


#definindo senha uma lista de bairros e de abrigos para os moradores
SENHA_ADMIN = "defesa123"
BAIRROS = ["centro", "santa luzia", "linhares"]
ABRIGOS = ["escola", "igreja", "centro comunitario"]

#historico de chuva dos bairros
CHUVA = [
    [10, 22, 35, 40, 12], #centro
    [30, 45, 60, 85, 20], #santa luzia
    [40, 55, 70, 90, 50], #linhares
]

#nivel de agua em cada bairro
NIVEL = [20, 70, 110]

# moradores e missoes para concluir
MORADORES = [["ana", 1, 120], ["bruno", 2, 90], ["carla", 0, 150]]
MISSOES = [["limpar o bueiro da rua", 30], ["avisar 3 vizinhos", 20]]


#recebe um texto um numero minmo e maximo, se estiver fora dos padroes ele printa um erro e volta a funcao do inicio
def ler_numero(msg, minimo, maximo):
    while True:
        texto = input(msg)
        if texto.isdigit() == False:
            print("digite apenas numeros")
        else:
            numero = int(texto)
            if numero < minimo or numero > maximo:
                print(f"digite um numero de {minimo} a {maximo}")
            else:
                return numero


def escolher_bairro():
    #loop para mostrar os bairros com numero do lado e nome do bairo do outro
    for i in range(len(BAIRROS)):
        print(f"{i + 1} - {BAIRROS[i]}")

    #chava a funcao de ler numero com a mensagem bairro: que o numero minmo vai ser 1 e o maximo vai ser a quantidade de bairros
    escolha = ler_numero("bairro: ", 1, len(BAIRROS))
    #vai retornar a escolha -1 por causa do index
    return escolha - 1

#classifica o nivel da chuva com if elif e else
def classificar_risco(chuva, nivel):
    if chuva >= 80 or nivel >= 150:
        return "emergencia"
    elif chuva >= 50 or nivel >= 100:
        return "alerta"
    elif chuva >= 25 or nivel >= 50:
        return "atencao"
    else:
        return "normal"

#vai olhar o resultado do classificar risco e dependendo da mensagem o match case vai agir diferente
def orientacao(risco, bairro):
    match risco:
        case "emergencia":
            return f"saia de casa agora. va para: {ABRIGOS[bairro]}"
        case "alerta":
            return f"prepare-se para sair. abrigo: {ABRIGOS[bairro]}"
        case "atencao":
            return "fique atento e evite areas alagaveis"
        case _:
            return "sem risco, siga sua rotina"


def risco_do_bairro(bairro):
    ultima_chuva = CHUVA[bairro][-1] #-1 pega a ultima posicao da lista de acordo com o bairro
    return classificar_risco(ultima_chuva, NIVEL[bairro]) # retorna a classificacao de risco com base na ultima chuva e tambem o nivel do bairo


def ver_alerta(morador):
    bairro = morador[1] #Pega a posicao do bairro que fica na posicao 1 da lista do morador
    risco = risco_do_bairro(bairro) # pega o risco do bairro
    print(f"{BAIRROS[bairro]}: {risco}")
    print(orientacao(risco, bairro))


def registrar_missao(morador):
    for i in range(len(MISSOES)): #para cada missao vai printar a numero- missao (+pontuacao)
        print(f"{i + 1} - {MISSOES[i][0]} (+{MISSOES[i][1]} pts)")
    escolha = ler_numero("missao concluida: ", 1, len(MISSOES))
    morador[2] = morador[2] + MISSOES[escolha - 1][1]
    print(f"missao registrada! total: {morador[2]} pts")


#exibe o ranking com base nos pontos de cada morador
def exibir_ranking():
    ranking = MORADORES.copy()
    for i in range(len(ranking)):
        for j in range(i + 1, len(ranking)):
            if ranking[j][2] > ranking[i][2]:
                temp = ranking[i]
                ranking[i] = ranking[j]
                ranking[j] = temp
    print("=== ranking ===")
    for i in range(len(ranking)):
        nome = ranking[i][0]
        pontos = ranking[i][2]
        print(f"{i + 1}o {nome} - {pontos} pts")


def painel_de_risco():
    print("=== painel da defesa civil ===")
    for i in range(len(BAIRROS)): # para a quantidade de bairros em BAIRROS
        print(f"{BAIRROS[i]}: {risco_do_bairro(i)} (nivel {NIVEL[i]} cm)") #vai printar nome do bairro: {risco} (nivel em cm)

#vai registrar uma nova chuva ou novo estado de clima nas listas
def registrar_leitura():
    bairro = escolher_bairro()
    chuva = ler_numero("chuva (mm): ", 0, 300)
    nivel = ler_numero("nivel da agua (cm): ", 0, 300)
    CHUVA[bairro].append(chuva)
    NIVEL[bairro] = nivel
    print(f"salvo! {BAIRROS[bairro]} agora: {risco_do_bairro(bairro)}")


def relatorio_chuva():
    print("=== relatorio de chuva (mm) ===") #mini titulo
    for i in range(len(CHUVA)): 
        total = sum(CHUVA[i]) #soma todas as leituras da utlimas chuvas
        media = total / len(CHUVA[i]) # faz a medai
        print(f"{BAIRROS[i]}: total {total}, media {round(media, 1)}, "
              f"maior {max(CHUVA[i])}, menor {min(CHUVA[i])}")

#cadastra um morador novo que recebe nome e bairro
def cadastrar_morador():
    nome = input("nome: ").lower()
    bairro = escolher_bairro()
    novo = [nome, bairro, 0]
    MORADORES.append(novo)
    return novo

# menu do morador que chama as funcoes de cima de acordo com o matchcase
def menu_morador():

    #loop para mostrar todos os moradores e receber quem é o morador com verificacao
    for i in range(len(MORADORES)):
        print(f"{i + 1} - {MORADORES[i][0]}")
    print(f"{len(MORADORES) + 1} - novo cadastro")
    escolha = ler_numero("quem e voce? ", 1, len(MORADORES) + 1)
    if escolha <= len(MORADORES):
        morador = MORADORES[escolha - 1]
    else:
        morador = cadastrar_morador()

    while True:
        print(f"\n--- morador: {morador[0]} ---")
        print("1 - ver alerta")
        print("2 - registrar missao")
        print("3 - ranking")
        print("0 - voltar")
        opcao = ler_numero("opcao: ", 0, 3)
        match opcao:
            case 1:
                ver_alerta(morador)
            case 2:
                registrar_missao(morador)
            case 3:
                exibir_ranking()
            case 0:
                break

#se a senha escrita estiver errada 3 vezes a funcao retorna falso oq faz retornar para a funcao main
def senha_correta():
    tentativas = 0
    while tentativas < 3:
        senha = input("senha: ")
        if senha == SENHA_ADMIN:
            return True
        print("senha incorreta")
        tentativas = tentativas + 1
    return False

#menu do administrador
def menu_admin():
    #senha errada 3 vezes = funcao main
    if senha_correta() == False:
        print("acesso bloqueado")
        return

    while True:
        print("\n--- defesa civil ---")
        print("1 - painel de risco")
        print("2 - registrar leitura")
        print("3 - relatorio de chuva")
        print("4 - cadastrar morador")
        print("0 - voltar")
        opcao = ler_numero("opcao: ", 0, 4)
        match opcao:
            case 1:
                painel_de_risco()
            case 2:
                registrar_leitura()
            case 3:
                relatorio_chuva()
            case 4:
                cadastrar_morador()
            case 0:
                break

#funcao main que executa todas as funcoes
def main():
    """menu inicial"""
    print("=== alera ===")
    while True:
        print("\n1 - morador")
        print("2 - administrador")
        print("0 - sair")
        opcao = ler_numero("entrar como: ", 0, 2)
        match opcao:
            case 1:
                menu_morador()
            case 2:
                menu_admin()
            case 0:
                print("ate logo!")
                break


main()
