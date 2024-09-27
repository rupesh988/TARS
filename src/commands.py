from .libs import *


#for shutdowning the system in time seconds
def shutdown(update: Update,time : str = '5',*args):
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
        

def system_info(update: Update,*args):
    mes = update.message
    sys_info = ""
    disk = psutil.disk_usage('/').percent
    ram = psutil.virtual_memory().percent
    bat = psutil.sensors_battery()
    battery = bat.percent if bat else "server battery"
    cpu = psutil.cpu_percent(interval=1)
    sys_info = f" disk : {disk}% \n ram : {ram}% \n cpu : {cpu}% \n power : {battery}%"
    mes.reply_text(sys_info)

    


commands ={
    "shutdown" : shutdown,
    "system" : system_info,

}