import matplotlib.pyplot as plt  
fig=plt.figure()    
ax=fig.add_axes([0.1, 0.1, 0.8, 0.8])   
ax.plot([7, 1, 2, 3, 8, 4, 5, 3, 6, 1])          
ax.set_xlabel('X')            
ax.set_ylabel('Y')            
ax.set_title('Demo')        
plt.show()           