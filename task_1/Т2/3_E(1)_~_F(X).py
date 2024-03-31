
import numpy as np
import matplotlib.pyplot as plt

lambda_param = 1


a = "0 0,069 0,093 0,158 0,199 0,339 0,385 0,388 0,452 0,482 0,517 0,543 0,648 0,719 0,735 0,789 0,944 0,996 1,071 1,136 1,297 1,888 2,125 2,306 3,291 3,585"
a = a.replace(',','.')

x =list(map(float, a.split(' ')))
x=np.array(x)

cdf = 1 - np.exp(-lambda_param * x)

for i in range(len(x)-1):
    plt.hlines(cdf[i], x[i], x[i+1], colors='r')
    plt.scatter(x[i], cdf[i], facecolors='none', edgecolors='r')

plt.hlines(1, x[-1], x[-1]*1.1, colors='r')
plt.scatter(x[-1], 1, facecolors='none', edgecolors='r')
plt.scatter(x[0], cdf[0], color='r')

plt.title('Эмпирическая функция распределения')
plt.xlabel('x', loc='right')
plt.xticks(np.arange(0, x[-1]*1.1, 0.2))
plt.xlim(0, x[-1]*1.1)
plt.ylabel('~_F(x)', loc='top')
plt.yticks(np.arange(0, 1.05, 0.05))
plt.ylim(0, 1.05)
plt.grid()
plt.show()
