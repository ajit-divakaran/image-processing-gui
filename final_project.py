import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import cv2
from matplotlib import pyplot as plt
import sys

m = tk.Tk()
m.title("Image processing GUI")
m.geometry("730x690")

def openg():
    file_path = filedialog.askopenfilename()
    modifyg(file_path)
    print(file_path)

def modifyg(file_path):
    img = cv2.imread(file_path)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    Resized0= cv2.resize(img,(960,700))

    
    if img is None:
        print("Can not find any image. Choose appropriate file")   
        sys.exit()

    label1=Label(m,text="Image uploaded successfully",font=('Arial bold',10),padx=10,pady=5,bg='white',fg='green').grid(row=0,column=1,padx=10,pady=10)
    editbutton=Button(m,text="Edit image",command=lambda:show0(Resized0,file_path),padx=20,pady=5,activebackground="pink",justify=LEFT,bg="AntiqueWhite2").grid(row=1,column=0,padx=10,pady=10)

def show0(Resized0,file_path):
    
    grayScaleImage= cv2.cvtColor(Resized0, cv2.COLOR_BGR2GRAY)
    ReSized1 = cv2.resize(grayScaleImage, (960, 700))
    cannyimage = cv2.Canny(Resized0,50,50)
    ReSized2 = cv2.resize(cannyimage, (960, 700))
    blurimage=cv2.bilateralFilter(Resized0,10,250,250)
    ReSized3= cv2.resize(blurimage, (960, 700))
    label3=Label(m,text="Choose an option",font=('Arial bold',10),padx=10,pady=5).grid(row=2,column=1,padx=10,pady=10)
    gray1=Button(m,text="Gray image",command=lambda:show1(ReSized1,Resized0,file_path),padx=19,pady=5,activebackground="pink").grid(row=3,column=0,padx=10,pady=10)
    canny1=Button(m,text="Canny image",command=lambda:show2(ReSized2,Resized0,file_path),padx=10,pady=5,activebackground="pink").grid(row=3,column=1,padx=10,pady=10)
    blur1=Button(m,text="Blur image",command=lambda:show3(ReSized3,Resized0,file_path),padx=10,pady=5,activebackground="pink").grid(row=3,column=2,padx=10,pady=10)
    
def show1(ReSized1,Resized0,file_path):
    plt.subplot(121),plt.imshow(Resized0,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(ReSized1,cmap = 'gray')
    plt.title('Gray Image'), plt.xticks([]), plt.yticks([])
    plt.show()


def show2(ReSized2,Resized0,file_path):
    plt.subplot(121),plt.imshow(Resized0,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(ReSized2,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()
    print("Executed")

def show3(ReSized3,Resized0,file_path):
    plt.subplot(121),plt.imshow(Resized0,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(ReSized3,cmap = 'gray')
    plt.title('Blurred Image'), plt.xticks([]), plt.yticks([])
    plt.show()
    print("Executed")
    
def exit0():
    res=messagebox.askquestion("Confirm","Are you sure you want to exit the program?")
    if res == 'yes':
        m.destroy()

upload=Button(m,text="Upload image",command=openg,padx=10,pady=5,activebackground="pink").grid(row=0,column=0,padx=10,pady=10)
exitbutton=Button(m,text="Exit",command=exit0,padx=29,pady=5,activebackground='#ff5434').grid(row=1,column=2,padx=10,pady=10)



m.mainloop()
