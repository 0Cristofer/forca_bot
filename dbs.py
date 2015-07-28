from google.appengine.ext import ndb

palavras = ['teste','madalena','rodrigo schulz']
dicas = ['Nome da variavel usado frequentemente','A professora complexa','Sem ressentimentos']

class Palavras(ndb.Model):
    palavra = [ndb.StringProperty(indexed=False, default=False)]
    dica = [ndb.StringProperty(indexed=False, default=False)]

def updateList(palavras, dicas):
    es = Palavras.get_or_insert(str(001))
    for i in range(0,len(palavras)):
        es.palavra.append(palavras[i])
        es.dica.append(dicas[i])
        es.put()

def getPalavra(k):
    k = k+1
    es = Palavras.get_by_id(str(001))
    palavra = es.palavra[k]
    dica = es.dica[k]
    ped = [palavra, dica]
    return ped


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

#Classes para lista de jogares ==================================
class Players(ndb.Model):
    jogadores = [ndb.StringProperty(indexed=False, default=False)]
    nomes = [ndb.StringProperty(indexed=False, default=False)]

def addPlayer(chat_id, uId, uName):
    es = Players.get_or_insert(str(chat_id))
    es.jogadores.append(uId)
    es.nomes.append(uName)
    es.put()

def getPlayer(chat_id,uId):
    es = Players.get_by_id(str(chat_id))
    pos = es.jogadores.index(uId)
    nome = es.jogadores[pos]
    return nome

def getPlayers(chat_id):
    es = Players.get_by_id(str(chat_id))
    nomes = es.nomes
    return nomes
