import requests
import telebot
import time

## Bot Connection
TOKEN = '5957864714:AAFu9jRNkzztTc2rsZNHqL5RV2YCoTIM-y8'     #colocar seu token do bot
id_chat = '-1001563326954'                              #colocar id do chat, para super grupo colocar -100 antes
bot = telebot.TeleBot(TOKEN)
bot.send_message(id_chat, text="Bot conectado com sucesso. | Desenvolvido por  @kingtrade")

## Get Data from Blaze
resultados = []
fresh_data = []

## Configurações Iniciais
analise_sinal = False
entrada = 0
num_entradas = 4

## Message Controler

def reset():
    global analise_sinal
    entrada
    
    entrada = 0
    analise_sinal = False
    return

def entradas():
    global entrada
    entrada += 1

    if entrada <= num_entradas:
        bot.send_message(id_chat, text="⚠️atenção entrada{entrada}⚠️")
    else :
        loss()
        reset()
    return

def acertos(resultados):
    if resultados[0:1] == ['A']:
        win()
        reset()
        return
    else:
       entradas()
       return

## Padrões de mensagens
def win():
    bot.send_message(id_chat,"Mais uma pra conta ✅.")                          #para enviar esticker basta trocar para: bot.send_sticker(chat_id=id_chat, sticker"colocar o id do sticker aqui")
    return 

def loss():
    bot.send_message(id_chat, text="Analise o mercado ❌.")
    return

def enviar_sinal(padrao):
    bot.send_message(id_chat, text=f'''
    🚨Sinal Confirmado🚨

    ⏯️ Padrão: {padrao}

    💶entrar após => {float(['crash_point'])}

    🐓4 entradas: (opcional)''')
    return


## Validador de Padrões

def strategy(resultados):

    if analise_sinal == True:
            acertos(entradas)
    else:
    ## Inserir aqui as estratégias 
        if resultados[0:5] == ['B','B','M','B','B']:
            padrao = '🧙 Bruxo 🧙'
            enviar_sinal(padrao)
            analise_sinal = True
            print('sinal enviado')
    
        if resultados[0:3] == ['M','B','M']:
            padrao = '👑 Coroa👑 '
            enviar_sinal(padrao)
            analise_sinal = True
            print('sinal enviado')
    
        if resultados[0:5] == ['B','B','B','B','B']:
            padrao = '🛞 Freio da Blaze 🛞'
            enviar_sinal(padrao)
            analise_sinal = True
            print('sinal enviado')

## System execution
class new_data:
    success = True
    while success:
        crash_api = requests.get('https://blaze.com/api/crash_games/recent')
        success = crash_api.status_code==200
        data = crash_api.json()
        for value in data:
                if (float(value['crash_point'])) < 2:
                    valor = 'B'
                elif (float(value['crash_point'])) > 4:
                    valor = 'A'
                else :
                    valor = 'M'
                fresh_data.append(valor)        
        print(fresh_data)
        def Check():
            if fresh_data != resultados:
                print(resultados)
                resultados.insert(0, fresh_data[0])
                strategy(resultados)
            else:
                time.sleep(10)
                fresh_data.clear()

