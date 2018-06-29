import imageio as im
import numpy as np
import cv2 
from mst import grafo



class Processment(object):
    def __init__(self, imageName, auto=0, rectangle=(0,0,0,0), seed1=None, seed2=None, useArea = 1, usePaint = 0):
        try:
            self.mask = np.array(im.imread("mask.png"))
            
            self.region = rectangle
            print(rectangle)
        except:
            self.mask = None

        if (auto==0):
            self.image = cv2.imread(imageName)
        elif (auto == 1):
            self.image = np.array(im.imread(imageName))
        
        # Seeds que sao usadas no caso de o user ter selecionado a opcao de 'Automatic segmentation'
        self.pixel1 = seed1
        self.pixel2 = seed2

        self.useArea = useArea
        self.usePaint = usePaint

        # Metodo utilizado para realizar o processamento
        self.setup(auto)
    
    def setup(self, auto):
        if (auto == 0):       
    

            if (self.useArea):

                # Abaixo ocorre a segmentacao da imagem contida dentro do retangulo definido pelo usuario
                # Cria uma mascara vazia para receber os dados do grabCut
                mask = np.zeros(self.image.shape[:2],np.uint8)
                # Modelos de background utilizados pela biblioteca 
                bgdModel = np.zeros((1,65),np.float64)
                fgdModel = np.zeros((1,65),np.float64)
                # Realiza o metodo de segmentacao graphCut para a mascara 'mask' concedida como input
                cv2.grabCut(self.image, mask,self.region,bgdModel,fgdModel,1,cv2.GC_INIT_WITH_RECT)
                # Normalizamos a mascara para realizar a multiplicacao pixel a pixel dela com a imagem 
                mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
                # Realiza a segmentacao da imagem(multiplicacao pixel a pixel)
                # a partir da mascara que o grab cut retorna
                self.image = cv2.bitwise_and(self.image,self.image,mask=mask2) 


            
            # Salvamos e exibimos a imagem
            cv2.imwrite("sticker.png", self.image)

        elif (auto == 1):
            
            graph = grafo(self.image.shape[0],self.image.shape[1], self.image)

            mask = graph.prim(self.pixel1, self.pixel2)

            print(self.image.shape)

            self.image[:,:,0] = self.image[:,:,0] * np.array(mask).transpose()
            self.image[:,:,1] = self.image[:,:,1] * np.array(mask).transpose()
            self.image[:,:,2] = self.image[:,:,2] * np.array(mask).transpose()
            cv2.imwrite("sticker.png", self.image)



            

    

    # Metodo que converte as imagens '.png' com apenas um canal para imagens '.png' com tres canais
    def to_rgba(self):
        # as 3a, but we add an extra copy to contiguous 'C' order
        # data
        self.image = np.dstack([self.image] * 4).copy(order='C')

        # self.image[0].fill(255)
        # self.image[:,:,0] = (self.image[:,:,3] + self.image[:,:,0] + self.image[:,:,2] + self.image[:,:,1])*self.mask[:,:,0]
        # self.image[:,:,1] = (self.image[:,:,3] + self.image[:,:,0] + self.image[:,:,2] + self.image[:,:,1])*self.mask[:,:,0]
        # self.image[:,:,2] = (self.image[:,:,3] + self.image[:,:,0] + self.image[:,:,2] + self.image[:,:,1])*self.mask[:,:,0]
        self.image[:,:,3] = (self.image[:,:,3] + self.image[:,:,0] + self.image[:,:,2] + self.image[:,:,1])*self.mask[:,:,0]
        
