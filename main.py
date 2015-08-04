#Responsavel pela comunicacao do nosso codigo com o app engine (a ser melhor comentado)

#Imports necessarios para codificacao dos dados

import StringIO
import json
import logging
import random
import urllib
import urllib2

#Para enviar imagens

from PIL import Image
import multipart

#Utilizados para fins da app engine

from google.appengine.api import urlfetch
from google.appengine.ext import ndb
import webapp2

#Importa o jogo em si

import bds
import game
import preGame

TOKEN = '123881753:AAEQXNdXS9fMLIFjzlVkpQw9mMd40vvChBw'

BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'

preJogo = preGame.PreJogo()
Jogo = game.Jogo()

# ================================

class EnableStatus(ndb.Model):
    # key name: str(chat_id)
    enabled = ndb.BooleanProperty(indexed=False, default=False)


# ================================

def setEnabled(chat_id, yes):
    es = EnableStatus.get_or_insert(str(chat_id))
    es.enabled = yes
    es.put()

def getEnabled(chat_id):
    es = EnableStatus.get_by_id(str(chat_id))
    if es:
        return es.enabled
    return False

def getInGame(chat_id):
    return bds.getInGame(chat_id)

# ================================

class MeHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getMe'))))


class GetUpdatesHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getUpdates'))))


class SetWebhookHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        url = self.request.get('url')
        if url:
            self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'setWebhook', urllib.urlencode({'url': url})))))


class WebhookHandler(webapp2.RequestHandler):
    def post(self):
        urlfetch.set_default_fetch_deadline(60)
        body = json.loads(self.request.body)
        logging.info('request body:')
        logging.info(body)
        self.response.write(json.dumps(body))

        update_id = body['update_id']
        message = body['message']
        message_id = message.get('message_id')
        date = message.get('date')
        text = message.get('text')
        fr = message.get('from')
        chat = message['chat']
        chat_id = str(chat['id']) #gets chat id
        user_id = message['from']
        uId = str(user_id.get('id'))    #gets user id
        uName = str(user_id.get('first_name')) #gets user first name

        if not text:
            logging.info('no text')
            return

        def reply(msg=None, img=None):
            if msg:
                resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                    'chat_id': str(chat_id),
                    'text': msg.encode('utf-8'),
                    'disable_web_page_preview': 'true',
                    #'reply_to_message_id': str(message_id),
                })).read()
            elif img:
                resp = multipart.post_multipart(BASE_URL + 'sendPhoto', [
                    ('chat_id', str(chat_id)),
                    ('reply_to_message_id', str(message_id)),
                ], [
                    ('photo', 'image.jpg', img),
                ])
            else:
                logging.error('no msg or img specified')
                resp = None

            logging.info('send response:')
            logging.info(resp)
        #try:
        inGame = getInGame(chat_id)
        if inGame:
            send = Jogo.game(uId, uName, chat_id, text)
        else:
            send = preJogo.preGame(uId, uName, chat_id, text)
        for i in range(0, len(send)):
            reply(send[i])
        #except:
        #    reply('Erro bem louco')
#-------------------
app = webapp2.WSGIApplication([
    ('/me', MeHandler),
    ('/updates', GetUpdatesHandler),
    ('/set_webhook', SetWebhookHandler),
    ('/webhook', WebhookHandler),
], debug=True)
