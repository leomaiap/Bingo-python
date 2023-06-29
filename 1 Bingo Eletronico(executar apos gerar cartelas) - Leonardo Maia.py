# TCC00308 - PROGRAMAÇÃO DE COMPUTADORES I  →  TRABALHO BINGO ELETRÔNICO
# Aluno: Leonardo Maia Pereira        Matrícula: 120031027
# Turma: B1 - 20.1

#BIBLIOTECAS
from random import randint
from time import sleep

#FUNÇÕES
def ordenar(lista):#função para ordenar, selection sort
    for i in range(len(lista)-1):
        indiceatual = i+1
        menorvalor = i
        while indiceatual < len(lista):
            if lista[indiceatual] < lista[menorvalor]:
                menorvalor = indiceatual
            indiceatual += 1
        lista[i], lista[menorvalor] = lista[menorvalor], lista[i]

def ordenarCartela(): #função para ordenar cartelas de forma decrescente temdo numeros de já sorteados como referência
    for i in range(quantJogadores-1):
        indiceatual = i+1
        menorvalor = i
        while indiceatual < quantJogadores:
            if 10-len(cartelaJogador[indiceatual]) > 10-len(cartelaJogador[menorvalor]):
                menorvalor = indiceatual
            indiceatual += 1
        nomes[i], nomes[menorvalor] = nomes[menorvalor], nomes[i]
        cartelaJogador[i], cartelaJogador[menorvalor] = cartelaJogador[menorvalor], cartelaJogador[i]
        originalCartela[i], originalCartela[menorvalor] = originalCartela[menorvalor], originalCartela[i]

def formatarCartela(i):#Função que retorna a conversão de lista em formato de inteiro para uma string(foi usado dentro da função imprimircartelas)
    cartelaatual = str(cartelaJogador[i][:])
    char = str()
    for c in range(1,len(cartelaatual)):
        if cartelaatual[c] == ',':
            char = char+' '
        if cartelaatual[c].isnumeric():
            char = char+cartelaatual[c] 
    return char

def imprimircartelas():#Função que imprime resultados das cartelas dos jogadores na tela
    for p4 in range(0, (4*print4), 4):
        for mostarjogador in range(p4, p4+4):
            jog = f'∎ {nomes[mostarjogador]} - Sorteados: {10-len(cartelaJogador[mostarjogador])} ∎'
            print(f'{jog:^31}', end='  ')
        print()
        for mostarnumero in range(p4, p4+4):
            numerosdaCartela = formatarCartela(mostarnumero) #Função que retorna a conversão de lista em formato de inteiro para uma string
            if len(cartelaJogador[mostarnumero]) == 0:
                numerosdaCartela = 'BINGO'
            print(f'|{numerosdaCartela:^29}|', end='  ')
        print()
        print('-'*130)
        print()

    if printResto == 1:
        print(' '*50,end='')
        jog = f'∎ {nomes[mostarjogador+1]} - Sorteados: {10-len(cartelaJogador[mostarjogador+1])} ∎'
        print(f'{jog:^31}')
        print(' '*50,end='')
        numerosdaCartela = formatarCartela(mostarnumero+1) #Função que retorna a conversão de lista em formato de inteiro para uma string
        if len(cartelaJogador[mostarnumero+1]) == 0:
            numerosdaCartela = 'BINGO'
        print(f'|{numerosdaCartela:^29}|')
        print('-'*130)
    
    if printResto == 2:
        print(' '*33,end='')
        for jo in range(mostarjogador+1,mostarjogador+3):
            jog = f'∎ {nomes[jo]} - Sorteados: {10-len(cartelaJogador[jo-1])} ∎'
            print(f'{jog:^31}', end='  ')
        print()
        print(' '*33,end='')
        for num in range(mostarnumero+1,mostarnumero+3):
            numerosdaCartela = formatarCartela(num) #Função que retorna a conversão de lista em formato de inteiro para uma string
            if len(cartelaJogador[num]) == 0:
                numerosdaCartela = 'BINGO'
            print(f'|{numerosdaCartela:^29}|', end='  ')
        print()
        print('-'*130)
    
    if printResto == 3:
        print(' '*17,end='')
        for jo in range(mostarjogador+1,mostarjogador+4):
            jog = f'∎ {nomes[jo]} - Sorteados: {10-len(cartelaJogador[jo-1])} ∎'
            print(f'{jog:^31}', end='  ')
        print()
        print(' '*17,end='')
        for num in range(mostarnumero+1,mostarnumero+4):
            numerosdaCartela = formatarCartela(num) #Função que retorna a conversão de lista em formato de inteiro para uma string
            if len(cartelaJogador[num]) == 0:
                numerosdaCartela = 'BINGO'
            print(f'|{numerosdaCartela:^29}|', end='  ')
        print()
        print('-'*130)
        print()
    #fim da funçao imprimircartelas


# =PROGRAMA PRINCIPAL=
# #1- pré sortear números do globo
globo = []
tot_globo = 0
while True:
    nsorteado = randint(0,99)
    if nsorteado not in globo:
        globo.append(nsorteado)
        tot_globo += 1
    if tot_globo == 100:
        break

# #2- Boas vindas ao usuário
print('='*130)              
print(f'{"SEJA BEM-VINDO AO Ⓑ Ⓘ Ⓝ Ⓖ Ⓞ  ELETRÔNICO!!!":^130}')
print(f'{"***AO UTILIZAR REDIMENSIONE O TERMINAL ATÉ QUE TODOS IGUAIS = , ESTEJAM NA MESMA LINHA***":^130}')
print('='*130)

# #3- importar cartelas geradas e nomes dos jogadores, e preservar numeros originais da cartela
cartelaJogador = [] #recebe cartelas lidas do arquivo txt
nomes = []
originalCartela = []
#ler cartelas
with open('cartelas_geradas.txt','r') as arquivo:
    for cart in arquivo:
        cartela = cart.split()
        importTemp = []
        #converter de string para inteiro
        for Int in range(10):
            importTemp.append(int(cartela[Int]))
        cartelaJogador.append(importTemp)
#ler nomes
with open('nomes.txt','r') as arquivo2:
    for nome in arquivo2:
        jnome = nome.split()
        nomes.append(jnome[0])

#preservar cartela original para quando for mostrar o vencedor
quantJogadores = len(cartelaJogador)
for oc in range(quantJogadores):
    originalCartela.append(formatarCartela(oc))

input('> APERTE "ENTER" PARA CONTINUAR... < ')
print('='*130)
print(f'IMPORTANDO CARTELAS...')
sleep(0.8)
print(f'IMPORTANDO COM SUCESSO!')
print('='*130)
sleep(0.8)

#inicializar algumas variaveis (essas variaveis são para o funcionamento da função imprimircartelas())
print4 = quantJogadores // 4 #variavel para imprimir cartelas na tela (quantas linhas de 4 cartelas serão mostradas)
printResto = quantJogadores % 4 #resto das cartelas

# #4- Mostar cartelas inicial de cada jogador
print('CADA JOGADOR FICOU COM AS SEGUINTES CARTELAS...')
print()
imprimircartelas() #função definida
print('>>>')
input('> APERTE "ENTER" PARA INICIAR AS RODADAS... < ')

# #5- execução do sorteio, informar numeros sorteados, informar último número sorteado, e jogadores por 1 número de vencer
rodada = 1
numRodadaanterior = 'Nenhum'
vencedor = False
faltando1 = False
nummerojasoerteado = []
jogquevemceram = []
# Enquanto não houver um vencedor faça o sorteio e informações...
while not vencedor:
    #sleep(0) #adicionar pausa entre cada rodada, tempo em ponto flutuante ex 0.5 para 500ms
    #Sortear o numero e remover ele da lista
    numeroAtual = globo[-1]
    nummerojasoerteado.append(numeroAtual)
    ordenar(nummerojasoerteado)
    globo.pop()

#Verificar em cada certela...
    #se numero esta na cartela atual, e remover se tiver
    for num in range(quantJogadores):
        if numeroAtual in cartelaJogador[num]:
            cartelaJogador[num].remove(numeroAtual)
    #se existe alguma cartela vazia (vencedor)
    for cart in range(quantJogadores):
        if len(cartelaJogador[cart]) == 0:
            vencedor = True
            jogquevemceram.append(nomes[cart])
    #se alguma cartela teve 9 numeros sorteados
    falta1 = []
    for cart in range(quantJogadores):
        if len(cartelaJogador[cart]) == 1:
            falta1.append(nomes[cart])
            faltando1 = True

#impimprimir a cada rodada as informações de:
    # Número da rodada
    print('~'*130)    
    print(f'\033[1;36m>>>>>>> RODADA {rodada}\033[m','='*112)
    print()
    #Sorteado atual e sorteado anteriormente
    print(f'\033[32mNÚMERO SORTEADO NESSA RODADA FOI:\033[m 《 \033[1;34m{numeroAtual}\033[m 》', ' '*42, f'\033[33mNÚMERO SORTEADO NA RODADA ANTERIOR:\033[m 《 \033[1;34m{numRodadaanterior}\033[m 》')
    print()
    
    #Números já sorteados
    print('\033[35mJÁ SORTEADOS:\033[m')
    print('>>> ',end='')
    cont = 1
    for ns in nummerojasoerteado:
        cont +=1
        print(f' {ns}',end=' ▴')
        if cont % 26 == 0:
            print()
    print()
    print('.'*130)
    
    #Falta 1 para bingo
    if faltando1 and vencedor == False:
        print()
        print('\033[31m!!! JOGADORES POR UM NÚMERO DE FAZER BINGO !!! → \033[m',end='')
        for nm in falta1:
            print(f'> {nm} <', end=' ')
        print()
    print()
    
    #cartelas dos jogadores
    print('CARTELAS:')
    print()
    ordenarCartela()
    imprimircartelas()
    numRodadaanterior = numeroAtual
    print('      ★'*17)
    print()
    rodada += 1
    numRodadaanterior = numeroAtual

# #6- Informar o vencedor do jogo
print('~'*130)
print('='*130)
print()
if len(jogquevemceram) == 1:
    print('\033[32mBINGOOOOO!!! TEMOS 1 VENCEDOR!!!\033[m')
    print()
    vencedornome = jogquevemceram[0]
    numvencedor = originalCartela[0]
    print('O VENCEDOR FOI:')
    print(f'> \033[34m{vencedornome}\033[m, E SEUS NÚMEROS FORAM >>> \033[33m{numvencedor}\033[m')
else:
    print(f'BINGOOOOO!!! TEMOS {len(jogquevemceram)} VENCEDORES!!!')
    print()
    print('OS VENCEDORES FORAM:')
    for venc in range(len(jogquevemceram)):
        print(f'> {jogquevemceram[venc]}, E SEUS NÚMEROS FORAM >>> {originalCartela[venc]}')

#Informar todos números que foram sorteados
print('.    '*20)
print(f'AO TOTAL FORAM SORTEADOS {rodada} NÚMEROS, E FORAM SORTEADOS OS SEGUINTES:')
print()
print('>>> ',end='')
cont = 1
for ns in nummerojasoerteado:
    cont +=1
    print(f' {ns}',end=' ▴')
    if cont % 26 == 0:
        print()
print()
print()
print('FIM!!!')
# FIM PROGRAMA PRINCIPAL
