from tkinter import Label,Tk,filedialog,Button,Toplevel,Entry, Scrollbar, RIGHT, Y, VERTICAL
from PIL import Image, ImageTk, ImageFilter
import webbrowser as w
from PIL import Image

root = Tk()
root.configure(background = '#0099ff')


path=filedialog.askopenfilename(filetypes=[("Image File",'.*')])
img = Image.open(path)
w, h = img.size
img = img.resize((w//2, h//2), Image.ANTIALIAS)
tkimage = ImageTk.PhotoImage(img)
myvar=Label(root,image = tkimage)
myvar.image = tkimage



def display():
    window = Toplevel(root)
    im = Image.open(path)
    width, height = im.size
    im = im.resize((width//2, height//2), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(window,image = tkimage)
    myvar.image = tkimage
    myvar.pack()
    window.mainloop()



def rotate():
    window = Toplevel(root)
    
    def yes(w1):
        global path
        path = 'temp.jpg'
        img.save(path)
        w1.destroy()

    def rotatenow():
        global img
        img = Image.open(path)
        img = img.rotate(int(e.get()))
        w1 = Toplevel(window)
        width, height = img.size
        img = img.resize((width//2, height//2), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(img)
        myvar=Label(w1,image = tkimage)
        myvar.image = tkimage
        l1 = Label(w1,text = "Save?")
        b1 = Button(w1,text = "Yes",command = lambda w1=w1:yes(w1))
        b2 = Button(w1,text = "No",command = w1.destroy)
        l1.pack()
        b1.pack()
        b2.pack()
        myvar.pack()
        w1.mainloop()
    l = Label(window,text = "Degrees to rotate")
    l.pack()
    e = Entry(window)
    e.pack()
    b = Button(window,text = "Rotate",command = rotatenow)
    b.pack()
    window.mainloop()
    
def crop():
    window = Toplevel(root)
    
    def yes(w1):
        global path
        path = 'temp.jpg'
        img.save(path)
        w1.destroy()

    def cropnow():
        global img
        img = Image.open(path)
        width,height = img.size
        dim = (int(e1.get()),int(e2.get()),width-int(e3.get()),height-int(e4.get()))
        img = img.crop(dim)
        w1 = Toplevel(window)
        width, height = img.size
        img = img.resize((width//2, height//2), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(img)
        myvar=Label(w1,image = tkimage)
        myvar.image = tkimage
        l1 = Label(w1,text = "Save?")
        b1 = Button(w1,text = "Yes",command = lambda w1=w1:yes(w1))
        b2 = Button(w1,text = "No",command = w1.destroy)
        l1.pack()
        b1.pack()
        b2.pack()
        myvar.pack()
        w1.mainloop()
    l1 = Label(window,text = "Degrees to crop out the left side")
    l2 = Label(window,text = "Degrees to crop out the upper side")
    l3 = Label(window,text = "Degrees to crop out the right side")
    l4 = Label(window,text = "Degrees to crop out the lower side")
    e1 = Entry(window)
    e2 = Entry(window)
    e3 = Entry(window)
    e4 = Entry(window)
    l1.pack()
    e1.pack()
    l2.pack()
    e2.pack()
    l3.pack()
    e3.pack()
    l4.pack()
    e4.pack()
    b = Button(window,text = "Crop",command = cropnow)
    b.pack()
    window.mainloop()        

def resize():
    window = Toplevel(root)
    
    def yes(w1):
        global path
        path = 'temp.jpg'
        img.save(path)
        w1.destroy()

    def resizenow():
        global img
        img = Image.open(path)
        img = img.resize((int(e1.get()),int(e2.get())))
        w1 = Toplevel(window)
        width, height = img.size
        img = img.resize((width//2, height//2), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(img)
        myvar=Label(w1,image = tkimage)
        myvar.image = tkimage
        l1 = Label(w1,text = "Save?")
        b1 = Button(w1,text = "Yes",command = lambda w1=w1:yes(w1))
        b2 = Button(w1,text = "No",command = w1.destroy)
        l1.pack()
        b1.pack()
        b2.pack()
        myvar.pack()
        w1.mainloop()
    l1 = Label(window,text = "Width to resize to")
    l2 = Label(window,text = "Height to resize to")
    e1 = Entry(window)
    e2 = Entry(window)
    l1.pack()
    e1.pack()
    l2.pack()
    e2.pack()
    b = Button(window,text = "Resize",command = resizenow)
    b.pack()
    window.mainloop()
     
def insert():
    window = Toplevel(root)
    
    def yes(w1):
        global path
        path = 'temp.jpg'
        img.save(path)
        w1.destroy()

    def insertnow():
        global img
        img = Image.open(path)
        img2 = filedialog.askopenfilename(filetypes=[("Image File",'.*')])
        img2 = Image.open(img2)
        img.paste(img2, (int(e1.get()), int(e2.get())))
        w1 = Toplevel(window)
        width, height = img.size
        img = img.resize((width//2, height//2), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(img)
        myvar=Label(w1,image = tkimage)
        myvar.image = tkimage
        l1 = Label(w1,text = "Save?")
        b1 = Button(w1,text = "Yes",command = lambda w1=w1:yes(w1))
        b2 = Button(w1,text = "No",command = w1.destroy)
        l1.pack()
        b1.pack()
        b2.pack()
        myvar.pack()
        w1.mainloop()
    l1 = Label(window,text = "x coordinate to insert new image")
    l2 = Label(window,text = "y coordinate to insert new image")
    e1 = Entry(window)
    e2 = Entry(window)
    l1.pack()
    e1.pack()
    l2.pack()
    e2.pack()
    b = Button(window,text = "Insert",command = insertnow)
    b.pack()
    window.mainloop()
    
    
def transpose():
    window = Toplevel(root)
    
    def yes(w1):
        global path
        path = 'temp.jpg'
        img.save(path)
        w1.destroy()

    def transposenowl():
        global img
        img = Image.open(path)
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        w1 = Toplevel(window)
        width, height = img.size
        img = img.resize((width//2, height//2), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(img)
        myvar=Label(w1,image = tkimage)
        myvar.image = tkimage
        l1 = Label(w1,text = "Save?")
        b1 = Button(w1,text = "Yes",command = lambda w1=w1:yes(w1))
        b2 = Button(w1,text = "No",command = w1.destroy)
        l1.pack()
        b1.pack()
        b2.pack()
        myvar.pack()
        w1.mainloop()
        
    def transposenowt():
        global img
        img = Image.open(path)
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        w1 = Toplevel(window)
        width, height = img.size
        img = img.resize((width//2, height//2), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(img)
        myvar=Label(w1,image = tkimage)
        myvar.image = tkimage
        l1 = Label(w1,text = "Save?")
        b1 = Button(w1,text = "Yes",command = lambda w1=w1:yes(w1))
        b2 = Button(w1,text = "No",command = w1.destroy)
        l1.pack()
        b1.pack()
        b2.pack()
        myvar.pack()
        w1.mainloop()
    b = Button(window,text = "Transpose left-right",command = transposenowl)
    b.pack()
    b1 = Button(window,text = "Transpose top-bottom",command = transposenowt)
    b1.pack()
    window.mainloop()    

def blur():
    window = Toplevel(root)
    
    def yes(window):
        global path
        path = 'temp.jpg'
        img.save(path)
        window.destroy()
       
    l1 = Label(window,text = "Save?")
    b1 = Button(window,text = "Yes",command = lambda window=window:yes(window))
    b2 = Button(window,text = "No",command = window.destroy)
    l1.pack()
    b1.pack()
    b2.pack()
    global img
    img = Image.open(path)
    img = img.filter(ImageFilter.BLUR)
    width, height = img.size
    img = img.resize((width//2, height//2), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(img)
    myvar=Label(window,image = tkimage)
    myvar.image = tkimage
    myvar.pack()
    window.mainloop()

def contour():
    window = Toplevel(root)
    
    def yes(window):
        global path
        path = 'temp.jpg'
        img.save(path)
        window.destroy()
       
    l1 = Label(window,text = "Save?")
    b1 = Button(window,text = "Yes",command = lambda window=window:yes(window))
    b2 = Button(window,text = "No",command = window.destroy)
    l1.pack()
    b1.pack()
    b2.pack()
    global img
    img = Image.open(path)
    img = img.filter(ImageFilter.CONTOUR)
    width, height = img.size
    img = img.resize((width//2, height//2), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(img)
    myvar=Label(window,image = tkimage)
    myvar.image = tkimage
    myvar.pack()
    window.mainloop()



def detail():
    window = Toplevel(root)
    
    def yes(window):
        global path
        path = 'temp.jpg'
        img.save(path)
        window.destroy()
       
    l1 = Label(window,text = "Save?")
    b1 = Button(window,text = "Yes",command = lambda window=window:yes(window))
    b2 = Button(window,text = "No",command = window.destroy)
    l1.pack()
    b1.pack()
    b2.pack()
    global img
    img = Image.open(path)
    img = img.filter(ImageFilter.DETAIL)
    width, height = img.size
    img = img.resize((width//2, height//2), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(img)
    myvar=Label(window,image = tkimage)
    myvar.image = tkimage
    myvar.pack()
    window.mainloop()


def edgeenhance():
    window = Toplevel(root)
    
    def yes(window):
        global path
        path = 'temp.jpg'
        img.save(path)
        window.destroy()
       
    l1 = Label(window,text = "Save?")
    b1 = Button(window,text = "Yes",command = lambda window=window:yes(window))
    b2 = Button(window,text = "No",command = window.destroy)
    l1.pack()
    b1.pack()
    b2.pack()
    global img
    img = Image.open(path)
    img = img.filter(ImageFilter.EDGE_ENHANCE)
    width, height = img.size
    img = img.resize((width//2, height//2), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(img)
    myvar=Label(window,image = tkimage)
    myvar.image = tkimage
    myvar.pack()
    window.mainloop()



def edgeenhancemore():
    window = Toplevel(root)
    
    def yes(window):
        global path
        path = 'temp.jpg'
        img.save(path)
        window.destroy()
       
    l1 = Label(window,text = "Save?")
    b1 = Button(window,text = "Yes",command = lambda window=window:yes(window))
    b2 = Button(window,text = "No",command = window.destroy)
    l1.pack()
    b1.pack()
    b2.pack()
    global img
    img = Image.open(path)
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    width, height = img.size
    img = img.resize((width//2, height//2), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(img)
    myvar=Label(window,image = tkimage)
    myvar.image = tkimage
    myvar.pack()
    window.mainloop()



def emboss():
    window = Toplevel(root)
    
    def yes(window):
        global path
        path = 'temp.jpg'
        img.save(path)
        window.destroy()
       
    l1 = Label(window,text = "Save?")
    b1 = Button(window,text = "Yes",command = lambda window=window:yes(window))
    b2 = Button(window,text = "No",command = window.destroy)
    l1.pack()
    b1.pack()
    b2.pack()
    global img
    img = Image.open(path)
    img = img.filter(ImageFilter.EMBOSS)
    width, height = img.size
    img = img.resize((width//2, height//2), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(img)
    myvar=Label(window,image = tkimage)
    myvar.image = tkimage
    myvar.pack()
    window.mainloop()



def findedges():
    window = Toplevel(root)
    
    def yes(window):
        global path
        path = 'temp.jpg'
        img.save(path)
        window.destroy()
       
    l1 = Label(window,text = "Save?")
    b1 = Button(window,text = "Yes",command = lambda window=window:yes(window))
    b2 = Button(window,text = "No",command = window.destroy)
    l1.pack()
    b1.pack()
    b2.pack()
    global img
    img = Image.open(path)
    img = img.filter(ImageFilter.FIND_EDGES)
    width, height = img.size
    img = img.resize((width//2, height//2), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(img)
    myvar=Label(window,image = tkimage)
    myvar.image = tkimage
    myvar.pack()
    window.mainloop()



def sharpen():
    window = Toplevel(root)
    
    def yes(window):
        global path
        path = 'temp.jpg'
        img.save(path)
        window.destroy()
       
    l1 = Label(window,text = "Save?")
    b1 = Button(window,text = "Yes",command = lambda window=window:yes(window))
    b2 = Button(window,text = "No",command = window.destroy)
    l1.pack()
    b1.pack()
    b2.pack()
    global img
    img = Image.open(path)
    img = img.filter(ImageFilter.SHARPEN)
    width, height = img.size
    img = img.resize((width//2, height//2), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(img)
    myvar=Label(window,image = tkimage)
    myvar.image = tkimage
    myvar.pack()
    window.mainloop()



def smooth():
    window = Toplevel(root)
    
    def yes(window):
        global path
        path = 'temp.jpg'
        img.save(path)
        window.destroy()
       
    l1 = Label(window,text = "Save?")
    b1 = Button(window,text = "Yes",command = lambda window=window:yes(window))
    b2 = Button(window,text = "No",command = window.destroy)
    l1.pack()
    b1.pack()
    b2.pack()
    global img
    img = Image.open(path)
    img = img.filter(ImageFilter.SMOOTH)
    width, height = img.size
    img = img.resize((width//2, height//2), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(img)
    myvar=Label(window,image = tkimage)
    myvar.image = tkimage
    myvar.pack()
    window.mainloop()



def smoothmore():
    window = Toplevel(root)
    
    def yes(window):
        global path
        path = 'temp.jpg'
        img.save(path)
        window.destroy()
       
    l1 = Label(window,text = "Save?")
    b1 = Button(window,text = "Yes",command = lambda window=window:yes(window))
    b2 = Button(window,text = "No",command = window.destroy)
    l1.pack()
    b1.pack()
    b2.pack()
    global img
    img = Image.open(path)
    img = img.filter(ImageFilter.SMOOTH_MORE)
    width, height = img.size
    img = img.resize((width//2, height//2), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(img)
    myvar=Label(window,image = tkimage)
    myvar.image = tkimage
    myvar.pack()
    window.mainloop()
    
def classify():
    from keras.models import load_model
    from keras_preprocessing.image import img_to_array
    import cv2
    import numpy as np 

    path1 = filedialog.askopenfilename(filetypes=[("Image File",'.*')])
    image = cv2.imread(path1)
    model = load_model('my_model.h5')

    image = cv2.resize(image, (100, 100))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    (one, two, three, te, thirty) = model.predict(image)[0]
    max = one
    label = "2"
    outfile='01.jpg'
    if two > max:
        max = two
        label = "1"
    outfile='02.jpg'
    if three > max:
        max = three
        label = "0"
        outfile='03.jpg'
    if te > max:
        max = te
        label = "4"
        outfile='28.jpg'
    if thirty > max:
        max = thirty
        label = "3"
        outfile='30.jpg'
    s = label+" days left till the fruit decays."
    
    window = Toplevel(root)
    l = Label(window, text = s)
    l.grid(padx = 50,pady = 50)


b = Button(root,text = "Estimate age of fruit",command = classify, bg = '#ff0066')
b.grid(row = 0, column=0, padx = 30, pady = 15)

b1 = Button(root,text = "Rotate", command = rotate)
b1.grid(row = 1, column = 0, padx = 30, pady = 15)

b2 = Button(root,text = "Display", command = display)
b2.grid(row = 0, column = 1, padx = 30, pady = 15)

b3 = Button(root,text = "Crop", command = crop)
b3.grid(row = 2, column = 0, padx = 30, pady = 15)

b4 = Button(root,text = "Resize", command = resize)
b4.grid(row = 1, column = 1, padx = 30, pady = 15)

b5 = Button(root,text = "Insert", command = insert)
b5.grid(row = 3, column = 0, padx = 30, pady = 15)

b6 = Button(root,text = "Transpose", command = transpose)
b6.grid(row = 2, column = 1, padx = 30, pady = 15)

b7 = Button(root,text = "Blur", command = blur)
b7.grid(row = 4, column = 0, padx = 30, pady = 15)

b8 = Button(root,text = "Contour", command = contour)
b8.grid(row = 3, column = 1, padx = 30, pady = 15)

b9 = Button(root,text = "Detail", command = detail)
b9.grid(row = 5, column = 0, padx = 30, pady = 15)

b10 = Button(root,text = "Edge Enhance", command = edgeenhance)
b10.grid(row = 4, column = 1, padx = 30, pady = 15)

b11 = Button(root,text = "Edge Enhance More", command = edgeenhancemore)
b11.grid(row = 6, column = 0, padx = 30, pady = 15)

b12 = Button(root,text = "Emboss", command = emboss)
b12.grid(row = 5, column = 1, padx = 30, pady = 15)

b13 = Button(root,text = "Find Edges", command = findedges)
b13.grid(row = 7, column = 0, padx = 30, pady = 15)

b14 = Button(root,text = "Sharpen", command = sharpen)
b14.grid(row = 6, column = 1, padx = 30, pady = 15)

b15 = Button(root,text = "Smooth", command = smooth)
b15.grid(row = 8, column = 0, padx = 30, pady = 15)

b16 = Button(root,text = "Smooth More", command = smoothmore)
b16.grid(row = 7, column = 1, padx = 30, pady = 15)

root.mainloop()
