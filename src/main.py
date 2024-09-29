from .commands import *
load_dotenv()
BOT_TOKEN = os.getenv("ATLAS_BOT")
def handle_message(update: Update,context: CallbackContext) -> None:
    mes = update.message
    if (mes.from_user.username != "rupesh_reddy1"):
        mes.reply_text("No access")
        return
    cmds = mes.text.split() #split msg into list
    
    cmd = cmds[0].lower() 
    cmds[0]=update #remove 1st word i.e command from text and check if in cmd.._list and also make cmd[0] = update for function parameters
    if cmd in commands_list:
        commands_list[cmd](*cmds)
    else:
        mes.reply_text("i cant finish that task")


def main():
    updater = Updater(BOT_TOKEN)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
