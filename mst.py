import math 
import sys

class no:
    def __init__(self,a,b):
        self.dist = a;
        self.pos = b
        
class grafo:
    def __init__(self, sizeH,sizeV,valores):
        self.sizeV = sizeV
        self.sizeH = sizeH
        self.valores = [[(valores[x][y][0]+valores[x][y][1]+valores[x][y][2])/3 for x in range(sizeH)] for y in range(sizeV)]

    def prim(self,pos1,pos2):
        #2 caso nao definido
        #1 caso ligado a ponto pos2 e visitado
        #0 caso ligado a ponto pos1 e visitado
        #-1 caso ligado a ponto pos2 e nao visitado
        #-2  caso ligado a ponto pos1 e nao visitado
        mascara = [[2]*self.sizeH  for x in range(self.sizeV)]
        mascara[pos1[0]][pos1[1]] = -2
        mascara[pos2[0]][pos2[1]] = -1
        distancia = [no(0,pos1),no(0,pos2)]


        #realizando prim
        for teste in range(self.sizeH*self.sizeV ):
            print(teste)
            
            aux = distancia[0]
 
            #atualizando mascara
            if(mascara[aux.pos[0]][aux.pos[1]] == -1):
                mascara[aux.pos[0]][aux.pos[1]] = 1
            else:
                mascara[aux.pos[0]][aux.pos[1]] = 0

            #visitando nodos do lado
            if aux.pos[0] > 0:
                if aux.pos[1] > 0:
                    self.atualizarValores(aux,-1,-1,mascara,distancia)
                if(aux.pos[1] < self.sizeV-1):
                    self.atualizarValores(aux,-1,1,mascara,distancia)
            if(aux.pos[0] < self.sizeH-1):
                if aux.pos[1] > 0:
                    self.atualizarValores(aux,1,-1,mascara,distancia)
                if(aux.pos[1] < self.sizeV-1):
                    self.atualizarValores(aux,1,1,mascara,distancia) 

            #arrumando priority queue de menor distancias
            sorted(distancia, key=lambda no: no.dist) 

        return mascara



    def atualizarValores(self, aux,x,y,mascara,distancia):
        #caso já vizinado, nao atualize
        if mascara[aux.pos[0]+x][aux.pos[1]+y] == 1 or mascara[aux.pos[0]+x][aux.pos[1]+y] == 0:
            return


        #procurando caso nó está dentro do vetor distância
        for novoNo in distancia:
            if novoNo.pos == (aux.pos[0]+x,aux.pos[1]+y):
                a = novoNo
                break
            else:
                a = None

        #caso sim, remova-o
        if a != None:
            distancia.remove(a)

        #definindo nova distancia
        newDistance = aux.dist + abs(self.valores[aux.pos[0]][aux.pos[1]] - self.valores[aux.pos[0]+x][aux.pos[1]+y])

        #atualizando valores da mescara
        if a == None or newDistance < a.dist:
            if(mascara[aux.pos[0]][aux.pos[1]] == 1):
                mascara[aux.pos[0]+x][aux.pos[1]+y] = -1
            else:
                mascara[aux.pos[0]+x][aux.pos[1]+y] = -2

        #colocando-o no vetor de distancias
        distancia.append(no(newDistance,(aux.pos[0]+x,aux.pos[1]+y)))