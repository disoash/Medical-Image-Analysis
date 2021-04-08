import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter.filedialog import *
from tkinter.messagebox import showinfo 
from PIL import ImageTk, Image, ImageFont, ImageDraw

main_window = tk.Tk()
# main_window.geometry('400x400')
main_window.title ('MRI Deep Learning')
main_window.configure(background='#ffffff')

main_window.rowconfigure(0, minsize=600, weight=1)
main_window.columnconfigure(1, minsize=600, weight=1)

frame1 = tk.Frame(main_window, bg='#b1d4e0')
frame2 = tk.Frame(main_window, bg ='white')
label_gambar = tk.Label()


def browse_file():
    global label_gambar
    filetypes = (
        ('Picture files', '*.png *.jpeg *.jpg' ),
        ('All files', '*.*'))
    filename = askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    if not filetypes:
        return
    
    try:
        global uploaded
        uploaded = Image.open(filename)
        uploaded = uploaded.resize((512,512),Image.ANTIALIAS)
        # uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        gambar =  ImageTk.PhotoImage(uploaded)
        label_gambar.grid_forget()
        label_gambar = tk.Label(frame2)
        label_gambar.configure(image=gambar)
        label_gambar.image=gambar
        label_gambar.grid(row = 1, column=0, columnspan = 3)
        print("image uploaded")
    except:
        print("can't upload image")

def save_file():
    
    gambar1 = uploaded
    gambar1 = gambar1.resize((512,512),Image.ANTIALIAS)
    new_image = Image.new('RGB', size = (512, 525), color='white')
    new_image.paste(gambar1,(0,13))

    title_font = ImageFont.truetype("consola.ttf", 20)
    title_text = "Predicted : "
    draw_image = ImageDraw.Draw(new_image)
    draw_image.text((0,0), title_text, (0,0,0) ,font=title_font)

    filetypes = (
        ('Picture files', '*.png *.jpeg *.jpg' ),
        ('All files', '*.*'))
    filenames = asksaveasfile(
        title='Open a file',
        filetypes=filetypes,
        defaultextension = filetypes)
    new_image.save(filenames)
    print('kesimpen')
    # return

def process_file():
    

    bar = Progressbar(main_window, length=100)
    bar['value'] = 50
    # bar.grid(column=0, row=3, sticky = 's')
    bar.place(x=500,y=570)

def help_popup():
    showinfo(
        title="Help",
        message ='Instructon:\n\n1. CLick "Browse" to open file image \n\n2. After image file has choosen, click "Process" to clasify the image.\nIf you want to process another image, click "Browse" again.\n\n3. choose "Save" button if you want to save image with classification label. '
    )
    return



label_1 = tk.Label(frame2,
    text="MEDICAL IMAGE ANALISYS",
    fg='Black',
    bg='White',
    font=('arial',16),
    justify = 'center')
tombol_browse = tk.Button(frame1, 
    fg='white',
    bg='#0c2d48',
    text="Browse",
    command=browse_file)
tombol_process = tk.Button(frame1, 
    fg='white',
    bg='#0c2d48',
    text="Process",
    command=process_file)
tombol_save = tk.Button(frame1, 
    fg='white',
    bg='#0c2d48',
    text="Save",
    command=save_file)
tombol_help = tk.Button(frame1, 
    fg='white',
    bg='#0c2d48',
    text="Help",
    command=help_popup)



label_1.grid(row=0,column=0, sticky="n")
frame1.grid(row=0, column=0, sticky="ns")
frame2.grid(row=0, column=1, sticky="ns")

tombol_browse.grid(row=0, column=0, sticky="ew", padx=7, pady=2)
tombol_process.grid(row=1, column=0, sticky="ew", padx=7, pady=2)
tombol_save.grid(row=2, column=0, sticky="ew", padx=7, pady=2)
tombol_help.grid(row=3, column=0, sticky="ew", padx=7, pady=2)

main_window.mainloop()  
