from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import res_text as res_text
import res_doc as res_doc
from datetime import datetime

API_KEY ="7227079555:AAGHqE2KpezLxpXdEN6uH1DlwyL5TTidscw"
OWNER_USERID="rupesh_reddy1"
#HELlo all  kj

cmd = res_text.commands
cmd_doc = res_doc.commands
import os
pid = os.getpid()
print(f"pid is {pid}")
#global values
updater = None #for shutting down a bot in stop function
# it is deined in stop and main function so that we canuse then globally without passing to function
def handle_txt(update : Update, context: CallbackContext) ->None:
    mes = update.message
    print(mes.from_user.id)
    
    msg = mes.text.split()
    res_text.log_file(f"{datetime.now()}     {mes.from_user.username}                     {' '.join(msg)}")
    
    m = msg[0].strip().lower()
    print(m)
    msg[0] = update
    if m in cmd:
        val_cmd = cmd[m](*msg)
        if val_cmd:
            update.message.reply_text(val_cmd)
        else:
            pass
    else:
        mes.reply_text("yo 🤖 🤖! master its a invalid command, teach me that first")

def handle_doc(update : Update,context : CallbackContext) ->None:
    mes = update.message
    print(update.message.document.mime_type)
    caption = update.message.caption if update.message.caption else "a b c"
    
    cap = caption.split()
    res_text.log_file(f" document {datetime.now()}     {mes.from_user.username}                     {' '.join(cap)}")
    if(mes.from_user.username != OWNER_USERID
    ):
        mes.reply_text("Yo who the fu*k ?")
        return
    m = cap[0].strip().lower()
    cap[0]=update
    if m in cmd_doc:
        val_cmd = cmd_doc[m](*cap)
    else:
        update.message.reply_text("oh shit, what i want to do with that crap 🤬 🤬 🤬..provide  some caption ")

   
def handle_photo(update : Update,*args):
    photo = update.message.photo
    
    # 
    # pass some pic function dated 21 9 24
    # 


def handle_message(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.username == OWNER_USERID:
        handle_txt(update,context)
    else:
        update.message.reply_text("only lord have access 😏😏😏😏  😏 😏 - A T L A S")
        res_text.log_file(f"user tried to acces {update.message.from_user.username}    {update.message.from_user.first_name}  {update.message.from_user.id}  {update.message.chat_id}")

def start(update: Update,context: CallbackContext):
    update.message.reply_text("it's A T L A S here, how can i help you?")

def destruct(update: Update, context: CallbackContext) -> None:
    if(update.message.from_user.username != OWNER_USERID
    ):
        update.message.reply_text("you havent got access")
        return
    update.message.reply_text("Self destructing... 💥")
    print(context.bot_data)
    global updater
    global pid
    if updater:
        
        print("Terminating the bot")
        os.system(f"taskkill /pid {pid} /f")

        

def main():
    global updater
    updater = Updater(API_KEY)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # On message received from the user
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    dp.add_handler(MessageHandler(Filters.document,handle_doc))
    dp.add_handler(MessageHandler(Filters.photo,handle_photo))
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("destruct",destruct))
    #starting the bot
    updater.start_polling()

    # ctrl + c to exit True
    updater.idle()

if __name__ == '__main__':
    main()



