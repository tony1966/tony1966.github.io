import matplotlib.pyplot as plt

plt.style.use('seaborn')
week=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
temperature=[25.4, 23.7, 28.6, 29.2, 24.8, 22.5, 21.9]
plt.plot(week, temperature)
plt.title('Temperature Change')                      
plt.xlabel('Weekday')                                                 
plt.ylabel('Celsius')  
plt.show()