import imageio as im
import numpy as np
import cv2 
from matplotlib import pyplot as plt
class Processment(object):
    def __init__(self, imageName, rectangle):
        self.mask = np.array(im.imread("mask.png"))
        self.image = np.array(im.imread(imageName))
        # self.image = cv2.imread(imageName)
        self.region = rectangle
        self.setup()
    
    def setup(self):
        # Normalizacao
        self.mask[:,:,0] = ((self.mask[:,:,0] - self.mask[:,:,0].min())/(self.mask[:,:,0].max()-self.mask[:,:,0].min()))
        self.mask[:,:,0] = 1 - self.mask[:,:,0]

        # Segmentando a imagem
        # Algumas imagens png possuem apenas uma camada de cinza; nesses casos, o if abaixo e realizado
        if (len(self.image.shape) == 2): 
            self.to_rgba()
            print(self.image.shape)
        else: # Para a maioria das imagens, este 'else' sera executado
            for i in range(self.image.shape[-1]):
                self.image[:,:,i] = self.image[:,:,i]*self.mask[:,:,0]
            print(self.image.shape)
        im.imwrite("sticker.png", self.image)

        # mask = np.zeros(self.image.shape[:2],np.uint8)

        # bgdModel = np.zeros((1,65),np.float64)
        # fgdModel = np.zeros((1,65),np.float64)

        # cv2.grabCut(self.image, mask,self.region,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

        # mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
        # self.image = self.image*mask2[:,:,np.newaxis]


        # cv2.imwrite("sticker.png", self.image)
        # self.image = self.image[:,:,::-1]
        # plt.imshow(self.image, cmap='hsv'),plt.colorbar(),plt.show()
    def to_rgba(self):
        # as 3a, but we add an extra copy to contiguous 'C' order
        # data
        self.image = np.dstack([self.image] * 4).copy(order='C')

        # self.image[0].fill(255)
        # self.image[:,:,0] = (self.image[:,:,3] + self.image[:,:,0] + self.image[:,:,2] + self.image[:,:,1])*self.mask[:,:,0]
        # self.image[:,:,1] = (self.image[:,:,3] + self.image[:,:,0] + self.image[:,:,2] + self.image[:,:,1])*self.mask[:,:,0]
        # self.image[:,:,2] = (self.image[:,:,3] + self.image[:,:,0] + self.image[:,:,2] + self.image[:,:,1])*self.mask[:,:,0]
        self.image[:,:,3] = (self.image[:,:,3] + self.image[:,:,0] + self.image[:,:,2] + self.image[:,:,1])*self.mask[:,:,0]
        





