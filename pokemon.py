from random import*#importando a biblioteca para numeros aleatorios
import time


def insert(lista):
    for i in range (1, len(lista)):
        aux= lista[i]
        j= i-1
        while j>=0 and aux < lista[j]:
            lista[j+1]= lista[j]
            j-=1
        lista[j+1]= aux

def insertALF(lista):
    for i in range (1, len(lista)):
        aux= lista[i]
        j= i-1
        while j>=0 and aux < lista[j]:
            lista[j+1]= lista[j]
            j-=1
        lista[j+1]= aux
    print(lista)

def procura(lista, indice):
    for i in range(0, len(lista)):
        if lista[i] == indice:
            return 1
    return 0

def ordenaVIO(matriz, indice):
    raridade = []
    for i in range (0, len(matriz)):
        raridade.append(matriz[i][indice])
    #print(matriz)
    insert(raridade)
    vetorIO = []#vetor que recebera os indices

    for i in range(0, len(matriz)):
        for j in range(0, len(matriz)):
            if matriz[j][indice] == raridade[i]:
                validacao = procura(vetorIO, j)# chama a funcao para verificar se tem o indice repetido no vetor IO
                if validacao == 0:
                    vetorIO.append(j)
                else:
                    break

    for i in range(0, len(matriz)):
        print(matriz[vetorIO[i]])

def ordenaAlfavetica(matrizPokemon, indice):
    ordemAlf = []

    for i in range(0, len(matrizPokemon)):
        ordemAlf.append(matrizPokemon[i][indice])
    insertALF(ordemAlf)

def inserirPokemon(matriz, lista):
    matriz.append(lista)# adiciona os dados do pokemon na matriz de pokemons.

def menuORDER(pokemons):
    opcao = 1;
    while opcao != 4:
        opcao = int(input("1 - Orderm alfabetica.\n2 - Ordem de CP(Combat Power).\n3 - Ordem raridade. \n4 - Voltar.\n"))

        if opcao == 1:
            ordenaAlfavetica(pokemons, 0)  # manda o indice que quero ordernar(Alfabeto)

        elif opcao == 2:
            ordenaVIO(pokemons, 2)  # manda o indice que quero ordernar(nivel de CP - Combat Power)

        elif opcao == 3:
            ordenaVIO(matrizPokemon, 1)  # manda o indice que quero ordernar(nivel de raridade)

def GerarPokemon():
    mPokemon = [['pikachu', 2, 500],
                     ['pikachu', 2, 200],
                     ['charmeleon', 3, 1500],
                     ['wartortle', 2, 1456],
                     ['blastoise', 1, 3200],
                     ['chartzard', 1, 3700],
                     ['charmander', 6, 200],
                     ['ivysaur', 3, 1600],
                     ['venusaur', 1, 3400],
                     ['eeve', 12, 100],
                     ['ratata', 11, 600],
                     ['bulbassaur', 6, 500],
                     ['squirtle', 6, 500],
                     ['moltres', 4, 1000],
                     ['zapdos', 5, 500],
                     ['bayleef', 3, 250],
                     ['feralgatr', 1, 2000],
                     ['dragonite', 3, 700],
                     ['crobat', 8, 300],
                     ['togepi', 2, 10],
                     ['aerodactyl', 2, 1200],
                     ['kabutops', 1, 870],
                     ['exeggutor', 1, 3000],
                     ['hitmonchan', 3, 2400],
                     ['rhydon', 10, 530],
                     ['alakazan', 1, 5000],
                     ['pidgey', 12, 20],
                     ['pidgeotto', 11, 100],
                     ['pedgeot', 10, 1500],
                     ['raticate', 11, 300],
                     ['charmander', 6, 600],
                     ['eeve', 12, 1000],
                     ['ratata', 11, 10],
                     ['bulbassaur', 6, 30],
                     ['square', 6, 345],
                     ['moltres', 4, 1660],
                     ['zapdos', 5, 578],
                     ['bayleef', 3, 20],
                     ['feralgatr', 1, 2400],
                     ['dragonite', 3, 750],
                     ['crobat', 8, 25],
                     ['togepi', 2, 30],
                     ['aerodactyl', 2, 580],
                     ['kabutops', 1, 555],
                     ['exeggutor', 1, 990],
                     ['hitmonchan', 3, 1345],
                     ['rhydon', 10, 290],
                     ['alakazan', 1, 2567],
                     ['pidgey', 12, 120],
                     ['pidgeotto', 11, 543],
                     ['pedgeot', 10, 167],
                     ['raticate', 11, 45], ]

    numPok = randint(0, len(mPokemon))
    return mPokemon[numPok]

def GerarPerguntas():
    matrizPerguntas = [[ "Listas lineares (Linguagem C): Eh um conjunto de elementos de diferentes tipos, armazenados linearmente(em sequencia)? " ,"1+1x2+1 eh = 5? ", "python eh uma lingaguem OO? ", "A linguagem C++ eh uma extensao da linguagem C? ", "Boa Vista eh capital do estado de Rondonia? ", "1 + 1 eh = 10? ", "QuickSort tem como principio dividir para conquistar? "],
                       [0 ,0, 1, 1, 0, 1, 1]]
    numPer = randint(0, len(matrizPerguntas))
    return matrizPerguntas[0][numPer], matrizPerguntas[1][numPer] # envia a pergunta e reposta de acordo com o numero que foi sorteado, pegando o numero da coluna

def GerarCuriosidades():

    curiosidades = ['A origem de Pokemon esta em dois jogos chamados Pokemon green e Pokemon Red, foram lancados em 1996.' ,'Os nomes para cada um dos tres passaros lendarios termina em contagem em espanhol: Articuno, Zapdos e Moltres. ', 'A Nintendo foi processada por um magico por usar Abra, Kadabra e Alakazam como nomes de Pokemon. A companhia venceu o processo', 'PokemonGO foi programado em C#, usando o Unity Framework. ', 'Cientistas batizaram uma proteina que ajuda a carregar impulsos eletricos dos olhos para o cerebro, de Pikachurin, em referencia ao monstrinho amarelo. ', 'Pokemon foi criado primeiro em jogo, depois foi feito em Anime.']
    n = randint(0 , len(curiosidades) - 1)
    return curiosidades[n]

def Jogar(MatrizP):
    frase = GerarCuriosidades()
    print("Loading . . .                    %s" %frase)
    time.sleep(5.5)
    pergunta, resposta = GerarPerguntas()
    pokemon = GerarPokemon()
    # print(pergunta, resposta, pokemon)
    print("Pokemon : %s" %pokemon[0], " Nivel de Raridade: %d" %pokemon[1], "CP(Combat Power): %d" %pokemon[2])
    print("1 - Para SIM,         0 - NAO.  ")
    answer = int(input(pergunta))
    if answer == resposta:
        print("Parabens! Voce capturou o Pokemon ", pokemon[0])
        inserirPokemon(MatrizP, pokemon)
    else:
        print("Voce errou. =/           Boa sorte na proxima vez!")

def menu(pokemons):
    aux = 1
    while aux != 3: # se for igual a 3 eh para sair do laco
        aux = int(input("Bem vindo ao jogo PokemonGO \n1 - Ver lista de pokemons \n2 - Jogar \n3 - Sair. =( \n"))
        if aux == 1:
            menuORDER(pokemons)# manda para a funcao que tem um menu de ordenacoes.
        elif aux == 2:
            Jogar(pokemons)# envia para funcao do jogode perguntas e respostas







'''------------------------------------------------------ M      A      I      N ----------------------------------------------------------'''
# Cria matriz dos pokemons iniciais
matrizPokemon = [['pikachu', 2, 500],
                 ['charmander', 6, 200],
                 ['eeve', 11, 100],
                 ['ratata', 12, 600],
                 ['bulbassaur', 6, 500],
                 ['square', 6, 500]]
# envia para funcao onde tera o menu de opcoes.
menu(matrizPokemon)
print("Ate mais!")

