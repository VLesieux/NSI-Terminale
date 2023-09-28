import matplotlib.pyplot as plt
import numpy as np
import math
########################  choix des axes et représentation   ####################################
plt.axis([0, 20, 0, 14])
plt.title("Courbe de titrage pH-métrique")
plt.xlabel("Vb")
plt.ylabel("pH")
########################   modélisation linéaire et représentation  ##################################################
pKA=4.8
x = np.linspace(0, 10, 200)#200 est le nombre de points
y=pKA+np.log10(x/(10-x))
plt.plot(x,y,"r,-")
x = np.linspace(10, 20 , 200)#200 est le nombre de points
y=14+np.log10((0.1*x-0.1*10)/(10+x))
plt.plot(x,y,"r,-")
################################################################################
plt.show()
plt.close()

