
import os
from telegram import Update
from PIL import ImageGrab
import pandas as pd

data = pd.read_csv("other_res/Book1.csv",encoding='ISO-8859-1')



def student(update: Update, pin : str='220003', *args):
    match = data[data['REGD.NO'] == pin]
    print(match)

    if not match.empty:
        row = match.iloc[0]
        val = row[1:6]
        res = '   \n'.join(str(value) for value in val)
        update.message.reply_text(res)
        return None
    else:
        return "Sorry the applicant not found 😭/ wwrong format 😩😩😩😩 "
    
    


def screenshot(update : Update, *args) -> str:
    if not(update.message.from_user.username == "rupesh_reddy1"):
        return "only lord have access 😏😏😏😏  😏 😏"
    image = ImageGrab.grab()
    image.save("other_res/scrn.jpg","JPEG",quality = 100)
    with open("other_res/scrn.jpg",'rb') as pic:
        update.message.reply_photo(pic)
    os.remove('other_res/scrn.jpg')
    return 

def shutdown(update: Update, *args) -> str:
    if not(update.message.from_user.username == "rupesh_reddy1"):
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
    os.system("shutdown /a")
    update.message.reply_text("Shutdown stopped - A T L A S")
    
def log_file(text : str):
    with open("logs.txt",'a') as file :
        file.write(f"{text}    \n")




commands = {

    'scrn' : screenshot,
    'screenshot' : screenshot,
    'shutdown' : shutdown,
    'student' : student,
    'stop' : stop,


}

