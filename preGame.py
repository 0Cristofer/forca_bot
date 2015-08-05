#Contem a logica do jogo

#Importa os BDs
import bds

#Importa funcao que randomiza um int
from random import randint

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

def cleanGame(chat_id):
    bds.cleanGame(chat_id)

#Classe que contem toda logica do jogo (a ser melhor comentada)

class PreJogo:

    def preGame(self, uId, uName, chat_id, text):
        text = text.lower()
        animais = ['Animal', 'macaco', 'elefante']
        comidas = ['Comida', 'banana']
        proficoes = ['Proficao', 'professor', 'zelador']
        zueracc = ['Relacionado a CC', 'programador']
        zuerauem = ['Relacionado a UEM', 'rodrigo Schulz']
        matriz = [animais, comidas, proficoes, zueracc, zuerauem]
        rpl = []
        preState = getPreGame(chat_id)
        if text.startswith('/'):
                #Bloco Inicial================================================
            if preState == False:
                if text.startswith('/novojogo') or text.startswith('/novojogo@forca_bot'):
                    setGame(chat_id)
                    rpl.append('Comecando um novo jogo! Voce sera o administrador dessa rodada '+uName)
                    rpl.append('Vamos comecar definindo os jogadores\nQuem quiser participar dessa rodada envie o comando /entrar :D')
                    rpl.append('Para fechar o grupo de participantes envie o comando /fecharjogo Administador '+uName)
                    setPreGame(chat_id, True)
                    setAdm(chat_id, uId)
                    addPlayer(chat_id, uId, uName)
                    updateList(matriz)
                    setRound(chat_id, 0)
                elif text.startswith('/help') or text.startswith('/help@forca_bot'):
                    str1 = 'Nao existe jogo em andamento, utilize o comando /novojogo para comecar e irei te guiando :)'
                    rpl = [str1]
                elif text.startswith('/cancelar') or text.startswith('/cancelar@forca_bot'):
                    str1 = 'Nao existe jogo no momento, envie o comando /help caso precise de ajuda!'
                    rpl = [str1]
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
                    nomes = getPlayers(chat_id)
                    if uId == adm:
                        str1 = 'Grupo de participantes fechados! Jogarao nesta rodada:'
                        rpl = [str1]
                        for i in range(0,len(nomes)):
                            rpl.append(nomes[i])
                        setInGame(chat_id,True)
                        rpl.append('O jogo vai comecar agora! Instrucoes:\nUtilize o comando /chutarletra para chutar letras, quando estiver pronto para arriscar utilize o comando /arriscarpalavra Mas cuidado, se voce errar perde o jogo!\n*** 6 VIDAS ***')
                        leng = len(matriz)-1
                        rnd1 = randint(0,leng)
                        leng = len(matriz[rnd1])-1
                        rnd2 = randint(1, leng)
                        ped = getNPeD(rnd1, rnd2)
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
                        rpl.append('Palavra secreta: '+mascara)
                        rpl.append('Dica: '+ped[1])
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
