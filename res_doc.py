import os
from telegram import Update,InputMediaPhoto
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import io
import plot_fun
import time


def topdf(update : Update, *args):
    mes = update.message
    doc = mes.document
    
    file = doc.get_file()
    id = doc.file_id
    name = doc.file_name
    f_path = f"other_res/docs/{name}"
    file.download(custom_path=f_path)
    print(f_path)
    print("downloaded")
    name1 = f"{name}.pdf"
    
    if "image" == doc.mime_type.split('/')[0] :
        image = Image.open(f_path)
        if image.mode in ("RGBA","P"):
            image = image.convert("RGB")
        image.save("other_res/docs/"+name1,"PDF",resolution=100.0)

        with open(f"other_res/docs/{name1}",'rb') as img_file:
            mes.reply_document(img_file)
        os.remove(f"other_res/docs/{name1}")
        os.remove(f_path)


    else:
        mes.reply_text("Damn i cant convert it imao ☠")

def plot(update : Update, plot_type : str, *args):
    mes = update.message
    doc = mes.document
    file = doc.get_file()
    fileName = doc.file_name
    fileId = doc.file_id
    f_path = f"other_res/docs/{fileName}"
    file.download(f_path)
    
    try :
        df = pd.read_csv(filepath_or_buffer= f_path, encoding='ISO-8859-1')
        if plot_type == "head" :
            col_z = df.columns
            col_z = "  ".join(col_z)
            mes.reply_text(col_z)
            
            return
        colToPlot = [c for c in args]
        plot_data = df[colToPlot]
        plot_ax = plot_data.plot(kind=plot_type)
        plt.xlabel("index")
        plt.ylabel("values")
        plt.title(f"{plot_type} plot by A T L A S")
        plt.legend(colToPlot)
        plt.savefig('atlas_plot.png',format='png')
        with open('atlas_plot.png','rb') as plt_img:
            update.message.reply_photo(plt_img)
        os.remove("atlas_plot.png")
        

    except Exception as e:
        mes.reply_text(f"Exception : {e}")
    except KeyboardInterrupt:
        print("Process interopted ")
    finally:
        os.remove(f_path)
        plt.close()

def text_to_image(text, output_image_path):
    # Define image size (width, height), modify depending on content length
    image_size = (1000, 1500)  # Adjust height if text is long

    # Create a new blank image with a white background
    img = Image.new('RGB', image_size, color=(255, 255, 255))

    # Initialize ImageDraw to draw on the image
    d = ImageDraw.Draw(img)

    # Load a font (use any system font you have, or use default)
    font = ImageFont.load_default()

    # Define text positioning (left padding, top padding)
    padding = 20
    current_height = padding

    # Split text into lines to manage overflow
    lines = text.split('\n')
    
    # Draw each line on the image
    for line in lines:
        d.text((padding, current_height), line, font=font, fill=(0, 0, 0))
        current_height += 15  # Move the cursor down after each line

    # Save the image
    img.save(output_image_path,quality=95)


def analyse(update: Update,*args):
    mes = update.message
    doc = mes.document
    file_id = doc.file_id
    file_name = doc.file_name
    file = doc.get_file()
    f_path = f"other_res/docs/{file_name}"
    file.download(custom_path=f_path)
    try:
        df = pd.read_csv(f_path,encoding="ISO-8859-1")
        mes.reply_text("being analysed .be patient for 5 seconds tick tick")

        # message to reply back
        m = "head \n"
        m+=df.head(2).to_string()
        m+="\n info\n"
        #the df.info() is used to print data only we want to store it in m so save it into buffer and then to m
        buffer =io.StringIO()
        df.info(buf=buffer)
        m+=' '.join(buffer.getvalue())
        # its not working 
        # Exception : 'list' attribute has no object 'write'

        m+= "\n describe \n"
        m+=df.describe().to_string()
        m+="\n missing\n"
        m+=df.isnull().sum().to_string()
        m+="\n shape \n"
        m+=str(df.shape)
        m+="\n dtypes\n"
        m+=df.dtypes.to_string()
        i_path = "plots/image.jpg"
        text_to_image(m,i_path)
        # with open(i_path,'rb') as img:
        #     mes.reply_photo(img)   its used whrn analyse function from plot_fun dont work
        plot_fun.analyze_dataset(f_path,"plots")

        # send all photos to sender 1st iterate over images inplots folder and use mediagroup dated: 22-09-2024

        image_files = [os.path.join("plots", f) for f in os.listdir("plots") if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        media = [InputMediaPhoto(open(img,'rb')) for img in image_files]
        #if files present send the reply back else send error
        if media:
            mes.reply_media_group(media)
        else:
            mes.reply_text("oops E R R O R ❌ ❌")

        

    except Exception as e:
        mes.reply_text(f"Exception : {e}")
    finally:
        os.remove(f_path)
        
        
         





    



    

    


commands = {
    'topdf' : topdf,
    'plot' : plot,
    'analyse' : analyse,


}