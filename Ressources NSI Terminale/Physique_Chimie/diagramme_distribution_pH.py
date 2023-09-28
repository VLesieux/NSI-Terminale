import matplotlib.pyplot as plt
import numpy as np

########################  choix des axes et représentation   ####################################
plt.axis([0, 14, 0, 100])
plt.title("Diagramme de distribution HA/A-")
plt.xlabel("pH")
plt.ylabel("%")
########################   modélisation linéaire et représentation  ##################################################
pKA=4.8
x = np.linspace(0, 14 , 200)#200 est le nombre de points
y=100*(1/(1+10**(x-pKA)))
titre="% HA"
plt.plot(x,y,"r,-",label=titre)
plt.legend(loc='upper left')
x = np.linspace(0, 14 , 200)#200 est le nombre de points
z=100-y
titre="% A-"
plt.plot(x,z,"r,:",label=titre)
plt.legend(loc='upper right')
################################################################################
plt.show()
plt.close()
