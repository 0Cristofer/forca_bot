#Contem todo o gerenciamento do banco de dados

#Imports
from operator import itemgetter, attrgetter, methodcaller
from google.appengine.ext import ndb

#BD que grava as palavras
class PeDs(ndb.Model):
    pecs = ndb.StringProperty(repeated=True)
    tams = ndb.IntegerProperty(repeated=True)

def getNPeD(rnd, rnd2):
    PeD = ndb.Key(PeDs, 'PeDs').get()
    matriz = []

    x = [0]
    leg = (len(PeD.tams))
    for i in range(leg):
        a = i+1
        soma = x[i] + PeD.tams[i]
        x.append(soma)

    for i in range(len(PeD.tams)):
        pals = []
        a = i+1
        for j in range(x[i], x[a]):
            pals.append(PeD.pecs[j])
        matriz.append(pals)

    p = matriz[rnd][rnd2]
    d = matriz[rnd][0]
    ped = [p, d]
    return ped

def updateList(matriz):
    pec = []
    tam = []
    for i in range(len(matriz)):
        tam.append(len(matriz[i]))
        for j in range(len(matriz[i])):
            pec.append(matriz[i][j])
    PeD = PeDs(pecs = pec, tams = tam, id = 'PeDs')
    PeD.put()


class Rank(ndb.Model):
    rank = ndb.StringProperty(repeated = True)

def addPlayerRank(chat_id, uName):
    r = ndb.Key(Rank, chat_id).get()
    if not (uName in r.rank):
        r.rank.append(uName)
        r.rank.append('0')
        r.put()

def updateRank(chat_id):
    r = ndb.Key(Rank, chat_id).get()
    matriz = []
    vet = []
    for i in range(0, (len(r.rank)), 2):
        aux = []
        aux.append(r.rank[i])
        aux.append(int(r.rank[i+1]))
        matriz.append(aux)
        i = i+1
    matriz = sorted(matriz, key=itemgetter(1), reverse=True)
    for i in range(len(matriz)):
        vet.append(matriz[i][0])
        vet.append(str(matriz[i][1]))
    r.rank = vet
    r.put()

def getRank(chat_id):
    r = ndb.Key(Rank, chat_id).get()
    if not r:
        r = Rank(id = chat_id)
        r.put()
        return []
    matriz = []
    for i in range(0, (len(r.rank)), 2):
        aux = []
        aux.append(r.rank[i])
        aux.append(r.rank[i+1])
        matriz.append(aux)
    return matriz

def addScore(chat_id, uName, score):
    r = ndb.Key(Rank, chat_id).get()
    index = r.rank.index(uName)+1
    r.rank[index] = str(int(r.rank[index])+score)
    r.put()

class Game(ndb.Model):
    enabled = ndb.BooleanProperty(indexed=False, default=True)
    preState = ndb.BooleanProperty(indexed=False, default=False)
    state = ndb.BooleanProperty(indexed=False, default=False)
    jogadores = ndb.StringProperty(repeated=True)
    nomes = ndb.StringProperty(repeated=True)
    adm = ndb.StringProperty(default='noAdm')
    rnd = ndb.IntegerProperty(default=0)
    palavra = ndb.StringProperty(default='noPalavra')
    dica = ndb.StringProperty(default='noDica')
    mascara = ndb.StringProperty(default='noMascara')
    letras = ndb.StringProperty(repeated=True)
    vidas = ndb.IntegerProperty(default = 6)

def setEnabled(chat_id, status):
    e = ndb.Key(Game, chat_id).get()
    if e:
        e.enabled = status
        e.put()

def getEnabled(chat_id):
    e = ndb.Key(Game, chat_id).get()
    if e:
        return e.enabled
    return True

def menosVida(chat_id):
    v = ndb.Key(Game, chat_id).get()
    v.vidas -= 1
    v.put()

def getVidas(chat_id):
    v = ndb.Key(Game, chat_id).get()
    return v.vidas

def setVidas(chat_id, modVida):
    v = ndb.Key(Game, chat_id).get()
    v.vidas = v.vidas+modVida
    v.put()

def setGame(chat_id):
    g = Game(id = chat_id)
    g.put()

def setPeD(chat_id, ped):
    PeD = ndb.Key(Game, chat_id).get()
    PeD.palavra = ped[0]
    PeD.dica = ped[1]
    PeD.put()

def getPeD(chat_id):
    PeD = ndb.Key(Game, chat_id).get()
    ped = [PeD.palavra, PeD.dica]
    return ped

def setMascara(chat_id, masc):
    msc = ndb.Key(Game, chat_id).get()
    msc.mascara = masc
    msc.put()

def getMascara(chat_id):
    msc = ndb.Key(Game, chat_id).get()
    return msc.mascara

def setLetra(chat_id, letra):
    let = ndb.Key(Game, chat_id).get()
    let.letras.append(letra)
    let.put()

def getLetras(chat_id):
    let = ndb.Key(Game, chat_id).get()
    return let.letras

def setPreGame(chat_id, status):
    GameState = ndb.Key(Game, chat_id).get()
    GameState.preState = status
    GameState.put()

def getPreGame(chat_id):
    GameState = ndb.Key(Game, chat_id).get()
    if GameState:
        return GameState.preState
    return False

def setInGame(chat_id, status):
    GameState = ndb.Key(Game, chat_id).get()
    GameState.state = status
    GameState.put()

def getInGame(chat_id):
    GameState = ndb.Key(Game, chat_id).get()
    if GameState:
        return GameState.state
    return False

def addPlayer(chat_id, uId, uName):
    players = ndb.Key(Game, chat_id).get()
    players.jogadores.append(uId)
    players.nomes.append(uName)
    players.put()

def setAdm(chat_id, uId):
    a = ndb.Key(Game, chat_id).get()
    a.adm = uId
    a.put()

def getuIds(chat_id):
    u = ndb.Key(Game, chat_id).get()
    return u.jogadores

def getPlayers(chat_id):
    p = ndb.Key(Game, chat_id).get()
    return p.nomes

def rmPlayer(chat_id, rd):
    p = ndb.Key(Game, chat_id).get()
    p.jogadores.remove(p.jogadores[rd])
    p.nomes.remove(p.nomes[rd])
    p.put()

def getAdm(chat_id):
    a = ndb.Key(Game, chat_id).get()
    return a.adm

def setRound(chat_id, rd):
    r = ndb.Key(Game, chat_id).get()
    r.rnd = rd
    r.put()

def getRound(chat_id):
    r = ndb.Key(Game, chat_id).get()
    return r.rnd

def cleanGame(chat_id):
    p = ndb.Key(Game, chat_id).get()
    p.key.delete()
