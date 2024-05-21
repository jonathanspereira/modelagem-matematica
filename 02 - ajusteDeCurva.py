# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:38:28 2024

METODO DOS MINIMOS QUADRADOS EM PYTHON - MODELAGEM MATEMATICA

@author: rafael
"""
import matplotlib.pyplot as plt
import numpy as np


#Entrada dos dados discretos
xi=np.array([0,1,2,3,4,5])
yi=np.array([3,4,7,12,19,28])

##RESULTADO USANDO A FUNCAO NATIVA POLYFIT
coef=np.polyfit(xi,yi,2)
p=np.poly1d(coef)


##METODO TRADICIONAL ENTRADA VALORES
#Definindo as funções g
g1=xi**2
g2=xi
g3=np.ones_like(xi)

#Composição da Matriz A
A=np.zeros([3,3])
A[0,0]=np.dot(g1,g1)
A[0,1]=np.dot(g1,g2)
A[0,2]=np.dot(g1,g3)

A[1,0]=np.dot(g2,g1)
A[1,1]=np.dot(g2,g2)
A[1,2]=np.dot(g2,g3)

A[2,0]=np.dot(g3,g1)
A[2,1]=np.dot(g3,g2)
A[2,2]=np.dot(g3,g3)

#Definindo o Vetor B
b=np.zeros([3])
b[0]=np.dot(yi,g1)
b[1]=np.dot(yi,g2)
b[2]=np.dot(yi,g3)

#Resultado Vetor alpha
alpha=np.linalg.solve(A,b)

#Plotagem dos resultados
x=np.arange(min(xi),max(xi),0.01)
g1x=x**2
g2x=x
g3x=np.ones_like(x)
phi=alpha[0]*g1x+alpha[1]*g2x+alpha[2]*g3x

f,ax=plt.subplots(1,1)

ax.plot(xi,yi,'or',linewidth=0.15,label="Dados discretos")
ax.plot(x,phi,'b-',linewidth=1,label="\u03C6 (x)")
ax.plot(x,p(x),'g-',linewidth=0.5,label="Nativa")
ax.legend()
ax.grid(True)
ax.set_xlabel('x')
ax.set_ylabel('y=f(x)')
plt.xlim([min(xi),max(xi)])

print("\nCoeficientes obtidos pelo ajuste de curva - Tradicional:")
print(alpha)
print("\nCoeficientes obtidos pelo ajusre de curva - Função Nativa:")
print(coef)

plt.show()
