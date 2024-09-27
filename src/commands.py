from .libs import *


#for shutdowning the system in time seconds
def shutdown(update: Update,time : str = '5'):
    mes = update.message
    if(time == "stop"):
        os.system("shutdown /a")
        mes.reply_text("Shutdown terminated")
        return
    try:
        time = int(time)
        os.system(f"shutdown /s /t {time}")
        mes.reply_text(f"shutdown will be executed in {time} seconds")
    except Exception as e:
        mes.reply_text(f"can't shutdown the system \n Reason : {e}")
        


    



commands ={}