
import os
from telegram import Update
from PIL import ImageGrab
import pandas as pd
import psutil

data = pd.read_csv("other_res/Book1.csv",encoding='ISO-8859-1')



def student(update: Update, pin : str='220003', *args):
    mes = update.message
    match = data[data['REGD.NO'] == pin]
    print(match)

    if not match.empty:
        row = match.iloc[0]
        val = row[1:6]
        res = '   \n'.join(str(value) for value in val)
        mes.reply_text(res)
        return None
    else:
        return "Sorry the applicant not found 😭/ wwrong format 😩😩😩😩 "
    
    


def screenshot(update : Update, *args) -> str:
    mes = update.message
    if not(mes.from_user.username == "rupesh_reddy1"):
        return "only lord have access 😏😏😏😏  😏 😏"
    image = ImageGrab.grab()
    image.save("other_res/scrn.jpg","JPEG",quality = 100)
    with open("other_res/scrn.jpg",'rb') as pic:
        mes.reply_photo(pic)
    os.remove('other_res/scrn.jpg')
    return 

def shutdown(update: Update, *args) -> str:
    mes = update.message
    if not(mes.from_user.username == "rupesh_reddy1"):
        return "only lord have access 😏😏😏😏  😏 😏"
    try:
        if(len(args)>0):
            os.system(f"shutdown /s /t {int(args[0])} ")
        else:
            os.system(f"shutdown /s /t 10 ")
            return f"shutdown in 10 seconds"

        print(args[0])
        return f"shutdown in {args[0]} seconds"
    
    except Exception as e:
        return f"Error :  {e}"
    
def stop(update: Update,*args):
    mes = update.message
    os.system("shutdown /a")
    mes.reply_text("Shutdown stopped - A T L A S")
    
def log_file(text : str):
    with open("logs.txt",'a') as file :
        file.write(f"{text}    \n")

def system_info(update: Update,*args):
    mes = update.message
    d_usage = psutil.disk_usage("/").percent
    ram = psutil.virtual_memory().percent
    battery = psutil.sensors_battery()
    b_percent = battery.percent if battery else None
    cpu = psutil.cpu_percent(interval=1)
    m = f"disk usage : {d_usage}%\nram : {ram}% \n battery : {b_percent}% \n cpu : {cpu}%"
    mes.reply_text(m)
def email(update : Update,*args):
    receiver_email = args[1]
    subject = args[2]
    body = args[3]




commands = {

    'scrn' : screenshot,
    'screenshot' : screenshot,
    'shutdown' : shutdown,
    'student' : student,
    'stop' : stop,
    'system' : system_info,
    'email' : email


}

