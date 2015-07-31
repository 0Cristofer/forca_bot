#Contem a logica do jogo

#Importa os BDs
import bds

#Importa funcao que randomiza um int
from random import randint

#Pega as funcoes dos BDs para poderem ser utilizadas nesse arquivo
def updateList(palavras, dicas):
    bds.updateList(palavras, dicas)

def getNPeD(k):
    return bds.getNPeD(k)

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

def cleanPlayers(chat_id):
    bds.cleanPlayers(chat_id)

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

def cleanLetras(chat_id):
    bds.cleanLetras(chat_id)

#Classe que contem toda logica do jogo (a ser melhor comentada)

class PreJogo:

    def preGame(self, uId, uName, chat_id, text):
        palavras = ['teste','madalena','rodrigo schulz', 'lolzinho', 'computador', 'ciencia da computacao']
        dicas = ['Nome da variavel usado frequentemente','A professora complexa','Sem ressentimentos', 'jogo do mal', 'bagulho que te faz ficar sentado', 'curso op']
        rpl = []
        preState = getPreGame(chat_id)
        state = getInGame(chat_id)
        nomes = getPlayers(chat_id)
        uIds = getuIds(chat_id)
        adm = getAdm(chat_id)
        if text.startswith('/'):
                #Bloco Inicial================================================
            if preState == False:
                if text.startswith('/novojogo') or text.startswith('/novojogo@forca_bot'):
                    str1 = 'Comecando um novo jogo! Voce sera o administrador dessa rodada '+uName
                    setPreGame(chat_id,True)
                    str2 = 'Vamos comecar definindo os jogadores\nQuem quiser participar dessa rodada envie um /entrar :D'
                    str3 = 'Para fechar o grupo de participantes mande um /fecharjogo Administador'
                    cleanPlayers(chat_id)
                    setAdm(chat_id, uId)
                    addPlayer(chat_id, uId, uName)
                    updateList(palavras,dicas)
                    cleanLetras(chat_id)
                    rpl = [str1, str2, str3]
                elif text.startswith('/help') or text.startswith('/help@forca_bot'):
                    str1 = 'Nao existe jogo em andamento, utilize /novojogo para comecar e irei te guiando :)'
                    rpl = [str1]
                elif text.startswith('/cancelar') or text.startswith('/cancelar@forca_bot'):
                    str1 = 'Nao existe jogo no momento'
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
                    if uId in uIds:
                        str1 = 'Voce ja participa desse jogo'
                        rpl = [str1]
                    else:
                        addPlayer(chat_id, uId, uName)
                        str1 = 'Certo, '+uName+' voce vai participar desta rodada'
                        rpl = [str1]
                elif text.startswith('/cancelar') or text.startswith('/cancelar@forca_bot'):
                    if uId == adm:
                        str1 = 'Voce cancelou o jogo' #implementar cancelamento por votacao
                        setPreGame(chat_id, False)
                        setInGame(chat_id, False)
                        cleanPlayers(chat_id)
                        rpl = [str1]
                    else:
                        str1 = 'Voce nao tem autorizacao para fechar o jogo\nApenas o administrador pode fazer isso'
                        rpl = [str1]
                elif text.startswith('/fecharjogo') or text.startswith('/fecharjogo@forca_bot'):
                    if uId == adm:
                        str1 = 'Grupo de participantes fechados! Jogarao nesta rodada:'
                        rpl = [str1]
                        for i in range(0,len(nomes)):
                            rpl.append(nomes[i])
                        setInGame(chat_id,True)
                        rpl.append('O jogo vai comecar agora!') #Mudar talvez
                        ped = getNPeD(randint(0,5))
                        setPeD(chat_id, ped)
                        mascara = '*'*(len(ped[0]))
                        setMascara(chat_id, mascara)
                        rpl.append('A palavra eh: '+mascara)
                        rpl.append('A dica eh: '+ped[1])
                    else:
                        str1 = 'Voce nao tem autorizacao para cancelar o jogo\nApenas o administrador pode fazer isso'
                        rpl = [str1]
                elif text.startswith('/help') or text.startswith('/help@forca_bot'):
                    str1 = 'Nesse momento os a partida esta aberta para entrada de novos jogadores\nUtilize /entrar para participar'
                    rpl = [str1]
                else:
                    str1 = 'Comando nao reconhecido no momento'
                    rpl = [str1]
        else:
            rpl = ['Nao eh um comando, lembre se que comandos comecam com /']
        return rpl
