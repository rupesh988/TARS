from .commands import *
load_dotenv()
BOT_TOKEN = os.getenv("ATLAS_BOT")
def handle_message(update: Update,context: CallbackContext):
    screenshot(update)

def main():
    updater = Updater(BOT_TOKEN)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
