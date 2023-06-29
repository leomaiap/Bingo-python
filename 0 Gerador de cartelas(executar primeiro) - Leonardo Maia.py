# TCC00308 - PROGRAMAÇÃO DE COMPUTADORES I  →  TRABALHO BINGO ELETRÔNICO
# Aluno: Leonardo Maia Pereira        Matrícula: 120031027
# Turma: B1 - 20.1

#BIBLIOTECAS
from random import randint, shuffle
from time import sleep

#FUNÇÕES
def ordenar(lista):
    for i in range(len(lista)-1):
        indiceatual = i+1
        menorvalor = i
        while indiceatual < len(lista):
            if lista[indiceatual] < lista[menorvalor]:
                menorvalor = indiceatual
            indiceatual += 1
        lista[i], lista[menorvalor] = lista[menorvalor], lista[i]

def colocarnotxt(lista):
    with open('cartelas_geradas.txt','a') as arquivo:
        for valores in lista:
            arquivo.write(str(valores) + ' ')
        arquivo.write('\n')


# =PROGRAMA PRINCIPAL=

# Criar(caso não exista no disco) e/ou limpar e sobrescrever arquivo de texto no armazenamento
open('cartelas_geradas.txt','w')

# #1- Boas vindas ao usuário, 
print('='*130)
print(f'{"SEJA BEM-VINDO AO GERADOR DE CARTELAS DO BINGO ELETRÔNICO!!!":^130}')
print(F'{"AQUI SERÃO SORTEADOS AS CARTELAS PARA O JOGO, ESCOLHA A QUANTIDADE DE JOGADORES PARTICIPANTES":^130}')
print('='*130)

# #2- pedir a quantidade de participantes ao usuário
# uma validação de dados para o usuário não inserir dados de forma incorreta
while True:
    numeroJogadores = int(input('DIGITE O NÚMERO DE JOGADORES: (4 ATÉ 80): >>> ')) #ler quantidade de jogadores
    while True:
        if numeroJogadores < 4 or numeroJogadores> 80:
            numeroJogadores = int(input('QUANTIDADE INVÁLIDA: (4 ATÉ 80): >>> ')) 
        else:
            break
    continuar = str(input(f'VOCÊ ESCOLHEU {numeroJogadores} JOGADORES. DESEJA CONTINUAR? [S/N]: >>> ')).lower().strip()
    while True:
        if continuar in 'sn':
            break
        else:
            continuar = str(input(f'VOCÊ ESCOLHEU {numeroJogadores} JOGADORES. DESEJA CONTINUAR? [S/N]: >>> ')).lower().strip()
    if continuar in 's':
        break

print('='*130)
print('GERANDO CARTELAS...')
print('='*130)

# #3- Sortear a quantidades de cartelas escolhidas
historicoCartelas = []
tot_cartelas = 0
cartelaTemp = []
cartelacont = 0
#enquanto não forem geradas a quantidade solicitada continue gerando cartelas
while tot_cartelas < numeroJogadores:
    while True:
        numCartela = randint(0,99)
        if numCartela not in cartelaTemp:
            cartelaTemp.append(numCartela)
            cartelacont += 1
        if cartelacont == 10:
            break
    ordenar(cartelaTemp) #função definida
    
    #verificação se cartela é repetida no jogo
    if len(historicoCartelas) < 1:
        tot_cartelas += 1
        historicoCartelas.append(cartelaTemp[:])
        colocarnotxt(cartelaTemp) #função definida
    else:
        cartelaInedita = True    
        for cart in range(len(historicoCartelas)):
            if historicoCartelas[cart] == cartelaTemp:
                cartelaInedita = False
                break
        if cartelaInedita:
            tot_cartelas += 1
            historicoCartelas.append(cartelaTemp[:])
            colocarnotxt(cartelaTemp) #função definida
    cartelaTemp = []
    cartelacont = 0
    
#Feedback para o usuário de que a ação foi concluída 
sleep(0.3)
print('CARTELAS GERADAS...')
print('='*130)

#Nomear as cartelas...
nomes = ['HELENA', 'ALICE', 'LAURA', 'MANUELA', 'VALENTINA', 'SOPHIA', 'ISABELLA', 'HELOISA', 'LUIZA', 'JULIA', 'LORENA', 'LIVIA', 'CECILIA', 'ELOA', 'GIOVANNA',
'MARIANA', 'LARA', 'BEATRIZ', 'ANTONELLA', 'EMANUELLY', 'ISADORA', 'ANA CLARA', 'MELISSA', 'ANA LUIZA', 'ANA JULIA', 'ESTHER', 'LAVINIA', 'GABI', 'SARAH', 'ELISA',
'LIZ', 'YASMIN', 'ISABELLY', 'ALICIA', 'CLARA', 'ISIS', 'REBECA', 'RAFAELA', 'MARINA', 'ANA LAURA', 'AGATHA', 'VITOR', 'ENRICO', 'DOUGLAS', 'CAIO', 'VINÍCIUS', 'HENRY',
'AUGUSTO', 'RAVI', 'FRANCISCO', 'OTAVIO', 'THOMAS', 'ICARO', 'THEODORO', 'YAN', 'NATHAN', 'ERICK', 'BRENO', 'LEONARDO', 'MARTIN', 'MATTEO', 'OLIVER', 'RYAN', 'RAUL',
'LUAN', 'TIAGO', 'MATHIAS', 'DAVI LUIZ', 'DERICK', 'CARLOS', 'RODRIGO', 'BRUNO', 'YAGO', 'JOSE', 'HUGO', 'OTTO', 'JOHN', 'DIOGO', 'MIGUEL', 'ARTHUR', 'HEITOR','BERNARDO']
#embaralhar nomes
shuffle(nomes)
# Criar(caso não exista no disco) e/ou limpar e sobrescrever arquivo de texto no armazenamento
open('nomes.txt','w')
with open('nomes.txt','a') as arquivo:
        for nm in range(numeroJogadores):
            arquivo.write(str(nomes[nm]) + ' \n')

print('ARMAZENANDO CARTELAS...  ', end='')
sleep(0.3)
porcentagem = ['5%','20%','36%','65%','78%', '85%', '99%', '100%']
for percent in porcentagem:
    print(percent, end=' ', flush=True)
    sleep(0.12)
print()
print('='*130)
sleep(0.2)
print('CARTELAS ARMAZENADAS COM SUCESSO!!! FIM!!!')
print('='*130)
#FIM DO PROGRAMA
