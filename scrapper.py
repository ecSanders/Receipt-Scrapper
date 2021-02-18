from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import os
import tkinter as tk
import cmath

root= Tk(className = " Receipt Scrapper")

# Declared canvas
canvas1 = Canvas(root
                , width = 300
                , height = 400
                , bg = '#474749'
                , relief = 'raised')
canvas1.pack()

# Declared label 
label1 = Label(root
                , text='The Receipt Scrapper'
                , bg = '#474749'
                , fg="white")
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

# Function declaration of the browse_button_img
def get_img ():
    global image_path
    global image_name
    global path

    image_path = filedialog.askopenfilename()
    image_name = os.path.basename(image_path)
    
    test = image_path.split(image_name)
    path = test[0]
    
# Creating a photoimage object to use image
photo = PhotoImage(file="/Users/jonathanhald/Documents/SAI/receipt_scanner/Receipt_Scanner/dist/icons/upload.png")

# Resizing image to fit on button
photoimage = photo.subsample(9, 9)

# Button to allow the user to select an image
browse_button_img = Button(root
                            , height = 40
                            , width = 200
                            , image = photoimage
                            , text="     Import Image File"
                            ,  command=get_img
                            , fg='white'
                            , bg='#1db954'
                            , font=('helvetica', 12, 'bold')
                            ,compound=LEFT)
browse_button_img.pack()
canvas1.create_window(150, 150, window=browse_button_img)

# Function declaration of the convert_excel
def convert_excel ():
    global new_file_name
    new_file_name = 'poppy'
    clear_dir = 'cd\ '
    run_tesseract = 'tesseract ' + image_name + ' ' + new_file_name

    # Input the path and image file into the CNN to have the information
    # on the iamge extracted from the image.
    os.system(clear_dir)
    os.system('cd ' + path)
    os.chdir(path)
    os.system(run_tesseract)

    # Converts txt file to cvs
    read_file = pd.read_csv (path + new_file_name + '.txt', sep='delimiter', header=None)
    

    # Converts cvs file to excel file
    read_file.to_excel (path + new_file_name + '.xlsx', index = None, header=True)


photo2 = PhotoImage(file="/Users/jonathanhald/Documents/SAI/receipt_scanner/Receipt_Scanner/dist/icons/convert.png")

# Resizing image to fit on button
photoimage2 = photo2.subsample(7, 7)

# Button that takes the selected image file and inputs it into the CNN
# to have the information extracted from it. It will then convert the 
# new file with the extracted information into a csv and then excel file.
button_excel = Button(root
                        , height = 40
                        , width = 200
                        , image = photoimage2
                        , text='     Convert to Excel'
                        , command=convert_excel
                        , bg='#1db954'
                        , fg='white'
                        , font=('helvetica', 12, 'bold')
                        , compound=LEFT)
button_excel.pack()
canvas1.create_window(150, 210, window=button_excel)

# Function declaration to open the new excel file that was created
def open_file():
    os.system('open ' + new_file_name + '.xlsx')


photo3 = PhotoImage(file="/Users/jonathanhald/Documents/SAI/receipt_scanner/Receipt_Scanner/dist/icons/open.png")

# Resizing image to fit on button
photoimage3 = photo3.subsample(17, 17)
# Button to the new fileopen file
open_file_excel = Button(root
                        ,height = 40
                        ,width = 200
                        ,image = photoimage3
                        ,text='             Open File     '
                        ,command=open_file
                        ,bg='#1db954'
                        ,fg='white'
                        ,font=('helvetica', 12, 'bold')
                        ,compound=LEFT)
open_file_excel.pack()

canvas1.create_window(150, 270, window=open_file_excel)

# Function declaration to exit the program
def exit_application():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application'
                                    ,icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()

# Button to exit the program     
exit_button = Button (root
                    , width = 200
                    , height = 40
                    , text='       Exit Application     '
                    ,command=exit_application
                    , bg='#ec002d'
                    , fg='white'
                    , font=('helvetica', 12
                    , 'bold'))
canvas1.create_window(150, 330, window=exit_button)

root.mainloop()
