
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def get_bootstrap(x, n_sample):
    sample = np.random.choice(x, size = (x.size, n_sample), replace = True)
    return sample

#Выборку смотреть в excel
a = "0,069 0,093 0,158 0,199 0,339 0,385 0,388 0,452 0,482 0,517 0,543 0,648 0,719 0,735 0,789 0,944 0,996 1,071 1,136 1,297 1,888 2,125 2,306 3,291 3,585"
a = a.replace(',','.')

x = list(map(float, a.split(' ')))
x = np.array(x)

n_full=1000
k = round(1+np.log2(n_full))

x_boot = get_bootstrap(x, n_full)
x_boot_mean = np.mean(x_boot, axis = 0)
l = np.max(x_boot_mean) - np.min(x_boot_mean)
delta = l/k
sns.distplot(x_boot_mean, color='blue', bins = k, kde = True, label = 'bootstrap')

mu = np.mean(x)
sigma =  ((np.mean((x - mu) ** 2)) / np.size(x)) ** 0.5
x_mean = np.linspace(mu - 3 * sigma, mu + 3 * sigma, n_full)
plt.plot(x_mean, stats.norm.pdf(x_mean, mu, sigma), color='black', label = 'ЦПТ')


plt.title('~_mean')
plt.xlabel('x', loc='right')
plt.ylabel('~_P(x)', loc='top')
plt.grid()
plt.legend()
plt.show()