import bds

def updateList(palavras, dicas):
    bds.updateList(palavras, dicas)

def getPalavra(k):
    return bds.getPalavra(k)

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

def setMascara(chat_id, ped):
    return bds.setMascara(chat_id, ped)

class Jogo:
    def game(self, uId, uName, chat_id, text):
        palavras = ['teste','madalena','rodrigo schulz']
        dicas = ['Nome da variavel usado frequentemente','A professora complexa','Sem ressentimentos']
        rpl = []
        preState = getPreGame(chat_id)
        state = getInGame(chat_id)
        nomes = getPlayers(chat_id)
        uIds = getuIds(chat_id)
        adm = getAdm(chat_id)
        if text.startswith('/'):
            if text.startswith('/cancelar') or text.startswith('/cancelar@forca_bot'):
                if uId == adm:
                    str1 = 'Voce cancelou o jogo' #implementar cancelamento por votacao
                    setPreGame(chat_id, False)
                    setInGame(chat_id, False)
                    cleanPlayers(chat_id)
                    rpl = [str1]
                else:
                    str1 = 'Voce nao tem autorizacao para cancelar o jogo\nApenas o administrador pode fazer isso'
                    rpl = [str1]
            elif text.startswith('/help') or text.startswith('/help@forca_bot'):
                str1 = 'Existe um jogo em andamento\nUse este comando /help e irei te guiando!'
                rpl = [str1]
            else:
                rpl = ['Comando nao reconhecido no momento']
        else:
            rpl = ['Nao eh um comando, comandos comecam com "/"']
        return rpl
