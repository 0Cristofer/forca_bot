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

def rmPlayer(chat_id, rd):
    return bds.rmPlayer(chat_id, rd)

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
    bds.updateRank(chat_id)

def menosVida(chat_id):
    bds.menosVida(chat_id)

def getVidas(chat_id):
    return bds.getVidas(chat_id)

def addScore(chat_id, uName, score):
    bds.addScore(chat_id, uName, score)

def getRank(chat_id):
    rank = bds.getRank(chat_id)
    str1 = 'NOME - SCORE\n'
    for i in range(len(rank)):
        str1 = str1 + str(rank[i][0])+' - '+str(rank[i][1])+'\n'
    return str1

def getVidasInit(chat_id):
    return bds.getVidasInit(chat_id)

class Jogo:
    def game(self, uId, uName, chat_id, text):
        emoji_heart = (u'\u2764\ufe0f').encode('utf-8')
        emoji_heartb = (u'\U0001f494').encode('utf-8')
        emoji_confetti = (u'\U0001f389').encode('utf-8')
        emoji_claps = (u'\U0001f44f\U0001f3fc').encode('utf-8')
        emoji_triste = (u'\U0001f614').encode('utf-8')
        emoji_poop = (u'\U0001f4a9').encode('utf-8')
        emoji_lua = (u'\U0001f31a').encode('utf-8')
        emoji_negativo = (u'\U0001f44e\U0001f3fb').encode('utf-8')
        emoji_bug = (u'\U0001f41e').encode('utf-8')
        emoji_point = (u'\U0001f448\U0001f3fb').encode('utf-8')
        text = str(text.lower().encode('utf-8'))
        uName = str(uName.encode('utf-8'))
        rpl = []
        uIds = getuIds(chat_id)
        adm = getAdm(chat_id)
        palavra = getPeD(chat_id)[0]
        dica = getPeD(chat_id)[1]
        letras = getLetras(chat_id)
        mascara = getMascara(chat_id)
        rd = getRound(chat_id)
        vida_init = getVidasInit(chat_id)
        if text.startswith('/'):
            if uId in uIds:
                if text.startswith('/palavra'):
                    rpl = ['Palavra secreta: '+str(mascara)]
                elif text.startswith('/dica'):
                    rpl = ['Dica: '+str(dica)]
                elif text.startswith('/letras'):
                    rpl = ['Letras chutadas:']
                    rpll = ' '
                    for i in range(len(letras)):
                        rpll= rpll+str(letras[i])+' '
                    rpl.append(rpll)
                elif text.startswith('/rank') or text.startswith('/rank@forca_bot'):
                    rpl.append('***RANKING***')
                    rank = getRank(chat_id)
                    rpl.append(rank)
                elif text.startswith('/cancelar') or text.startswith('/cancelar@forca_bot'):
                    if uId == adm:
                        str1 = 'O administrador cancelou o jogo'
                        cleanGame(chat_id)
                        rpl = [str1]
                    else:
                        str1 = 'Você não tem autorização para cancelar o jogo\nApenas o administrador pode fazer isso'
                        rpl = [str1]
                elif text.startswith('/help') or text.startswith('/ajuda'):
                    rpl.append('Jogo em andamento, instruções:\n/chutar para chutar uma letra\n/getpalavra para checar a palavra\n/getdica para ver a dica\n/getletras para ver a lista de letras')
                elif checkRound(chat_id, uId):
                    if text.startswith('/chutar'):
                        if len(text) == 9:
                            letra = text[8]
                            if letra in letras:
                                rpl = ['Essa letra já foi chutada.\nUse /getletras para ver uma lista das letras chutadas!']
                            else:
                                locais = []
                                mscra = ''
                                newM = ''
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
                                    rpl = ['Voce acertou!'+emoji_claps]
                                    addScore(chat_id,uName, 2)
                                    setLetra(chat_id, letra)
                                    rpl.append(getMascara(chat_id))
                                    nomes = getPlayers(chat_id)
                                    auxx = 0 if rd+1 > (len(nomes)-1) else rd + 1
                                    rpl.append('Agora é a vez de: '+str(nomes[auxx])+emoji_point)
                                else:
                                    rpl = ['Errou...'+emoji_triste]
                                    setLetra(chat_id, letra)
                                    menosVida(chat_id)
                                    nomes = getPlayers(chat_id)
                                    auxx = 0 if rd+1 > (len(nomes)-1) else rd + 1
                                    if getVidas(chat_id) == 1:
                                        rpl.append('Vocês têm apenas uma vida restante! Tentem descobrir a palavra ou aceitem a DERROTA! '+emoji_lua)
                                    elif getVidas(chat_id) == 0:
                                        rpl.append(emoji_poop+'LOSERS'+emoji_poop)
                                        rpl.append('O jogo acabou, utilize /novojogo para começar um novo')
                                        rpl.append('Creditos: Bot criado por @bcesarg6 e @cristoferoswald\nVersão Beta 1.7'+emoji_bug)
                                        cleanGame(chat_id)
                                    else:
                                        aux = vida_init - getVidas(chat_id)
                                        str1= ''
                                        for i in range(getVidasInit(chat_id)-aux):
                                            str1 = str1 + emoji_heart
                                        for i in range(aux):
                                            str1 = str1 + emoji_heartb
                                        rpl.append(str1)
                                        rpl.append('Agora é a vez de: '+nomes[auxx]+emoji_point)
                        else:
                            rpl = ['Chute invalido!'+emoji_lua]
                    elif text.startswith('/arriscar'):
                        arrisca = text[10:len(text)]
                        if not (len(arrisca) == 0):
                            if arrisca == palavra:
                                rpl.append(emoji_confetti+'Parabéns '+uName+' você acertou a palavra secreta e ganhou o jogo!'+emoji_confetti)
                                rpl.append('O jogo acabou, utilize /novojogo para começar um novo')
                                rpl.append('Creditos: Bot criado por @bcesarg6 e @cristoferoswald\nVersão Beta 1.7'+emoji_bug)
                                addScore(chat_id,uName, len(palavra)*2)
                                cleanGame(chat_id)
                            else:
                                rpl.append('ERROU! '+emoji_negativo+'\n'+uName+' arriscou a palavra e errou, que burro!')
                                rpl.append('*VOCÊ FOI OBLITERADO* '+emoji_poop+emoji_lua)
                                addScore(chat_id,uName, -(len(palavra)))
                                change = rmPlayer(chat_id, rd)
                                if change[0]:
                                    rpl.append('O novo ADM é o(a): '+ change[1]+emoji_point)
                                uIds = getuIds(chat_id)
                                if len(uIds) == 0:
                                    rpl.append(emoji_poop+'LOSERS'+emoji_poop)
                                    rpl.append('O jogo acabou, utilize /novojogo para começar um novo')
                                    rpl.append('Créditos: Bot criado por @bcesarg6 e @cristoferoswald\nVersão Beta 1.7'+emoji_bug)
                                    cleanGame(chat_id)
                        else:
                            rpl.append('Tentativa inválida')
                    else:
                        rpl = ['Comando não reconhecido no momento, comandos reconhecidos no momento:\n/chutar "letra", /arriscar "palavra", /dica, /palavra, /letras, /rank, /cancelar (adm), /help']
                elif not (checkRound(chat_id,uId)):
                    nomes = getPlayers(chat_id)
                    rpl.append('Não é sua vez de jogar, vez de: '+nomes[rd]+emoji_lua)
                else:
                    rpl = ['Comando não reconhecido no momento, comandos reconhecidos no momento:\n/chutar "letra", /arriscar "palavra", /dica, /palavra, /letras, /rank, /cancelar (adm), /help']
            else:
                rpl.append('Você não esta participando deste jogo '+uName+'\nlembre-se de entrar no proximo jogo se você quer participar')
        else:
            rpl = ['Não é um comando, comandos começam com "/"']
        return rpl
