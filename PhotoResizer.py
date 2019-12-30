import PIL.Image as Image
import os
import tkinter as tk

def convertor (imgpath,edited_dir,img_name):
    img = Image.open(imgpath)
    ar = float(img.size[1])/float(img.size[0])
    width = 400
    height = int(ar*width)
    img = img.resize((width,height), Image.ANTIALIAS)
    return img


def writer(img_dir,edited_dir):
    try:
        os.mkdir(edited_dir)
        with os.scandir(img_dir) as entries:
            for entry in entries:
                img_name = str(entry.name)
                imagepath = img_dir+'/'+img_name
                img = convertor(imagepath,edited_dir,img_name)
                img.save(edited_dir + '/' + img_name)
                statinfo = os.stat(edited_dir + '/' + img_name)
                size = float(int(statinfo.st_size)/1000)
                print(size)
                if size > 64:
                    print("image too big changing quality")
                    print("quality =", quality)
                    img.save(edited_dir + '/' + img_name, quality=40)
                    size = int(statinfo.st_size) / 1000
                    print("new size :", size)


    except FileExistsError :
        with os.scandir(img_dir) as entries:
            for entry in entries:
                img_name = str(entry.name)
                imagepath = img_dir+'/'+img_name
                img = convertor(imagepath,edited_dir,img_name)
                img.save(edited_dir + '/' + img_name)
                statinfo = os.stat(edited_dir + '/' + img_name)
                size = int(statinfo.st_size)/1000
                print(size)
                if size>64:
                    print("image too big changing quality")
                    print("quality =", quality)
                    img.save(edited_dir + '/' + img_name,quality=40)
                    size = int(statinfo.st_size) / 1000
                    print("new size :", size)

def sub_func(pic_path,edit_path):
    picture = pic_path.get()
    edit = edit_path.get()
    writer(picture,edit)

def gui():
    root = tk.Tk()
    root.geometry("700x250")
    root.resizable(True, True)
    root.title("Photo Resizer")
    labelfont = ("Times", 20, "bold")

    tk.Label(text="Enter the absolute path of the pictures folder : ", font=labelfont).place(x=40,y=10)
    pic_path = tk.Entry(width=40,font=labelfont)
    pic_path.place(x=40,y=50)

    tk.Label(text="Enter the name of the new folder : ", font=labelfont).place(x=40, y=90)
    edit_path = tk.Entry(width=40, font=labelfont)
    edit_path.place(x=40, y=130)


    button = tk.Button(text='Submit', command= lambda : sub_func(pic_path,edit_path))
    button.place(x=320, y=200)


    root.mainloop()

def CLI():
    pic_dir = input("enter the directory : ")
    name = input("name of new dir : ")
    writer(pic_dir,name)

gui()
