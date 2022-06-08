from telegram.ext import CommandHandler, Updater
import requests
from coinbase.wallet.client import Client
from text import start, help
from coin import priceAlert, Exchange

updater = Updater(token="yourtoken", use_context=True)
dispatcher = updater.dispatcher

def controlla(update, context):
    if len(context.args) > 0:
        global coinprova
        coinprova = context.args[0].upper()
        data = single_prices(update, context)
        for i in data:
            if data[i]['price'] < 0.0001:
              update.message.reply_text(
                "Cryptovaluta: {}\n"
                "Prezzo: {:.8f} CHF\n"
                "Cambio giornaliero: {:.2f}%\n"
                "Cambio orario: {:.2f}%".format(data[i]['coin'],
                                            data[i]['price'],
                                            data[i]['change_day'],
                                            data[i]['change_hour']))
            elif 1 > data[i]['price'] >0.0001:
              update.message.reply_text(
                "Cryptovaluta: {}\n"
                "Prezzo: {:.5f} CHF\n"
                "Cambio giornaliero: {:.2f}%\n"
                "Cambio orario: {:.2f}%".format(data[i]['coin'],
                                            data[i]['price'],
                                            data[i]['change_day'],
                                            data[i]['change_hour']))
            elif data[i]['price'] >1:
              update.message.reply_text(
                "Cryptovaluta: {}\n"
                "Prezzo: {:.2f} CHF\n"
                "Cambio giornaliero: {:.2f}%\n"
                "Cambio orario: {:.2f}%".format(data[i]['coin'],
                                            data[i]['price'],
                                            data[i]['change_day'],
                                            data[i]['change_hour']))
    else:
     context.bot.send_message(chat_id=update.effective_chat.id, text='⚠️ Per favore inserisci una crypto valida: \nEsempio /controlla BTC')
      
def single_prices(update, callbackcontext):
    global coinprova
    coins = [coinprova]
    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=CHF".format(",".join(coins))).json()["RAW"]
    data = {}
    for i in crypto_data:
        data[i] = {
            "coin": i,
            "price": crypto_data[i]["CHF"]["PRICE"],
            "change_day": crypto_data[i]["CHF"]["CHANGEPCT24HOUR"],
            "change_hour": crypto_data[i]["CHF"]["CHANGEPCTHOUR"]
        }
    return data

def all_prices(update, context):
    coin=["BTC", "ETH", "USDT", "USDC", "BNB","ADA", "XRP", "BUSD", "SOL", "DOGE"]
    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=CHF".format(",".join(coin))).json()["RAW"]
    data = {}
    for i in crypto_data:
        data[i] = {
            "coin": i,
            "price": crypto_data[i]["CHF"]["PRICE"],
            "change_day": crypto_data[i]["CHF"]["CHANGEPCT24HOUR"],
            "change_hour": crypto_data[i]["CHF"]["CHANGEPCTHOUR"]
        }
        update.message.reply_text(
            "Cryptovaluta: {}\n"
            "Prezzo: {:.2f} CHF\n"
            "Cambio giornaliero: {:.2f}%\n"
            "Cambio orario: {:.2f}%".format(data[i]['coin'],
                                         data[i]['price'],
                                         data[i]['change_day'],
                                         data[i]['change_hour']))

def all_command(update, context):
    coin=["BTC", "ETH", "USDT", "USDC", "BNB","ADA", "XRP", "BUSD", "SOL", "DOGE"]
    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=CHF".format(",".join(coin))).json()["RAW"]
    data = {}
    for i in crypto_data:
        data[i] = {
            "coin": i,
            "price": crypto_data[i]["CHF"]["PRICE"],
            "change_day": crypto_data[i]["CHF"]["CHANGEPCT24HOUR"],
            "change_hour": crypto_data[i]["CHF"]["CHANGEPCTHOUR"]
        }
    return data

def sopra_orario(update, context):
    data = all_command(update, context)
    a=0
    for i in data:
        if data[i]['change_hour'] > 0:
            a+=1
            update.message.reply_text(
                "Cryptovaluta: {}\n"
                "Prezzo: {:.2f} CHF\n"
                "Cambio giornaliero: {:.2f}%\n"
                "Cambio orario: {:.2f}%".format(data[i]['coin'],
                                             data[i]['price'],
                                             data[i]['change_day'],
                                             data[i]['change_hour']))
    if a == 0:
        update.message.reply_text("Nessuna Crypto ha guadagnato valore nell'ultima ora")

def sotto_orario(update, context):
    data = all_command(update, context)
    a = 0
    for i in data:
        if data[i]['change_hour'] < 0:
            a+=1
            update.message.reply_text(
                "Cryptovaluta: {}\n"
                "Prezzo: {:.2f} CHF\n"
                "Cambio giornaliero: {:.2f}%\n"
                "Cambio orario: {:.2f}%".format(data[i]['coin'],
                                             data[i]['price'],
                                             data[i]['change_day'],
                                             data[i]['change_hour']))
    if a == 0:
        update.message.reply_text("📈Nessuna Crypto ha perso valore nell'ultima ora")

def sopra_giorno(update, context):
    data = all_command(update, context)
    a = 0
    for i in data:
        if data[i]['change_day'] > 0:
            a+=1
            update.message.reply_text(
                "Cryptovaluta: {}\n"
                "Prezzo: {:.2f} CHF\n"
                "Cambio giornaliero: {:.2f}%\n"
                "Cambio orario: {:.2f}%".format(data[i]['coin'],
                                             data[i]['price'],
                                             data[i]['change_day'],
                                             data[i]['change_hour']))
    if a == 0:
        update.message.reply_text("📉Nessuna Crypto ha guadagnato valore nell'ultimo giorno")

def sotto_giorno(update, context):
    data = all_command(update, context)
    a = 0
    for i in data:
        if data[i]['change_day'] < 0:
            a += 1
            update.message.reply_text(
                "Cryptovaluta: {}\n"
                "Prezzo: {:.2f} CHF\n"
                "Cambio giornaliero: {:.2f}%\n"
                "Cambio orario: {:.2f}%".format(data[i]['coin'],
                                             data[i]['price'],
                                             data[i]['change_day'],
                                             data[i]['change_hour']))
    if a == 0:
        update.message.reply_text("📈Nessuna Crypto ha perso valore nell'ultimo giorno")

def Wallet(update, context):
    update.message.reply_text("👛Guida per i wallet di Coinbase: https://www.youtube.com/watch?v=byNNauAJrKI")
    update.message.reply_text("👛Link al wallet di Coinbase: https://www.coinbase.com/it/wallet")


dispatcher.add_handler(CommandHandler("Help", help)) 
dispatcher.add_handler(CommandHandler('start', start))    
dispatcher.add_handler(CommandHandler("sopra_ora", sopra_orario))
dispatcher.add_handler(CommandHandler("sotto_ora", sotto_orario))
dispatcher.add_handler(CommandHandler("sopra_oggi", sopra_giorno))
dispatcher.add_handler(CommandHandler("sotto_oggi", sotto_giorno))
dispatcher.add_handler(CommandHandler("controlla", controlla))
dispatcher.add_handler(CommandHandler("all", all_prices))
dispatcher.add_handler(CommandHandler("cambio", Exchange))
dispatcher.add_handler(CommandHandler("wallet", Wallet))
dispatcher.add_handler(CommandHandler("notifica", priceAlert))
updater.start_polling()
updater.idle()