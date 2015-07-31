#Contem todo o gerenciamento do banco de dados

#Importa os BDs da Google

from google.appengine.ext import ndb

#BD que grava as palavras

class Palavras(ndb.Model):
    palavras = [ndb.StringProperty(indexed=False, default=False)]
    dicas = [ndb.StringProperty(indexed=False, default=False)]
    palavra = ndb.StringProperty()
    dica = ndb.StringProperty()
    mascara = ndb.StringProperty()
    letras = [ndb.StringProperty()]


def updateList(plvras, dcs):
    es = Palavras.get_or_insert(str(001))
    for i in range(0,len(plvras)):
        es.palavras.append(plvras[i])
        es.dicas.append(dcs[i])
    es.put()

def setPeD(chat_id, ped):
    es = Palavras.get_or_insert(str(chat_id))
    es.palavra = ped[0]
    es.dica = ped[1]
    es.put()

def getPeD(chat_id):
    es = Palavras.get_by_id(str(chat_id))
    return [es.palavra, es.dica]

def getNPeD(k):
    k = k+1
    es = Palavras.get_by_id(str(001))
    palavra = es.palavras[k]
    dica = es.dicas[k]
    ped = [palavra, dica]
    return ped

def setMascara(chat_id, masc):
    es = Palavras.get_or_insert(str(chat_id))
    es.mascara = masc
    es.put()

def getMascara(chat_id):
    es = Palavras.get_by_id(str(chat_id))
    return es.mascara

def setLetra(chat_id, letra):
    es = Palavras.get_or_insert(str(chat_id))
    es.letras.append(letra)
    es.put()

def getLetras(chat_id):
    es = Palavras.get_by_id(str(chat_id))
    return es.letras

def cleanLetras(chat_id):
    es = Palavras.get_or_insert(str(chat_id))
    let = es.letras
    i = len(let)
    i -= 1
    while(i >= 0):
        es.letras.remove(let[i])
        i -= 1

    es.put()

#BD que guarda os estados de cada jogo

class GameStates(ndb.Model):
    PreState = ndb.BooleanProperty(indexed=False, default=False)
    State = ndb.BooleanProperty(indexed=False, default=False)

def setPreGame(chat_id, status):
    es = GameStates.get_or_insert(str(chat_id))
    es.PreState = status
    es.put()

def getPreGame(chat_id):
    es = GameStates.get_by_id(str(chat_id))
    if es:
        return es.PreState
    return False

def setInGame(chat_id,status):
    es = GameStates.get_or_insert(str(chat_id))
    es.State = status
    es.put()

def getInGame(chat_id):
    es = GameStates.get_by_id(str(chat_id))
    if es:
        return es.State
    return False

#BD que grava os jogadores

class Players(ndb.Model):
    jogadores = [ndb.StringProperty()]
    nomes = [ndb.StringProperty()]
    adm = ndb.StringProperty()

def addPlayer(chat_id, uId, uName):
    es = Players.get_or_insert(str(chat_id))
    es.jogadores.append(uId)
    es.nomes.append(uName)
    es.put()

def setAdm(chat_id, uId):
    es = Players.get_or_insert(str(chat_id))
    es.adm = uId
    es.put()

def getuIds(chat_id):
    es = Players.get_by_id(str(chat_id))
    if es:
        return es.jogadores
    return []

def getPlayers(chat_id):
    es = Players.get_by_id(str(chat_id))
    if es:
        return es.nomes
    return []

def getAdm(chat_id):
    es = Players.get_by_id(str(chat_id))
    if es:
        return es.adm
    return False

def cleanPlayers(chat_id):
    es = Players.get_or_insert(str(chat_id))
    jog = es.jogadores
    nom = es.nomes
    i = len(jog)
    i -= 1
    while(i >= 0):
        es.jogadores.remove(jog[i])
        i -= 1
    i = len(nom)
    i -= 1
    while(i >= 0):
        es.nomes.remove(nom[i])
        i -= 1
    es.adm = ''
    es.put()
