from tkinter import filedialog
import tkinter as tk

#Importando las librerias del modelo resnet50
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input, decode_predictions
from keras.preprocessing import image
#Ciencias de datos?
import numpy as np
#Para rular por el directorio de datos
import zipfile
import os
#Librerías que nos ayudaran a mostrar imagenes
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import ImageTk,Image
#creamos nuestro modelo
model = VGG16(weights='imagenet')


class Window(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.prompt = tk.Label(self, text="Elige tu imagen: ", anchor="w")
        self.up = tk.Button(self, text="Subir img", command = self.subir)
        self.pred = tk.Button(self, text="Predecir", command = self.predict)
        self.output = tk.Label(self, text="")
        #self.img = tk.Image()

   
        self.prompt.pack(side="top", fill="x")
        self.output.pack(side="top", fill="x", expand=True)
        self.up.pack(side="right")
        self.pred.pack(side="right")
    
    def subir(self):
        self.filename =  filedialog.askopenfilename(initialdir = "D:\trigo\Escritorio\GIT HUB\DSC-UPV\COSAS\Talleres\TransferLearning\Data\Train\cat",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        print("HI:", self.filename)
        url = self.filename
        #self.output = tk.Label(self, text=prediccion(path= url))
        # print(prediccion(path= url))
    
    def predict(self):
        img_path = self.filename
        print('PATH: ',img_path)
        img1 = Image.open(img_path)
        img = img1.resize((224,224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        #predecimos la salida usando el modelo
        predicciones = model.predict(x)
        #decodificamos nuestra salida en tuplas
        [(clase, descripcion, probabilidad),
        (clase1, descripcion1, probabilidad1),
        (clase2, descripcion2, probabilidad2)] = decode_predictions(predicciones, top=3)[0]

        img = ImageTk.PhotoImage(img)
        panel = tk.Label(root, image=img)
        panel.image = img
        panel.pack()

        #mostramos la prediccion por pantalla
        print('=========================================PREDICCION=========================================\n')
        print("Es un: <",descripcion, "> con una probabilidad de: <", "{:.3f}".format(probabilidad*100),"%>\n")
        print("Es un: <",descripcion1, "> con una probabilidad de: <", "{:.3f}".format(probabilidad1*100),"%>\n")
        print("Es un: <",descripcion2, "> con una probabilidad de: <", "{:.3f}".format(probabilidad2*100),"%>\n")
        print('============================================================================================\n')

        t = ("=========================================PREDICCION=========================================" +"\n"+
            "Es un: <" + descripcion + "> con una probabilidad de: <" + "{:.3f}".format(probabilidad*100)+"%>"+"\n"+
            "Es un: <" +descripcion1+ "> con una probabilidad de: <" +"{:.3f}".format(probabilidad1*100)+"%>"+"\n"+
            "Es un: <"+ descripcion2+ "> con una probabilidad de: <"+ "{:.3f}".format(probabilidad2*100)+"%>"+"\n"+
            "============================================================================================\n")

        #t = "Es un: <" + descripcion + "> con una probabilidad de: <" + "{:.3f}".format(probabilidad*100)+"%>"
        self.output = tk.Label(self,  text = t)
       # self.output.pack(side="bottom", fill="x", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x500+300+150")
    root.resizable(width=True, height=True)
    Window(root).pack(fill="both",expand=True)
    root.mainloop()