# Este código é aberto e pode ser encontrado em seu formato original em : 
# https://gist.github.com/nikhilkumarsingh/85501ee2c3d8c0cfa9d1a27be5781f06

from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
from PIL import Image, ImageDraw
from processment import Processment


class pixelSel(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self, imagePath):

        self.errorShown = False
        # Cores base
        self.white = (255, 255, 255)
        self.green = (0,128,0)


        # Modifiquei essa linha
        self.root = Toplevel()



        self.firstSeed = Button(self.root, text='Background', command=self.use_FirstSeed)
        self.firstSeed.grid(row=0, column=0)
    
        self.secondSeed = Button(self.root, text='Foreground', command=self.use_SecondSeed)
        self.secondSeed.grid(row=0, column=1)

        # Adicionei o seguinte botao
        self.save_button = Button(self.root, text='Start Segmentation', command=self.save)
        self.save_button.grid(row=0, column=2)
        

        # Adicionei esse parametro
        self.imageName = imagePath
        
        # Eu adicionei essa linha para que a imagem de fundo aparecesse
        self.image = PhotoImage(file=self.imageName)

        # Modifiquei essa linha tambem para adaptar o tamanho da janela
        self.c = Canvas(self.root, width=self.image.width(), height=self.image.height())
        self.create_image = self.c.create_image(0,0, anchor=NW,image=self.image) # Eu adicionei essa linha.
        self.c.grid(row=1, columnspan=3)    
        


        # Posicao a partir da qual o user comecara a mover o mouse
        self.start_x = None
        self.start_y = None

        # Inicio do sistema de coordenadas.
        self.x = self.y = 0

        self.seed1 = None
        self.seed2 = None

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.color = self.DEFAULT_COLOR
        self.active_button = self.firstSeed
        self.c.bind('<Button-1>', self.paint)


    def use_FirstSeed(self):
        self.activate_button(self.firstSeed)

    def use_SecondSeed(self):
        self.activate_button(self.secondSeed)       


    def activate_button(self, some_button):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
    
    def paint(self, event):
        if self.old_x and self.old_y:
            if (self.active_button == self.firstSeed):
                self.seed1 = (event.x, event.y)
            if (self.active_button == self.secondSeed):
                self.seed2 = (event.x, event.y)    
            print("Seed 1: " + str(self.seed1))
            print("Seed 2: " + str(self.seed2))        

        self.old_x = event.x
        self.old_y = event.y

    # Para salvar a mascara, adicionei a funcao
    def save(self):        
        if (self.seed1 != None and self.seed2 != None):
            # Inicio o uso da classe contida no arquivo "processment.py"
            Processment(self.imageName, auto=1, seed1=self.seed1, seed2=self.seed2)
        else:
            if (self.errorShown == False):
                print("Error! Please select the other seed!")
                self.errorShown = True
        self.root.destroy()       
