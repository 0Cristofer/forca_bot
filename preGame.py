#-*- coding: utf-8 -*-
#Contem a logica do jogo

#Importa os BDs
import bds

#Importa funcao que randomiza um int
from random import randint, shuffle

#Pega as funcoes dos BDs para poderem ser utilizadas nesse arquivo
def updateList(matriz):
    bds.updateList(matriz)

def getNPeD(rnd1, rnd2):
    return bds.getNPeD(rnd1, rnd2)

def setGame(chat_id):
    bds.setGame(chat_id)

def setPreGame(chat_id, status):
    bds.setPreGame(chat_id, status)

def getPreGame(chat_id):
    return bds.getPreGame(chat_id)

def setInGame(chat_id, status):
    bds.setInGame(chat_id, status)

def getInGame(chat_id):
    return bds.getInGame(chat_id)

def addPlayer(chat_id, uId, uName):
    bds.addPlayer(chat_id, uId, uName)
    bds.addPlayerRank(chat_id, uName)

def setAdm(chat_id, uId):
    bds.setAdm(chat_id, uId)

def getuIds(chat_id):
    return bds.getuIds(chat_id)

def getPlayers(chat_id):
    return bds.getPlayers(chat_id)

def getAdm(chat_id):
    return bds.getAdm(chat_id)

def setPeD(chat_id, ped):
    bds.setPeD(chat_id, ped)

def setMascara(chat_id, mascara):
    bds.setMascara(chat_id, mascara)

def getMascara(chat_id):
    return bds.getMascara(chat_id)

def setLetra(chat_id, letra):
    bds.setLetra(chat_id, letra)

def getLetras(chat_id):
    return bds.getLetras(chat_id, letra)

def setRound(chat_id, rd):
    bds.setRound(chat_id, rd)

def getRound(chat_id):
    return bds.getRound(chat_id)

def setVidas(chat_id, modVida):
    bds.setVidas(chat_id, modVida)

def setVidasInit(chat_id,modVida):
    bds.setVidasInit(chat_id,modVida)

def getVidas(chat_id):
    return bds.getVidas(chat_id)

def cleanGame(chat_id):
    bds.cleanGame(chat_id)

def getRank(chat_id):
    rank = bds.getRank(chat_id)
    str1 = 'NOME - SCORE\n'
    for i in range(len(rank)):
        str1 = str1 + str(rank[i][0])+' - '+str(rank[i][1])+'\n'
    return str1

def setShuffle(chat_id, nomes, uIds):
    bds.setShuffle(chat_id, nomes, uIds)

#\u2764\ufe0f
#Classe que contem toda logica do jogo (a ser melhor comentada)

class PreJogo:

    def preGame(self, uId, uName, chat_id, text):
        text = str(text.lower().encode('utf-8'))
        #uName = str(uName.decode('utf-8'))
        emoji_heart = (u'\u2764\ufe0f').encode('utf-8')
        emoji_heartb = (u'\U0001f494').encode('utf-8')
        emoji_confetti = (u'\U0001f389').encode('utf-8')
        emoji_claps = (u'\U0001f44f\U0001f3fc').encode('utf-8')
        emoji_feliz = (u'\U0001f601').encode('utf-8')
        emoji_lua = (u'\U0001f31a').encode('utf-8')
        emoji_coroa = (u'\U0001f451').encode('utf-8')
        emoji_sorriso = (u'\U0001f601').encode('utf-8')
        matriz = [
            ['Animais ou espécies', 'macaco', 'elefante','zebra','papagaio','andorinha','golfinho','gorila','tubarao','lobo','ornitorrinco','cavalo','humano','lebre','coelho','piriquito','pomba','dinossauro','macaco','borboleta'],
            ['Comidas, sobremesas ou frutas', 'banana','miojo','cachorro quente','lasanha','salada de frutas','carambola','x-salada','frango frito','batata frita','ketchup','chocolate','morango','strogonoff','arroz e feijao','batata doce','pizza','sushi','temaki','fondue de chocolate','cupcake','donut','eclair','froyo','gingerbread','honeycomb','icecream sandwich','jellybean','kitkat','lollipop','marshmallow'],
            ['Profissão', 'professor', 'zelador','prostituta','tia do Xerox','medico','marceneiro','contrabandista','traficante','designer','game developer','dublador','escritor'],
            ['Relacionado a Computadores/Internet/Programação', 'programador','compilador','servidor','monitor','algoritmo','netflix','orkut','instagram','tumblr','twitter','rede neural','google','photoshop','wolfram alpha','python','java','framework','ruby','javascript','latex','android','stack overflow','wikipedia','debugging'],
            ['Pessoas importantes (ex: Presidentes ou cientistas)','albert einstein','barack obama','abraham lincoln','nikola tesla','carl sagan','larry page','steves jobs','mark zuckerberg','tim cook','charles chaplin','platao','aristoteles','dilma rousseff','luiz inacio lula da silva','fernando herinque cardoso','george washington','george walker bush','adolf hitler','shigeru miyamoto'],
            #['Você deu azar e não tem dica!','chaves','parafuseta','rebimboca','kibe','penal','orkut','android','telegram','whatsapp','ornitorrinco','skyrim','dota2','lolzinho','pipa','voce nao vai acertar essa','sim so de zoas'],
            ['Cidades do mundo','brasilia','curitiba','maringa','new york','tokio','barcelona','amsterda','paris','milao','pequim','berlim','sao paulo','rio de janeiro','salvador','manaus','rio branco','orlando','los angeles','calgary','toronto','montreal','dallas','londres'],
            ['Herói ou vilão do mundo das HQ/cinema (DC e Marvel)','batman','flash','mulher maravilha','pinguim','super Homem','lanterna verde','duende verde','homem aranha','thor','hulk','homem de ferro','homem formiga','tocha humana','o coisa','viuva negra','arqueiro verde','Groot','Rocket Raccoon','Magneto','Wolverine'],
            ['Videogames, jogos e empresas da area','the legend of zelda','super mario','counter strike','nintendo wii','super nintendo','playstation','steam','defense of the ancients','league of legends','final fantasy','donkey kong','angry birds','fallout','bioshock','tetris','the elders scroll','minecraft','call of duty','battlefield','bomberman','sonic the hedgehog','just dance','nintendo','sony','sega','dreamcast','bethesda','2k games','valve','riot'],
            ['Títulos ou nomes relacionados a TV e/ou Cinema!','how i met your mother','sense8','netflix','american Beauty','donnie Darko','esqueceram de mim','the sixth sense','the shining','titanic','todo mundo odeia o cris','agostinho carrara','chapeleiro maluco','alice no pais das maravilhas','harry potter','hora da aventura','bob esponja'],
            ['Países', 'brasil', 'estados Unidos', 'alemanha', 'japao', 'coreia do Sul', 'africa do sul', 'holanda', 'argentina', 'espanha', 'chile', 'equador', 'canada', 'singapura', 'india', 'emirados arabes', 'italia', 'inglaterra', 'austria', 'grecia', 'Republica Checa'],
            [
                'Pokémon',
                'Bulbasaur',
                'Ivysaur',
                'Venusaur',
                'Charmander',
                'Charmeleon',
                'Charizard',
                'Squirtle',
                'Wartortle',
                'Blastoise',
                'Caterpie',
                'Metapod',
                'Butterfree',
                'Weedle',
                'Kakuna',
                'Beedrill',
                'Pidgey',
                'Pidgeotto',
                'Pidgeot',
                'Rattata',
                'Raticate',
                'Spearow',
                'Fearow',
                'Ekans',
                'Arbok',
                'Pikachu',
                'Raichu',
                'Sandshrew',
                'Sandslash',
                'Nidoran',
                'Nidorina',
                'Nidoqueen',
                'Nidoran',
                'Nidorino',
                'Nidoking',
                'Clefairy',
                'Clefable',
                'Vulpix',
                'Ninetales',
                'Jigglypuff',
                'Wigglytuff',
                'Zubat',
                'Golbat',
                'Oddish',
                'Gloom',
                'Vileplume',
                'Paras',
                'Parasect',
                'Venonat',
                'Venomoth',
                'Diglett',
                'Dugtrio',
                'Meowth',
                'Persian',
                'Psyduck',
                'Golduck',
                'Mankey',
                'Primeape',
                'Growlithe',
                'Arcanine',
                'Poliwag',
                'Poliwhirl',
                'Poliwrath',
                'Abra',
                'Kadabra',
                'Alakazam',
                'Machop',
                'Machoke',
                'Machamp',
                'Bellsprout',
                'Weepinbell',
                'Victreebel',
                'Tentacool',
                'Tentacruel',
                'Geodude',
                'Graveler',
                'Golem',
                'Ponyta',
                'Rapidash',
                'Slowpoke',
                'Slowbro',
                'Magnemite',
                'Magneton',
                'Doduo',
                'Dodrio',
                'Seel',
                'Dewgong',
                'Grimer',
                'Muk',
                'Shellder',
                'Cloyster',
                'Gastly',
                'Haunter',
                'Gengar',
                'Onix',
                'Drowzee',
                'Hypno',
                'Krabby',
                'Kingler',
                'Voltorb',
                'Electrode',
                'Exeggcute',
                'Exeggutor',
                'Cubone',
                'Marowak',
                'Hitmonlee',
                'Hitmonchan',
                'Lickitung',
                'Koffing',
                'Weezing',
                'Rhyhorn',
                'Rhydon',
                'Chansey',
                'Tangela',
                'Kangaskhan',
                'Horsea',
                'Seadra',
                'Goldeen',
                'Seaking',
                'Staryu',
                'Starmie',
                'Mr. Mime',
                'Scyther',
                'Jynx',
                'Electabuzz',
                'Magmar',
                'Pinsir',
                'Tauros',
                'Magikarp',
                'Gyarados',
                'Lapras',
                'Ditto',
                'Eevee',
                'Vaporeon',
                'Jolteon',
                'Flareon',
                'Porygon',
                'Omanyte',
                'Omastar',
                'Kabuto',
                'Kabutops',
                'Aerodactyl',
                'Snorlax',
                'Articuno',
                'Zapdos',
                'Moltres',
                'Dratini',
                'Dragonair',
                'Dragonite',
                'Mewtwo',
                'Mew',
            ]
        ]
        rpl = []
        preState = getPreGame(chat_id)
        if text.startswith('/'):
                #Bloco Inicial================================================
            if preState == False:
                if text.startswith('/novojogo') or text.startswith('/novojogo@forca_bot'):
                    setGame(chat_id)
                    rpl.append('Começando um novo jogo! Você sera o administrador dessa rodada '+uName+'\nVamos começar definindo os jogadores\nQuem quiser participar dessa rodada envie o comando /entrar '+emoji_sorriso+'\nSe precisar de ajude mande um /help')
                    rpl.append('Para fechar o grupo de participantes envie o comando /fecharjogo Administador '+uName)
                    setPreGame(chat_id, True)
                    setAdm(chat_id, uId)
                    addPlayer(chat_id, uId, uName)
                    updateList(matriz)
                    setRound(chat_id, 0)
                elif text.startswith('/help') or text.startswith('/ajuda'):
                    str1 = 'Não existe nenhum jogo em andamento, utilize o comando /novojogo para começar e irei te guiando'+emoji_feliz+'\nCaso deseje ver o ranking use /rank'
                    rpl = [str1]
                elif text.startswith('/cancelar') or text.startswith('/cancelar@forca_bot'):
                    str1 = 'Não existe jogo no momento, envie o comando /help caso precise de ajuda!'
                    rpl = [str1]
                elif text.startswith('/rank') or text.startswith('/rank@forca_bot'):
                    rpl.append(emoji_coroa+'RANKING'+emoji_coroa)
                    rank = getRank(chat_id)
                    rpl.append(rank)
                else:
                    str1 = 'Comando não reconhecido no momento, comandos reconhecidos no momento:\n/novojogo, /rank, /help'
                    rpl = [str1]
            #Fim do bloco incial /// Comeco do bloco PreGame ===================================
            else:
                if text.startswith('/novojogo') or text.startswith('/novojogo@forca_bot'):
                    str1 = 'Existe um jogo em modo de entrada, se quiser entrar digite /entrar'
                    rpl = [str1]
                elif text.startswith('/rank') or text.startswith('/rank@forca_bot'):
                    rpl.append(emoji_coroa+'RANKING'+emoji_coroa)
                    rank = getRank(chat_id)
                    rpl.append(rank)
                elif text.startswith('/entrar') or text.startswith('/entrar@forca_bot'):
                    uIds = getuIds(chat_id)
                    if uId in uIds:
                        str1 = 'Você já participa desse jogo'+emoji_lua
                        rpl = [str1]
                    else:
                        addPlayer(chat_id, uId, uName)
                        str1 = 'Certo, '+uName+' você vai participar desta rodada'+emoji_feliz
                        rpl = [str1]
                elif text.startswith('/cancelar') or text.startswith('/cancelar@forca_bot'):
                    adm = getAdm(chat_id)
                    if uId == adm:
                        str1 = 'O Administador cancelou o jogo!' #implementar cancelamento por votacao
                        cleanGame(chat_id)
                        rpl = [str1]
                    else:
                        str1 = 'Você não tem autorização para fechar o jogo\nApenas o Administrador pode fazer isso'
                        rpl = [str1]
                elif text.startswith('/fecharjogo') or text.startswith('/fecharjogo@forca_bot'):
                    adm = getAdm(chat_id)
                    if uId == adm:
                        setInGame(chat_id,True)
                        leng = len(matriz)-1
                        rnd1 = randint(0,leng)
                        leng = len(matriz[rnd1])-1
                        rnd2 = randint(1, leng)
                        ped = getNPeD(rnd1, rnd2)
                        ped[1] = ped[1].lower()
                        setPeD(chat_id, ped)
                        mascara = '*'*(len(ped[0]))
                        lMascara = list(mascara)
                        for i in range(len(mascara)):
                            if ped[0][i]== ' ':
                                lMascara[i] = ' '
                            if ped[0][i]== '-':
                                lMascara[i] = '-'
                        mascara = "".join(lMascara)
                        setMascara(chat_id, mascara)
                        nomes = getPlayers(chat_id)
                        modVida = len(ped[0])/5 if len(ped[0]) > 5 else 0
                        modVida += len(nomes)-3 if len(nomes) > 4 else 0
                        modVida = 9 if modVida > 9 else modVida
                        setVidas(chat_id, modVida)
                        setVidasInit(chat_id, modVida)
                        vidas = getVidas(chat_id)
                        #Randomizar a lista de participantes
                        nomes = getPlayers(chat_id)
                        uIds = getuIds(chat_id)
                        # Given list1 and list2
                        nomes_shuf = []
                        uIds_shuf = []
                        index_shuf = range(len(nomes))
                        shuffle(index_shuf)
                        for i in index_shuf:
                            nomes_shuf.append(nomes[i])
                            uIds_shuf.append(uIds[i])
                        nomes = nomes_shuf
                        uIds = uIds_shuf
                        setShuffle(chat_id, nomes, uIds)
                        str1 = ''
                        for i in range(0, len(nomes)):
                            str1 = str1+nomes[i]+'\n'
                        str2='O jogo vai começar agora! Instruções:\nUtilize o comando /chutar "letra" para chutar letras, quando estiver pronto para arriscar utilize o comando /arriscar "palavra", mas cuidado, se você errar perde o jogo!\nVIDAS:'
                        for i in range(vidas):
                            str2 = str2 + emoji_heart
                        rpl.append(str2)
                        rpl.append('Palavra secreta: '+mascara)
                        rpl.append('Dica: '+str(ped[1]))
                        rpl.append('Grupo de participantes fechados! Vocês jogarão nesta ordem:')
                        rpl.append(str1)
                    else:
                        str1 = 'Você não tem autorização para cancelar o jogo\nApenas o administrador pode fazer isso'
                        rpl = [str1]
                elif text.startswith('/help') or text.startswith('/help@forca_bot'):
                    str1 = 'Nesse momento a partida está aberta para entrada de novos jogadores\nEnvie o comando /entrar para participar ou /fecharjogo para iniciar o jogo'
                    rpl = [str1]
                else:
                    str1 = 'Comando não reconhecido no momento\nComandos reconhecidos no momento:\n/entrar, /fecharjogo (adm), /cancelar (adm), /rank, /help'
                    rpl = [str1]
        else:
            rpl = ['Não é um comando, lembre se que comandos começam com /']
        return rpl
