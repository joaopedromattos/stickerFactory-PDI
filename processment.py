import imageio as im
import numpy as np

class Processment(object):
    def __init__(self, imageName):
        self.mask = np.array(im.imread("mask.png"))
        self.image = np.array(im.imread(imageName))
        self.setup()
    
    def setup(self):
        # Normalizacao
        self.mask[:,:,0] = ((self.mask[:,:,0] - self.mask[:,:,0].min())/(self.mask[:,:,0].max()-self.mask[:,:,0].min()))
        self.mask[:,:,0] = 1 - self.mask[:,:,0]

        # Segmentando a imagem
        if (len(self.image.shape) == 2): # Este if sera executado se a imagem tiver apenas uma camada.
            self.to_rgba()
            print(self.image.shape)
        else: # Para a maioria das imagens, este 'else' sera executado
            for i in range(self.image.shape[-1]):
                self.image[:,:,i] = self.image[:,:,i]*self.mask[:,:,0]
            print(self.image.shape)
        im.imwrite("sticker.png", self.image)

    def to_rgba(self):
        # as 3a, but we add an extra copy to contiguous 'C' order
        # data
        self.image = np.dstack([self.image] * 4).copy(order='C')

        # self.image[0].fill(255)
        # self.image[:,:,0] = (self.image[:,:,3] + self.image[:,:,0] + self.image[:,:,2] + self.image[:,:,1])*self.mask[:,:,0]
        # self.image[:,:,1] = (self.image[:,:,3] + self.image[:,:,0] + self.image[:,:,2] + self.image[:,:,1])*self.mask[:,:,0]
        # self.image[:,:,2] = (self.image[:,:,3] + self.image[:,:,0] + self.image[:,:,2] + self.image[:,:,1])*self.mask[:,:,0]
        self.image[:,:,3] = (self.image[:,:,3] + self.image[:,:,0] + self.image[:,:,2] + self.image[:,:,1])*self.mask[:,:,0]
        





