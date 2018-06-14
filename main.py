from tkinter import *
from tkinter import ttk
from tkinter import Toplevel
from paint import Paint
import cv2





# Variavel que testa se o user clicou no campo do diretorio
firstclick = True


# Funcao que apaga o lable quando o user clica
def on_entry_click(event):
    global firstclick

    if firstclick: # Se essa e a primeira vez que o user clicou no Entry...
        firstclick = False
        ed.delete(0, "end") # ...entao delete todo o texto escrito nele.


# Exibe a imagem depois de apertado o botao
def newCanvas():
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
# window.geometry('400x40')


# Instanciamento do campo do diretorio da imagem
ed = Entry(window, width=95)
ed.insert(0, "Insira o diretório da imagem")
ed.bind('<FocusIn>', on_entry_click)
ed.config(fg = 'grey')



# Instanciamento do botao de carregamento da imagem para exibicao
loadImageBtn = Button(window, text='Carregar imagem', command=newCanvas)

# Exibicao do conteudo em loop ate que o user tome alguma decisao do que vai fazer da vida
ed.pack()
loadImageBtn.pack()
window.mainloop()
