def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Benvenuto, sono un bot per controllare le tue Crypto preferite! \nUsa / per inserire un comando, con /help puoi vedere tutti i comandi")                          

def help(update, context):
   update.message.reply_text(
'1) Per vedere i valori e i cambi giornalieri ed orari scrivi /controlla e scegli la crypto\n' +
'2) Per vedere i cambi di valore delle 10 crypto principali puoi usare /sopra_oggi, /sotto_oggi,  /sopra_ora, /sotto_ora.\n' +
"3) Per vedere i valori e i cambiamenti di tutte le crypto usa /all\n"+
"4) Per vedere un wallet da noi consigliato ed una guida scrivi /wallet\n"+
"5) Per ricevere un avviso quando una crypto arriva ad un valore prestabilito scrivi /notifica \n"+
"6) Per vedere il cambio tra 2 crypto scrivi /cambio")
