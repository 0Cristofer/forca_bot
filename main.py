#-*- coding: utf-8 -*-
#Responsavel pela comunicacao do nosso codigo com o app engine (a ser melhor comentado)

#Imports necessarios para codificacao dos dados

import StringIO
import json
import logging
import random
import urllib
import urllib2
import time

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

# ================================
def getPreGame(chat_id):
    return bds.getPreGame(chat_id)

def getInGame(chat_id):
    return bds.getInGame(chat_id)

def setEnabled(chat_id, status):
    bds.setEnabled(chat_id, status)

def getEnabled(chat_id):
    return bds.getEnabled(chat_id)

def checkChat(chat_id):
    return bds.checkChat(chat_id)

def getChats():
    return bds.getChats()

def delChat(chat_id):
    bds.delChat(chat_id)

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
        uName = str(user_id.get('first_name').encode('utf-8')) #gets user first name
        emoji_gritar = ' ' + (u'\U0001f4e2').encode('utf-8')
        if not text:
            logging.info('no text')
            return

        def reply(msg=None, img=None, aux=None, esp=None):
            resp = None
            if msg:
                resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                'chat_id': str(chat_id),
                'text': msg,
                })).read()
            elif img:
                resp = multipart.post_multipart(BASE_URL + 'sendPhoto', [
                    ('chat_id', str(chat_id)),
                    ('reply_to_message_id', str(message_id)),
                ], [
                    ('photo', 'image.jpg', img),
                ])
            elif aux:
                resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                    'chat_id': str(aux),
                    'text': 'Olá jogadores do focar_bot, estivemos passando por alguns problemas na última hora como alguns devem ter percebido. Caso não estejam conseguindo jogar, recomendamos que cancelem o jogo atual e começem um novo. Caso ainda assim não estejam conseguindo jogar, contate @cristoferoswald ou @bcesarg6. Desculpem o inconveniente.'
                    #'text':'\t'+emoji_gritar+'***AVISO***'+emoji_gritar+'\nJogadores do forca_bot, uma nova versão do bot foi lançada! A versão 2.0 traz muitas novidades e uma interface totalmente nova. Recomendamos que você passe a utilizar o novo bot. Basta clicar em @PlayHangmanBot. Informamos que essa versão do bot não receberá mais atualizações e eventualmente será desligada, portanto utilizem o novo. Avisem seus amigos e se divirtam!',
                    #'disable_web_page_preview': 'true',
                    #'reply_to_message_id': str(message_id),
                })).read()
            elif esp:
                resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                    'chat_id': str(-34151177),
                    'text': 'Novo chat criado',
                    #'disable_web_page_preview': 'true',
                    #'reply_to_message_id': str(message_id),
                })).read()
            else:
                logging.error('no msg or img specified')
                resp = None

            logging.info('send response:')
            logging.info(resp)
        preJogo = preGame.PreJogo()
        Jogo = game.Jogo()
        inPreGame = getPreGame(chat_id)
        inGame = getInGame(chat_id)
        enabled = getEnabled(chat_id)
        send = []
        
        """if text.startswith('/Newws'):
            try:
                a = getChats()
                for i in range(len(a)):
                    time.sleep(1)
                    try:
                        reply(aux=a[i])
                    except Exception, e:
                        print e
                        print 'nao tem chat'
                        delChat(a[i])
            except Exception, e:
                print e"""
        try:
            if text.startswith('/start'):
                if checkChat(chat_id):
                    reply(esp='loucura')
                if enabled:
                    reply('forca_bot já esta ligado. Conheça o @playhangmanbot a nova versão do seu bot de jogo da forca! :)')
                else:
                    reply('Olá, eu sou o forca_bot!\n Uma nova versão está disponível: Conheça o @playhangmanbot a nova versão do seu bot de jogo da forca! :).\nPara começar um novo jogo digite /novojogo')
                    setEnabled(chat_id, True)
                    if (inPreGame or inGame):
                        reply('Já existe um jogo em andamento, se quiser é só continuar jogando')
            elif text.startswith('/stop'):
                if not enabled:
                    reply('forca_bot já esta desligado. Conheça o @playhangmanbot a nova versão do seu bot de jogo da forca! :)')
                else:
                    reply('forca_bot desligado. Conheça o @playhangmanbot a nova versão do seu bot de jogo da forca! :)')
                    setEnabled(chat_id, False)
            else:
                if enabled:
                    if inGame:
                        send = Jogo.game(uId, uName, chat_id, text)
                    else:
                        send = preJogo.preGame(uId, uName, chat_id, text)
            for i in range(0, len(send)):
                reply(send[i])
        except Exception, e:
            print e
            try:
                reply('Ocorreu um erro, por favor, contate @cristoferoswald ou @bcesarg6. Considere migrar para o @playhangmanbot a nova versão do seu bot de jogo da forca! :)')
            except Exception, e:
                print e
#-------------------
app = webapp2.WSGIApplication([
    ('/me', MeHandler),
    ('/updates', GetUpdatesHandler),
    ('/set_webhook', SetWebhookHandler),
    ('/webhook', WebhookHandler),
], debug=True)
