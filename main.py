import matplotlib.pyplot as plt

vetorX=[0,  1,  2,  3,  4,  5]
vetorY=[9.8,9.9,9.8,9.7,9.6,9.5]

#calculo de 'a':

#calculo das medias
mediaX=sum(vetorX)/len(vetorX)
#print('media de x: '+str(mediaX))

mediaY=sum(vetorY)/len(vetorY)
#print('media de y: '+str(mediaY)+'\n')

#separar a formula em duas partes(numerador e denominador) para ficar mais simples
numerador=0
for i in vetorX:
  numerador+= (vetorX[i]-mediaX)*(vetorY[i]-mediaY)

denominador=0
for i in vetorX:
  denominador+= (vetorX[i]-mediaX)**2

a=numerador/denominador

#calculo de 'b': (b=mediaY - mediaX*a)

b= mediaY - mediaX*a

print('a = '+str(a))
print('b = '+str(b))

plt.plot(vetorX,vetorY)

yy=[]
#for i in vetorX:
#  yy[i]=a*vetorX[i]+b

#plt.plot(x,y,)
