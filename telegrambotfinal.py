import requests
import telebot
import time

## Conexão telegram
TOKEN = '5957864714:AAFu9jRNkzztTc2rsZNHqL5RV2YCoTIM-y8'     #colocar seu token do bot
id_chat = '-1001563326954'                              #colocar id do chat, para super grupo colocar -100 antes
bot = telebot.TeleBot(TOKEN)
bot.send_message(id_chat, text="Bot conectado com sucesso. | Desenvolvido por  @kingtrade")


## Inicial Config
analise_sinal = False
entrada = 0
num_entradas = 4
resultados = []
sinal_value = []
valores = []

## Message Controller
def start_over():
    global analise_sinal
    global entrada

    entrada = 1
    analise_sinal = False
    return

def entradas():
    global entrada
    entrada += 1

    if entrada <= num_entradas:
        bot.send_message(id_chat, text=f"⚠️atenção entrada {entrada}⚠️")
        win_check
    else :
        loss()
        start_over()
    return

def win_check():
    if sinal_value[0:1] != resultados[0:1] and resultados[0:1] == ['A']:
        win()
        start_over
        return
    if sinal_value[0:1] != resultados[0:1] and resultados[0:1] != ['A']:
        entradas()
        return
    else:
        win_check
        return

## Win / Loss Messages

def win():
    bot.send_message(id_chat,text = f"Mais uma pra conta ✅. {valores[0:1]}")                          #para enviar esticker basta trocar para: bot.send_sticker(chat_id=id_chat, sticker"colocar o id do sticker aqui")
    return 

def loss():
    bot.send_message(id_chat, text="Analise o mercado ❌.")
    return

def enviar_sinal(padrao):
    bot.send_message(id_chat, text=f'''
    🚨Sinal Confirmado🚨
    ⏯️ Padrão: {padrao}
    💶entrar após {valores[0:1]}
    🐓4 entradas: (opcional)''')
    return


def api():
    global check_entrada
    global analise_sinal
    crash_api = requests.get('https://blaze.com/api/crash_games/recent').json()
    for value in crash_api:
        if (float(value['crash_point'])) < 2:
            valor = 'B'
        elif (float(value['crash_point'])) > 4:
            valor = 'A'
        else :
            valor = 'M'
        resultados.append(valor)
        valores.append(float(value['crash_point']))
    print (resultados[0:5])
    print (valores[0:5])
    time.sleep(20)

def strategy_pattern():
    global analise_sinal
    global sinal_value

    enviar_sinal(padrao)
    analise_sinal = True
    sinal_value = resultados
    print('Sinal Enviado')


def strategy(resultados):
    global analise_sinal
    global padrao

    if analise_sinal == True:
        win_check()
    else:
        if resultados[0:5] == ['B','B','M','B','B']:
            padrao = '🧙 Bruxo 🧙'
            strategy_pattern(padrao)
        if resultados [0:5] == ['B','B','B','B','B']:
            padrao = '🛞 Freio da Blaze 🛞'
            strategy_pattern(padrao)
        if resultados [0:5] == ['A', 'M', 'B', 'A', 'M']:
            padrao = '☠️ L7, me namora? ☠️'
            strategy_pattern(padrao)
            

while True:
    valores.clear()
    resultados.clear()
    api()
    strategy(resultados)
    

     
