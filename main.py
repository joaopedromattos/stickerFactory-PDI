from tkinter import *
from tkinter import ttk
from tkinter import Toplevel
from paint import Paint
from pixelSel import pixelSel   
import cv2


# Variavel que testa se o user clicou no campo do diretorio
firstclick = True


# Funcao que apaga o lable quando o user clica
def on_entry_click(event):
    global firstclick

    if firstclick: # Se essa e a primeira vez que o user clicou no Entry...
        firstclick = False
        ed.delete(0, "end") # ...entao delete todo o texto escrito nele.


# Exibe a imagem depois de apertado o botao de segmentacao automatica para selecao de seed
def autoSegCanvas():
    try:

        imagemNomeConservado = ed.get()
        formato = imagemNomeConservado.split(".")
        try:
            if (formato[1] != 'png'):
                img = cv2.imread(imagemNomeConservado)
                
                cv2.imwrite(formato[0] + ".png", img, [cv2.IMWRITE_PNG_COMPRESSION])
                imagemNomeConservado = formato[0] + ".png"
                
            pixelSel(imagemNomeConservado)
        except(IndexError):
            lb = Label(window, text="IMAGEM NAO ENCONTRADA OU DE FORMATO INVALIDO")
            lb.pack()
            return 0    

    except(TclError):
        lb = Label(window, text="IMAGEM NAO ENCONTRADA OU DE FORMATO INVALIDO")
        lb.pack()
        return 0

# Exibe a imagem para selecao de objeto na selecao semi-automatica
def semiSegCanvas():
    try:
        
        imagemNomeConservado = ed.get()
        formato = imagemNomeConservado.split(".")
        try:
            if (formato[1] != 'png'):
                img = cv2.imread(imagemNomeConservado)
                
                cv2.imwrite(formato[0] + ".png", img, [cv2.IMWRITE_PNG_COMPRESSION])
                imagemNomeConservado = formato[0] + ".png"
                
            Paint(imagemNomeConservado)

        except(IndexError):
            lb = Label(window, text="IMAGEM NAO ENCONTRADA OU DE FORMATO INVALIDO")
            lb.pack()
            return 0    

    except(TclError):
        lb = Label(window, text="IMAGEM NAO ENCONTRADA OU DE FORMATO INVALIDO")
        lb.pack()
        return 0


# Janela principal do programa e' criada aqui 
window = Tk()
window.style = ttk.Style()
window.style.theme_use("alt")
window.title('Sticker Factory')

frame = Frame(window) # Frame dos botoes para deixa-los lado a lado



# Instanciamento do campo do diretorio da imagem
ed = Entry(window, width=95)
ed.insert(0, "Insira o diretório da imagem")
ed.bind('<FocusIn>', on_entry_click)
ed.config(fg = 'grey')



# Instanciamento do botao de carregamento da imagem para exibicao
autoSeg = Button(frame, text='Automatic segmentation', command=autoSegCanvas)
# autoSeg.grid(row=0, column=0)
semiSeg = Button(frame, text='Semi-automatic segmentation', command=semiSegCanvas)
# semiSeg.grid(row=0, column=1)


# Exibicao do conteudo em loop ate que o user tome alguma decisao do que vai fazer da vida
ed.pack()
autoSeg.pack(side=LEFT)
semiSeg.pack(side=RIGHT)
frame.pack(side=BOTTOM)
window.mainloop()
