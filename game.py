#imports
import main
import palavras
from google.appengine.ext import ndb

class NewGame(ndb.Model):

class Jogo:
    keys = palavras.update_list(palavras.palavras, palavras.dicas)
    WebHook = main.WebhookHandler()
    reply = WebHook.reply
    uId = WebHook.uId
    text = WebHook.text.lower()

    if text.startswith('/'):
        if (text.startswith('/newgame'))  or (text.startswith('/newgame@forca_bot')):
