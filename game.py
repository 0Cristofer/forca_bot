import bds

def getPeD(chat_id):
    return bds.getPeD(chat_id)

def setPreGame(chat_id, status):
    bds.setPreGame(chat_id, status)

def setInGame(chat_id, status):
    bds.setInGame(chat_id, status)

def getuIds(chat_id):
    return bds.getuIds(chat_id)

def getPlayers(chat_id):
    return bds.getPlayers(chat_id)

def getAdm(chat_id):
    return bds.getAdm(chat_id)

def setPeD(chat_id, ped):
    bds.PeD(chat_id, ped)

def setMascara(chat_id, mascara):
    bds.setMascara(chat_id, mascara)

def getMascara(chat_id):
    return bds.getMascara(chat_id)

def setLetra(chat_id, letra):
    bds.setLetra(chat_id, letra)

def getLetras(chat_id):
    return bds.getLetras(chat_id)

def setRound(chat_id, rd):
    bds.setRound(chat_id, rd)

def getRound(chat_id):
    return bds.getRound(chat_id)

def checkRound(chat_id, uId):
    rd = getRound(chat_id)
    uIds = getuIds(chat_id)
    if (uId == uIds[rd]):
        return True
    else:
        return False

def cleanGame(chat_id):
    bds.cleanGame(chat_id)

class Jogo:
    def game(self, uId, uName, chat_id, text):
        rpl = []
        nomes = getPlayers(chat_id)
        uIds = getuIds(chat_id)
        adm = getAdm(chat_id)
        palavra = getPeD(chat_id)[0]
        dica = getPeD(chat_id)[1]
        letras = getLetras(chat_id)
        mascara = getMascara(chat_id)
        if text.startswith('/'):
            if text.startswith('/cancelar') or text.startswith('/cancelar@forca_bot'):
                if uId == adm:
                    str1 = 'Voce cancelou o jogo' #implementar cancelamento por votacao
                    cleanGame(chat_id)
                    rpl = [str1]
                else:
                    str1 = 'Voce nao tem autorizacao para cancelar o jogo\nApenas o administrador pode fazer isso'
                    rpl = [str1]
            elif text.startswith('/chutarletra'):
                if len(text) == 14:
                    letra = text[13]
                    setLetra(chat_id, letra)
                    locais = []
                    mscra = ''
                    newM = ''
                    rd = getRound(chat_id)
                    print "chutar rd"+str(rd)
                    if checkRound(chat_id,uId):
                        nRd = rd+1
                        if nRd > (len(uIds)-1):
                            nRd = 0
                        setRound(chat_id, nRd)
                        if letra in palavra:
                            for i in range(len(palavra)):
                                if palavra[i] == letra:
                                    mscra = mscra+letra
                                else:
                                    mscra = mscra+'*'
                            for i in range(len(mascara)):
                                if (mascara[i] == '*') and (mscra[i] == '*'):
                                    newM = newM+'*'
                                elif mascara[i] == '*':
                                    newM = newM+mscra[i]
                                elif mscra[i] == '*':
                                    newM = newM+mascara[i]
                            setMascara(chat_id, newM)
                            rpl = ['Voce acertou!']
                            rpl.append(getMascara(chat_id))
                        else:
                            rpl = ['Errou...']
                    else:
                        rpl = ['Nao eh sua vez de jogar, eh a vez do: '+nomes[rd]]
                else:
                    rpl = ['Nao pode chutar mais que uma letra']
            elif text.startswith('/getpalavra'):
                rpl = ['A palavra ate agora esta assim: '+mascara]
            elif text.startswith('/getdica'):
                rpl = ['A dica eh: '+dica]
            elif text.startswith('/getletras'):
                rpl = ['As letras ate agora foram:']
                for i in range(len(letras)):
                    rpl.append(letras[i])
            elif text.startswith('/help') or text.startswith('/help@forca_bot'):
                str1 = 'Existe um jogo em andamento\nUse /chutarletra para tentar!'
                rpl = [str1]
            else:
                rpl = ['Comando nao reconhecido no momento']
        else:
            rpl = ['Nao eh um comando, comandos comecam com "/"']
        return rpl
