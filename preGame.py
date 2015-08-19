#Contem a logica do jogo

#Importa os BDs
import bds

#Importa funcao que randomiza um int
from random import randint, shuffle

#Pega as funcoes dos BDs para poderem ser utilizadas nesse arquivo
def updateList(matriz):
    bds.updateList(matriz)

def getNPeD(rnd1, rnd2):
    return bds.getNPeD(rnd1, rnd2)

def setGame(chat_id):
    bds.setGame(chat_id)

def setPreGame(chat_id, status):
    bds.setPreGame(chat_id, status)

def getPreGame(chat_id):
    return bds.getPreGame(chat_id)

def setInGame(chat_id, status):
    bds.setInGame(chat_id, status)

def getInGame(chat_id):
    return bds.getInGame(chat_id)

def addPlayer(chat_id, uId, uName):
    bds.addPlayer(chat_id, uId, uName)
    bds.addPlayerRank(chat_id, uName)

def setAdm(chat_id, uId):
    bds.setAdm(chat_id, uId)

def getuIds(chat_id):
    return bds.getuIds(chat_id)

def getPlayers(chat_id):
    return bds.getPlayers(chat_id)

def getAdm(chat_id):
    return bds.getAdm(chat_id)

def setPeD(chat_id, ped):
    bds.setPeD(chat_id, ped)

def setMascara(chat_id, mascara):
    bds.setMascara(chat_id, mascara)

def getMascara(chat_id):
    return bds.getMascara(chat_id)

def setLetra(chat_id, letra):
    bds.setLetra(chat_id, letra)

def getLetras(chat_id):
    return bds.getLetras(chat_id, letra)

def setRound(chat_id, rd):
    bds.setRound(chat_id, rd)

def getRound(chat_id):
    return bds.getRound(chat_id)

def setVidas(chat_id, modVida):
    bds.setVidas(chat_id, modVida)

def getVidas(chat_id):
    return bds.getVidas(chat_id)

def cleanGame(chat_id):
    bds.cleanGame(chat_id)

def getRank(chat_id):
    return bds.getRank(chat_id)

def setShuffle(chat_id, nomes, uIds):
    bds.setShuffle(chat_id, nomes, uIds)


#Classe que contem toda logica do jogo (a ser melhor comentada)

class PreJogo:

    def preGame(self, uId, uName, chat_id, text):
        text = text.lower()
        matriz = [
            ['Animais', 'macaco', 'elefante','zebra','papagaio','andorinha','golfinho','gorila','tubarao','lobo','ornitorrinco','cavalo','humano'],
            ['Comidas', 'banana','miojo','cachorro quente','lasanha','salada de frutas','carambola','x-salada','frango frito','batata frita','ketchup','chocolate','morango','strogonoff','arroz e feijao','batata doce','pizza',''],
            ['Proficao', 'professor', 'zelador','prostituta','tia do Xerox','medico','marceneiro','contrabandista','traficante','designer','game developer','dublador','escritor'],
            ['Relacionado a Computadores/Internet/Programacao', 'programador','compilador','servidor','monitor','algoritmo','netflix','orkut','instagram','tumblr','twitter','rede neural','google','photoshop','wolfram alpha','python','java','framework','ruby','javascript','latex'],
            ['Relacionado a UEM', 'rodrigo Schulz','erica puta','tio elvio','restaurante universitario','biblioteca central','hackerspace','caccom'],
            ['Voce deu azar e nao tem dica!','chaves','parafuseta','rebimboca','kibe','penal','orkut','android','telegram','whatsapp','ornitorrinco','skyrim','dota2','lolzinho','pipa','voce nao vai acertar essa','sim soh de zoas'],
            ['Heroi ou vilao do mundo das HQ/cinema (DC e Marvel)','batman','flash','mulher maravilha','pinguim','super Homem','lanterna verde','duende verde','homem aranha','thor','hulk','homem de ferro','homem formiga','tocha humana','o coisa','viuva negra','arqueiro verde','Groot','Rocket Raccoon','Magneto','Wolverine'],
            ['Videogames e games em geral!','the legend of zelda','super mario','counter strike','nintendo wii','super nintendo','playstation','steam','defense of the ancients','league of legends','final fantasy','doneky kong','angry birds','fallout','bioshock','tetris','the elders scroll','minecraft','call of duty','battlefield'],
            ['Palavras ou nomes relacionados a TV e/ou Cinema!','how i met your mother','sense8','netflix','american Beauty','donnie Darko','esqueceram de mim','the sixth sense','the shining','titanic','todo mundo odeia o cris','agostinho carrara','chapeleiro maluco','alice no pais das maravilhas','harry potter','hora da aventura','bob esponja'],
            ['Paises', 'brasil', 'estados Unidos', 'alemanha', 'japao', 'coreia do Sul', 'africa do sul', 'holanda', 'argentina', 'espanha', 'chile', 'equador', 'canada', 'singapura', 'india', 'emirados Arabes', 'italia', 'inglaterra', 'austria', 'grecia', 'Republica Checa']
        ]
        rpl = []
        preState = getPreGame(chat_id)
        if text.startswith('/'):
                #Bloco Inicial================================================
            if preState == False:
                if text.startswith('/novojogo') or text.startswith('/novojogo@forca_bot'):
                    setGame(chat_id)
                    rpl.append('Comecando um novo jogo! Voce sera o administrador dessa rodada '+uName+'\nVamos comecar definindo os jogadores\nQuem quiser participar dessa rodada envie o comando /entrar :D' )
                    rpl.append('Para fechar o grupo de participantes envie o comando /fecharjogo Administador '+uName)
                    setPreGame(chat_id, True)
                    setAdm(chat_id, uId)
                    addPlayer(chat_id, uId, uName)
                    updateList(matriz)
                    setRound(chat_id, 0)
                elif text.startswith('/help') or text.startswith('/help@forca_bot'):
                    str1 = 'Nao existe nenhum jogo em andamento, utilize o comando /novojogo para comecar e irei te guiando :)\nCaso deseje ver o ranking use /getrank'
                    rpl = [str1]
                elif text.startswith('/cancelar') or text.startswith('/cancelar@forca_bot'):
                    str1 = 'Nao existe jogo no momento, envie o comando /help caso precise de ajuda!'
                    rpl = [str1]
                elif text.startswith('/getrank') or text.startswith('/getrank@forca_bot'):
                    rank = getRank(chat_id)
                    rpl.append('***RANKING***')
                    str1 = 'NOME - SCORE\n'
                    for i in range(len(rank)):
                        str1 = str1 + rank[i][0]+' - '+rank[i][1]+'\n'
                    rpl.append(str1)
                else:
                    str1 = 'Comando nao reconhecido no momento'
                    rpl = [str1]
            #Fim do bloco incial /// Comeco do bloco PreGame ===================================
            else:
                if text.startswith('/novojogo') or text.startswith('/novojogo@forca_bot'):
                    str1 = 'Existe um jogo em modo de entrada, se quiser entrar digite /entrar'
                    rpl = [str1]
                elif text.startswith('/entrar') or text.startswith('/entrar@forca_bot'):
                    uIds = getuIds(chat_id)
                    if uId in uIds:
                        str1 = 'Voce ja participa desse jogo'
                        rpl = [str1]
                    else:
                        addPlayer(chat_id, uId, uName)
                        str1 = 'Certo, '+uName+' voce vai participar desta rodada'
                        rpl = [str1]
                elif text.startswith('/cancelar') or text.startswith('/cancelar@forca_bot'):
                    adm = getAdm(chat_id)
                    if uId == adm:
                        str1 = 'O Administador cancelou o jogo!' #implementar cancelamento por votacao
                        cleanGame(chat_id)
                        rpl = [str1]
                    else:
                        str1 = 'Voce nao tem autorizacao para fechar o jogo\nApenas o Administrador pode fazer isso'
                        rpl = [str1]
                elif text.startswith('/fecharjogo') or text.startswith('/fecharjogo@forca_bot'):
                    adm = getAdm(chat_id)
                    if uId == adm:
                        setInGame(chat_id,True)
                        leng = len(matriz)-1
                        rnd1 = randint(0,leng)
                        leng = len(matriz[rnd1])-1
                        rnd2 = randint(1, leng)
                        ped = getNPeD(rnd1, rnd2)
                        ped[1] = ped[1].lower()
                        setPeD(chat_id, ped)
                        mascara = '*'*(len(ped[0]))
                        lMascara = list(mascara)
                        for i in range(len(mascara)):
                            if ped[0][i]== ' ':
                                lMascara[i] = ' '
                            if ped[0][i]== '-':
                                lMascara[i] = '-'
                        mascara = "".join(lMascara)
                        setMascara(chat_id, mascara)
                        nomes = getPlayers(chat_id)
                        modVida = len(ped[0])/5 if len(ped[0]) > 5 else 0
                        modVida += len(nomes)-3 if len(nomes) > 4 else 0
                        modVida = 9 if modVida > 9 else modVida
                        setVidas(chat_id, modVida)
                        vidas = str(getVidas(chat_id))+' VIDAS'
                        #Randomizar a lista de participantes
                        nomes = getPlayers(chat_id)
                        uIds = getuIds(chat_id)
                        # Given list1 and list2
                        nomes_shuf = []
                        uIds_shuf = []
                        index_shuf = range(len(nomes))
                        shuffle(index_shuf)
                        for i in index_shuf:
                            nomes_shuf.append(nomes[i])
                            uIds_shuf.append(uIds[i])
                        str1 = 'Grupo de participantes fechados! Voces jogarao nesta ordem:\n\n'
                        nomes = nomes_shuf
                        uIds = uIds_shuf
                        setShuffle(chat_id, nomes, uIds)
                        for i in range(0,len(nomes)):
                            str1 = str1+nomes[i]+'\n'
                        rpl.append('O jogo vai comecar agora! Instrucoes:\nUtilize o comando /chutarletra para chutar letras, quando estiver pronto para arriscar utilize o comando /arriscarpalavra Mas cuidado, se voce errar perde o jogo!\n*** '+vidas+' ***')
                        rpl.append('Palavra secreta: '+mascara)
                        rpl.append('Dica: '+ped[1])
                        rpl.append(str1)
                    else:
                        str1 = 'Voce nao tem autorizacao para cancelar o jogo\nApenas o administrador pode fazer isso'
                        rpl = [str1]
                elif text.startswith('/help') or text.startswith('/help@forca_bot'):
                    str1 = 'Nesse momento a partida esta aberta para entrada de novos jogadores\nEnvie o comando /entrar para participar'
                    rpl = [str1]
                else:
                    str1 = 'Comando nao reconhecido no momento'
                    rpl = [str1]
        else:
            rpl = ['Nao eh um comando, lembre se que comandos comecam com /']
        return rpl
