#imports
import palavras
from random import randint
from google.appengine.ext import ndb

update = palavras.update_list

def comandos(self, text):
    if text.startswith('/'):
        if (text.startswith('/newgame'))  or (text.startswith('/newgame@forca_bot')):
            update(self, palavras.palavras, palavras.dicas)
            pala = palavras.get_palavra(self, randint(1,3))
            return pala
