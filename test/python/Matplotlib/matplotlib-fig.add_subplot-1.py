import matplotlib.pyplot as plt    
fig=plt.figure()   
ax=fig.add_subplot()     
type(ax)     
ax.plot([7, 1, 2, 3, 8, 4, 5, 3, 6, 1])     
fig.axes      
ax.set_xlabel('X')     
ax.set_ylabel('Y')       
ax.set_title('Demo')     
plt.show()    
                