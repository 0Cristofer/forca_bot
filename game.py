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

def getPlayer(chat_id, uId):
    return dbs.getPlayer(chat_id, uId)

def getPlayers(chat_id):
    return dbs.getPlayers(chat_id)

class Jogo:
    updateList(dbs.palavras, dbs.dicas)
    palavra = getPalavra(randint(0,2))

    def comandos(self, uId, uName, chat_id, text):
        rpl = []
        PreState = getPreGame(chat_id)
        State = getInGame(chat_id)
        if (State == False):
            nomes = getPlayers(chat_id)
            if text.startswith('/'):
                if text.startswith('/novojogo') or text.startswith('/novojogo@forca_bot'):
                    if PreState == False:
                        str1 = 'Comecando um novo jogo! Voce sera o administrador dessa rodada '+uName
                        setPreGame(chat_id,True)
                        str2 = 'Vamos comecar definindo os jogadores\nQuem quiser participar dessa rodada envie um /entrar :D'
                        str3 = 'Para fechar o grupo de participantes mande um /fechar Administador'
                        addPlayer(chat_id, uId, uName)
                        rpl = [str1, str2, str3]
                        #Continuar
                    else:
                        str1 = 'Existe um jogo sendo organizado!\nCaso voce queira abandonar ele use o comando /cancelar'
                        rpl = [str1]
                elif text.startswith('/entrar') or text.startswith('/entrar@forca_bot'):
                    addPlayer(chat_id, uId, uName)
                    str1 = 'Certo, '+uName+' voce vai participar desta rodada'
                    rpl = [str1]
                elif text.startswith('/fecharJogo') or text.startswith('/fecharJogo@forca_bot'):
                    str1 = 'Grupo de participantes fechados! Jogarao nesta rodada:'
                    rpl = [str1]
                    for i in range(1,len(nomes)):
                        rpl.append(nomes[i])
                    setInGame(chat_id,True)
                    rpl.append('O jogo vai comecar agora!') #Mudar talvez
                elif text.startswith('/cancelar') or text.startswith('/cancelar@forca_bot'):
                    if PreState:
                        str1 = 'Voce cancelou o jogo' #implementar cancelamento por votacao
                        setPreGame(chat_id,False)
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
        else: #Existe um jogo em andamento
            nomes = getPlayers(chat_id)
            if text.startswith('/help') or text.startswith('/help@forca_bot'):
                str1 = 'O jogo esta em andamento, aqui vao estar varias ajudas hue'
                rpl = [str1]
            elif text.startswith('/cancelar') or text.startswith('/cancelar@forca_bot'): #Mudar, sei la
                if uName == nomes[1]:
                    str1 = 'O administador cancelou jogo que estava em andamento!'
                    setInGame(chat_id,False)
                    rpl = [str1]
                else:
                    str1 = 'Somente o administrador do jogo pode cancelar!\nVoce nao eh administrador!'
                    rpl = [str1]
        return rpl
