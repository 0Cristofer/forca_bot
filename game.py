#imports
import main
import palavras
from random import randint
from google.appengine.ext import ndb

class GameState(ndb.Model):
    State = ndb.BooleanProperty(indexed=False, default=False)

def setGame(chat_id, bool):
    es = GameState.get_or_insert(str(chat_id))
    es.State = bool
    es.put()

def getGame(chat_id):
    es = GameState.get_by_id(str(chat_id))
    if es:
        return es.State
    return False

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
    return es.nomes

class Jogo:
    update = palavras.update_list
    update(palavras.palavras, palavras.dicas)
    palavra = palavras.get_palavra(randint(0,2))

    def comandos(self, uId, uName, chat_id, text):
        rpl = []
        state = getGame(chat_id)
        nomes = getPlayers(chat_id)
        if text.startswith('/'):
            if text.startswith('/novojogo') or text.startswith('/novojogo@forca_bot'):
                if state == False:
<<<<<<< HEAD
                    str1 = 'Comecando um novo jogo! Voce sera o administrador dessa rodada '+uName
                    setGame(chat_id,True)
                    str2 = 'Vamos comecar definindo os jogadores\nQuem quiser participar dessa rodada envie um /entrar :D'
                    str3 = 'Para fechar o grupo de participantes mande um /fechar Administador'
                    rpl = [str1, str2, str3]
=======
                    str1 = 'Comecando um novo jogo!'
                    setGame(chat_id,True)
                    str2 = 'Vamos comecar definindo os jogadores\nQuem quiser participar dessa rodada envie um /entrar :D'
                    rpl = [str1, str2]
>>>>>>> upstream/master
                    #Continuar
                else:
                    str1 = 'Existe um jogo em andamento neste chat!\nCaso voce queira abandonar ele use o comando /cancelar'
                    rpl = [str1]
            elif text.startswith('/entrar') or text.startswith('/entrar@forca_bot'):
<<<<<<< HEAD
                addPlayer(chat_id, uId, uName)
                str1 = 'Certo, '+uName+' voce vai participar desta rodada'
                rpl = [str1]
            elif text.startswith('/fechar') or text.startswith('/fechar@forca_bot'):
                str1 = 'Grupo de participantes fechados! Jogaram nesta rodada:'
                rpl = [str1]
                for i in range(0,len(nomes)):
                    rpl.append(nomes[i])
=======
                str1 = 'Certo, '+uName+' voce vai participar desta rodada'
                rpl = [str1]
>>>>>>> upstream/master
            elif text.startswith('/cancelar') or text.startswith('/cancelar@forca_bot'):
                if state:
                    str1 = 'Voce cancelou o jogo' #implementar cancelamento por votacao
                    setGame(chat_id,False)
                else:
                    str1 = 'Nao existe nenhum jogo ativo! Comece um com o comando /novojogo'
                rpl = [str1]
            elif text.startswith('/help') or text.startswith('/help@forca_bot'):
                str1 = 'Sou o Forca_bot, para comecar um jogo use o comando /newgame\nUse este comando /help e irei te guiando!'
                rpl = [str1]
            else:
                rpl = ['Comando nao reconhecido']
        else:
            rpl = ['Nao eh um comando, lembre se que comandos comecam com /']
        return rpl
