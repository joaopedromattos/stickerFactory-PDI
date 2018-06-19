# Este código é aberto e pode ser encontrado em : https://gist.github.com/nikhilkumarsingh/85501ee2c3d8c0cfa9d1a27be5781f06

from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
from PIL import Image, ImageDraw
from processment import Processment


class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self, imagePath):

        # Cores base
        self.white = (255, 255, 255)
        self.green = (0,128,0)


        # Modifiquei essa linha
        # self.root = Tk()
        self.root = Toplevel()


        self.rectangle_button = Button(self.root, text='Rectangle', command=self.use_rectangle)
        self.rectangle_button.grid(row=0, column=0)
       
        self.pen_button = Button(self.root, text='pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=1)

        self.color_button = Button(self.root, text='color', command=self.choose_color)
        self.color_button.grid(row=0, column=2)

        self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=3)

        self.choose_size_button = Scale(self.root, from_=15, to=40, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=4)

        # Adicionei o seguinte botao
        self.save_button = Button(self.root, text='save', command=self.save)
        self.save_button.grid(row=0, column=5)
        

        # Adicionei esse parametro
        self.imageName = imagePath
        
        # Eu adicionei essa linha para que a imagem de fundo aparecesse
        self.image = PhotoImage(file=self.imageName)

        # Modifiquei essa linha tambem para adaptar o tamanho da janela
        self.c = Canvas(self.root, width=self.image.width(), height=self.image.height())
        self.create_image = self.c.create_image(0,0, anchor=NW,image=self.image) # Eu adicionei essa linha. Fe em deus que funciona
        self.c.grid(row=1, columnspan=6)    

        # Adicionei essas duas linhas para salvar a mascara
        self.preSavedMask = Image.new("RGB", (self.image.width(), self.image.height()), self.white)
        self.preSavedDraw = ImageDraw.Draw(self.preSavedMask)


        # Posicao a partir da qual o user comecara a mover o mouse
        self.start_x = None
        self.start_y = None

        # Inicio do sistema de coordenadas.
        self.x = self.y = 0

        self.rect = None

        self.rectDim = ()


        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
        

    def use_pen(self):
        self.activate_button(self.pen_button)
    
    # Adicionei o metodo abaixo
    def use_rectangle(self):
        self.activate_button(self.rectangle_button, recMode=True)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False, recMode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode
        if (recMode):
            self.c.bind("<ButtonPress-1>", self.on_button_press)
            self.c.bind("<B1-Motion>", self.on_move_press)
            self.c.bind("<ButtonRelease-1>", self.on_button_release)
    
    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
            
            # Adicionei a seguinte linha para fazer a mascara
            self.preSavedDraw.line([(self.old_x, self.old_y), (event.x, event.y)], fill=(0, 0, 0), width=self.line_width)
            # self.preSavedDraw.ellipse([(self.old_x, self.old_y), (event.x, event.y)], fill=(0, 0, 0))
            # self.preSavedDraw.chord([(self.old_x, self.old_y), (event.x, event.y)], fill=(0, 0, 0))


        self.old_x = event.x
        self.old_y = event.y

    # Para salvar a mascara, adicionei a funcao
    def save(self):        
        filename = "mask.png"
        self.preSavedMask.save(filename)

        # Inicio o uso da classe contida no arquivo "processment.py"
        Processment(self.imageName, self.rectDim)


    # Adicionei o codigo abaixo
    def reset(self, event):
        self.old_x, self.old_y = None, None

    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = event.x
        self.start_y = event.y

        # create rectangle if not yet exist
        #if not self.rect:
        self.rect = self.c.create_rectangle(self.x, self.y, 1, 1, fill="")

    def on_move_press(self, event):
        curX, curY = (event.x, event.y)

        # expand rectangle as you drag the mouse
        self.c.coords(self.rect, self.start_x, self.start_y, curX, curY)
        
        self.rectDim = (self.start_x, self.start_y, curX, curY)


    def on_button_release(self, event):
        pass

