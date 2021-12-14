from pprint import pprint

import pymongo

client = pymongo.MongoClient()
db = client.chat

def adicionar_mensagem(mensagem):
    res = db.mensagens.insert_one(mensagem)
    return res.acknowledged

def resgatar_mensagens(filtro=None):
    res = db.mensagens.find(filtro)
    return list(res)

def main():
    if 0:
        adicionar_mensagem({
            'de': 'fabricio',
            'para': 'rubens',
            'conteudo': "Vc está gostando da última review?"
        })
        adicionar_mensagem({
            'de': 'rubens',
            'para': 'fabricio',
            'conteudo': "Sim, estou adorando!"
        })

    else:
        pprint(resgatar_mensagens({
            '$or': [
                {'de': 'douglas'},
                {'para': 'douglas'}
            ]
        }))
        pprint(resgatar_mensagens({'para': {'$in': ['douglas', 'rubens']}}))


if __name__ == '__main__':
    main()
