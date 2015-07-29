#imports
import main
import dbs
from random import randint
from google.appengine.ext import ndb

def updateList(palavras, dicas):
    dbs.updateList(palavras, dicas)

def getPalavra(k):
    return dbs.getPalavra(k)

def setPreGame(chat_id, status):
    dbs.setPreGame(chat_id, status)

def getPreGame(chat_id):
    return dbs.getPreGame(chat_id)

def setInGame(chat_id, status):
    dbs.setInGame(chat_id, status)

def getInGame(chat_id):
    return dbs.getInGame(chat_id)

def addPlayer(chat_id, uId, uName):
    dbs.addPlayer(chat_id, uId, uName)

def getuIds(chat_id):
    return dbs.getuIds(chat_id)

def getPlayers(chat_id):
    return dbs.getPlayers(chat_id)

def cleanPlayers(chat_id):
    dbs.cleanPlayers(chat_id)

def setFirst(chat_id, status):
    dbs.setF(chat_id)

def getFirst(chat_id):
    return dbs.getFirst(chat_id)

class Jogo:
    updateList(dbs.palavras, dbs.dicas)
    palavra = getPalavra(randint(0,2))

    """def getF(self, chat_id):
        return getFirst(chat_id)

    def setF(self, chat_id, status):
        setFirst(chat_id, status)
        addPlayer(chat_id, 'uId', 'uName')"""

    def comandos(self, uId, uName, chat_id, text):
        rpl = []
        preState = getPreGame(chat_id)
        state = getInGame(chat_id)
        nomes = getPlayers(chat_id)
        uIds = getuIds(chat_id)
        print uId
        #print uIds[1]
        if text.startswith('/'):
            if state == False:
                if preState == False:
                    if text.startswith('/novojogo') or text.startswith('/novojogo@forca_bot'):
                        str1 = 'Comecando um novo jogo! Voce sera o administrador dessa rodada '+uName
                        setPreGame(chat_id,True)
                        str2 = 'Vamos comecar definindo os jogadores\nQuem quiser participar dessa rodada envie um /entrar :D'
                        str3 = 'Para fechar o grupo de participantes mande um /fechar Administador'
                        addPlayer(chat_id, uId, uName)
                        rpl = [str1, str2, str3]
                    elif text.startswith('/help') or text.startswith('/help@forca_bot'):
                        str1 = 'Nao existe jogo em andamento, utilize /novojogo para comecar e irei te guiando :)'
                        rpl = [str1]
                    else:
                        str1 = 'Comando nao reconhecido no momento'
                        rpl = [str1]
                else:
                    if text.startswith('/novojogo') or text.startswith('/novojogo@forca_bot'):
                        str1 = 'Existe um jogo em modo de entrada, se quiser entrar digite /entrar'
                        rpl = [str1]
                    elif text.startswith('/entrar') or text.startswith('/entrar@forca_bot'):
                        """if uId in uIds:
                            str1 = 'Voce ja participa desse jogo'
                            rpl = [str1]
                        else:
                            addPlayer(chat_id, uId, uName)
                            str1 = 'Certo, '+uName+' voce vai participar desta rodada'
                            rpl = [str1]"""
                        for i in range(len(uIds)):
                            if uIds[i] == uId:
                                rpl.append(uId)
                                print uIds[i]
                    elif text.startswith('/fecharjogo') or text.startswith('/fecharjogo@forca_bot'):
                        if uId == uIds[1]:
                            str1 = 'Grupo de participantes fechados! Jogarao nesta rodada:'
                            rpl = [str1]
                            for i in range(1,len(nomes)):
                                rpl.append(nomes[i])
                            setInGame(chat_id,True)
                            rpl.append('O jogo vai comecar agora!') #Mudar talvez
                        else:
                            str1 = 'Voce nao tem autorizacao para fechar o jogo\nApenas o administrador pode fazer isso'
                            rpl = [str1]
                    elif text.startswith('/cancelar') or text.startswith('/cancelar@forca_bot'):
                        """if uId == uIds[1]:
                            str1 = 'Voce cancelou o jogo' #implementar cancelamento por votacao
                            setPreGame(chat_id, False)
                            setInGame(chat_id, False)
                            cleanPlayers(chat_id)
                            rpl = [str1]
                        else:
                            str1 = 'Voce nao tem autorizacao para cancelar o jogo\nApenas o administrador pode fazer isso'
                            rpl = [str1]"""
                        setPreGame(chat_id, False)
                        setInGame(chat_id, False)
                        cleanPlayers(chat_id)
                    elif text.startswith('/help') or text.startswith('/help@forca_bot'):
                        str1 = 'Nesse momento os a partida esta aberta para entrada de novos jogadores\nUtilize /entrar para participar'
                        rpl = [str1]
                    else:
                        str1 = 'Comando nao reconhecido no momento'
                        rpl = [str1]
            else:
                if text.startswith('/cancelar') or text.startswith('/cancelar@forca_bot'):
                    """if uId == uIds[1]:
                        str1 = 'Voce cancelou o jogo' #implementar cancelamento por votacao
                        setPreGame(chat_id, False)
                        setInGame(chat_id, False)
                        cleanPlayers(chat_id)
                        rpl = [str1]
                    else:
                        str1 = 'Voce nao tem autorizacao para cancelar o jogo\nApenas o administrador pode fazer isso'
                        rpl = [str1]"""
                    setPreGame(chat_id, False)
                    setInGame(chat_id, False)
                    cleanPlayers(chat_id)
                elif text.startswith('/help') or text.startswith('/help@forca_bot'):
                    str1 = 'Existe um jogo em andamento\nUse este comando /help e irei te guiando!'
                    rpl = [str1]
                else:
                    rpl = ['Comando nao reconhecido no momento']
        else:
            rpl = ['Nao eh um comando, lembre se que comandos comecam com /']
        return rpl
