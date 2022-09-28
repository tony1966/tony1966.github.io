import matplotlib.pyplot as plt
import numpy as np

fig1=plt.figure()                      
x=np.linspace(0, 2*np.pi, 360)       
y=np.sin(x)      
plt.plot(x, y, 'b-', lw=2)             
plt.grid()
fig2=plt.figure('fig2', figsize=(8, 6), dpi=72, facecolor='#FFD700', edgecolor='blue')         
plt.plot(x, y, 'g-', lw=2)              
plt.grid()
plt.show()           