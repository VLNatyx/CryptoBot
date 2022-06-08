from coinbase.wallet.client import Client

COINBASE_KEY="yourkey"
COINBASE_SECRET="yoursecret"
coinbase_client=Client(COINBASE_KEY, COINBASE_SECRET)
def priceAlert(update, context):
    if len(context.args) > 2:
        crypto = context.args[0].upper()
        sign = context.args[1]
        price = context.args[2]
        update.message.reply_text(f"⏳ Ti mandero un messagio quando {crypto} raggiungerà {price} CHF: \nIl prezzo corrente {crypto} é {coinbase_client.get_spot_price(currency_pair=crypto + '-CHF')['amount']} CHF")
        context.job_queue.run_repeating(priceAlertCallback, interval=60, first=1, context=[crypto, sign, price, update.message.chat_id])
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='⚠️ Per favore inserisci una crypto valida ed un valore valido: \nEsempio /notifica BTC < 30000')

def priceAlertCallback(context):
    crypto = context.job.context[0]
    sign = context.job.context[1]
    price = context.job.context[2]
    chat_id = context.job.context[3]
    send = False
    crypto_price = coinbase_client.get_spot_price(currency_pair=crypto + '-CHF')['amount']
    if sign == '<' and float(price) >= float(crypto_price):
        send = True
    elif sign == '>' and float(price) <= float(crypto_price):
        send = True
	
    if send:
        crypto_prezzo=round(float(crypto_price), 3)
        context.bot.send_message(chat_id=chat_id, text=f'👋 La Crypto {crypto} ha raggiunto {price} CHF ed é arrivata a {crypto_prezzo} CHF!')
        context.job.schedule_removal()

def Exchange(update, context):
    if len(context.args) > 1:
        coin1 = context.args[0].upper()
        coin2 = context.args[1].upper()
        coin1_price = coinbase_client.get_spot_price(currency_pair=coin1 + '-CHF')['amount']
        coin2_price = coinbase_client.get_spot_price(currency_pair=coin2 + '-CHF')['amount']
        coin_exchange=float(coin1_price)/float(coin2_price)
        update.message.reply_text(f"💰 {round(coin_exchange, 2)} {coin2} equivalgono a 1 {coin1}")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='⚠️ Per favore inserisci due crypto separate da uno spazio: \nEsempio: /cambio BTC ETH')
