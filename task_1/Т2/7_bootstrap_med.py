import numpy as np
from scipy import stats
from math import comb
import matplotlib.pyplot as plt
import seaborn as sns

def get_bootstrap(x, n_sample):
    sample = np.random.choice(x, size = (x.size, n_sample), replace = True)
    return sample

a = "0,069 0,093 0,158 0,199 0,339 0,385 0,388 0,452 0,482 0,517 0,543 0,648 0,719 0,735 0,789 0,944 0,996 1,071 1,136 1,297 1,888 2,125 2,306 3,291 3,585"
a = a.replace(',','.')

x = list(map(float, a.split(' ')))
x = np.array(x)

n_full=1000
k = round(1+np.log2(n_full))
m_lambda = 1

x_boot = get_bootstrap(x, n_full)
x_boot_med = np.median(x_boot, axis = 0)
l = np.max(x_boot_med) - np.min(x_boot_med)
delta = l/k
sns.distplot(x_boot_med, color='green', bins = k, kde = True, label = 'bootstrap')

i_med = len(x)//2+1 if len(x)%2!=0 else 0
x_med = np.linspace(np.min(x), np.max(x), n_full)
plt.plot(x_med, len(x) * np.exp(-x_med) * comb(len(x)-1, i_med-1) * np.exp(-x_med)**(i_med-1) * (1 - np.exp(-x_med))**(len(x) - i_med),
        color='black', label = 'ЦПТ')   

plt.title('Bootstrap для медианы и сравнение его с ЦПТ для медианы')
plt.xlabel('x', loc='right')
plt.ylabel('~_P(x)', loc='top')
plt.grid()
plt.legend()
plt.show()