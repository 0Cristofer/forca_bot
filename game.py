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

def menosVida(chat_id):
    bds.menosVida(chat_id)

def getVidas(chat_id):
    return bds.getVidas(chat_id)

class Jogo:
    def game(self, uId, uName, chat_id, text):
        rpl = []
        uIds = getuIds(chat_id)
        adm = getAdm(chat_id)
        palavra = getPeD(chat_id)[0]
        dica = getPeD(chat_id)[1]
        letras = getLetras(chat_id)
        mascara = getMascara(chat_id)
        if text.startswith('/'):
            if uId in uIds:
                if text.startswith('/cancelar') or text.startswith('/cancelar@forca_bot'):
                    if uId == adm:
                        str1 = 'O administrador cancelou o jogo' #implementar cancelamento por votacao
                        cleanGame(chat_id)
                        rpl = [str1]
                    else:
                        str1 = 'Voce nao tem autorizacao para cancelar o jogo\nApenas o administrador pode fazer isso'
                        rpl = [str1]
                elif text.startswith('/chutarletra'):
                    if len(text) == 14:
                        letra = text[13]
                        if letra in letras:
                            rpl = ['Essa letra ja foi chutada.\nUse /getletras para ver uma lista das letras chutadas!']
                        else:
                            locais = []
                            mscra = ''
                            newM = ''
                            rd = getRound(chat_id)
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
                                    setLetra(chat_id, letra)
                                    rpl.append(getMascara(chat_id))
                                else:
                                    rpl = ['Errou...']
                                    setLetra(chat_id, letra)
                                    menosVida(chat_id)
                                    if getVidas(chat_id) == 1:
                                        rpl.append('Voces tem apenas uma vida restante! Tentem descobrir a palavra ou aceitem a DERROTA!')
                                    elif getVidas(chat_id) == 0:
                                        rpl.append('***LOSERS!!!***')
                                        rpl.append('Creditos: Bot criado por @bcesarg6 e @cristoferoswald\nVersao Beta 1.0')
                                        cleanGame(chat_id)
                                    else:
                                        rpl.append('Restam '+str(getVidas(chat_id))+' Vidas!')
                            else:
                                nomes = getPlayers(chat_id)
                                rpl = ['Nao eh sua vez de jogar, vez de: '+nomes[rd]]
                    else:
                        rpl = ['Chute invalido!']
                elif text.startswith('/arriscarpalavra'):
                    arrisca = text[17:len(text)]
                    if arrisca == palavra:
                        rpl.append('***Parabens '+uName+' voce acertou a palavra secreta e ganhou o jogo!***')
                        rpl.append('Creditos: Bot criado por @bcesarg6 e @cristoferoswald\nVersao Beta 1.0')
                        cleanGame(chat_id)
                    else:
                        rpl.append('***ERROU!***\n'+uName+' arriscou a palavra e errou, que burro!')
                        rpl.append('***LOSERS!!!***')
                        rpl.append('Creditos: Bot criado por @bcesarg6 e @cristoferoswald\nVersao Beta 1.0')
                        cleanGame(chat_id)
                elif text.startswith('/getpalavra'):
                    rpl = ['Palavra secreta: '+mascara]
                elif text.startswith('/getdica'):
                    rpl = ['Dica: '+dica]
                elif text.startswith('/getletras'):
                    rpl = ['Letras chutadas:']
                    for i in range(len(letras)):
                        rpl.append(letras[i])
                elif text.startswith('/help') or text.startswith('/help@forca_bot'):
                    rpl.append('Jogo em andamento, instrucoes:\n/chutarletra para chutar uma letra\n/getpalavra para checar a palavra\n/getdica para ver a dica\n/getletras para ver a lista de letras')
                else:
                    rpl = ['Comando nao reconhecido no momento']
            else:
                rpl.append('Voce nao esta participando deste jogo '+uName+'\nlembre-se de entrar no proximo jogo se voce quer particupar')
        else:
            rpl = ['Nao eh um comando, comandos comecam com "/"']
        return rpl
