from google.appengine.ext import ndb

palavras = ['teste','madalena','rodrigo schulz']
dicas = ['Nome da variavel usado frequentemente','A professora complexa','Sem ressentimentos']

class Palavras(ndb.Model):
    palavra = [ndb.StringProperty(indexed=False, default=False)]
    dica = [ndb.StringProperty(indexed=False, default=False)]

def update_list(palavras, dicas):
    es = Palavras.get_or_insert(str(001))
    for i in range(0,len(palavras)):
        es.palavra.append(palavras[i])
        es.dica.append(dicas[i])
        es.put()

def get_palavra(k):
    k = k+1
    es = Palavras.get_by_id(str(001))
    palavra = es.palavra[k]
    dica = es.dica[k]
    ped = [palavra, dica]
    return ped
