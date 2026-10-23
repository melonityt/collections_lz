import matplotlib.pyplot as plt
import numpy as np
#делаем подсчёты
x = np.linspace(-5, 5, 100)    #задаём (от, до, кол-во эл.) 
y = np.array(x**2)    

x2 = np.arange(-5,6,1)         #задаём (от, до, с шагом x)
y2 = np.array(x2**2)

ye = np.array(np.e**x)
ye2 = np.array(np.e**x2)

ylog = np.array(np.log(x))
ylog2 = np.array(np.log(x2))

y3 = np.array(x**3)
y33 = np.array(x2**3)

# print(x,y)

plt.title("График функций", color='#173554', fontstyle="italic", fontweight="bold")         #настройки окна
plt.xlabel('Ось х', color='#173554', fontweight="bold") #Подпись для оси х
plt.ylabel('Ось y', color='#173554', fontweight="bold") #Подпись для оси y
ax = plt.gca()
ax.set_facecolor('#fcffff')
plt.gcf().set_facecolor("#fcffff")


plt.plot(x, y, color='#173554', markersize=7)                                       #настройки линии графика x**2
plt.plot(x2, y2, color='#173554', marker='o', markersize=7, linestyle='none')       #настройка точек графика x**2


plt.plot(x, ye, color='#40B336', markersize=7)                                      #настройки линии графика e**x
plt.plot(x2, ye2, color="#40B336", marker='s', markersize=7, linestyle='none')      #настройки линии графика e**x


plt.plot(x, ylog, color="#3010E6", markersize=7)                                    #настройки линии графика log(x)
plt.plot(x2, ylog2, color="#3010E6", marker='x', markersize=7, linestyle='none')    #настройки линии графика log(x)


plt.plot(x, y3, color="#E73718", markersize=7)                                      #настройки линии графика x**3
plt.plot(x2, y33, color="#E73718", marker='d', markersize=7, linestyle='none')      #настройки линии графика x**3








plt.show()


