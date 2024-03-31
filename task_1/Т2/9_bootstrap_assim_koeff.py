import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def get_bootstrap(x, n_sample):
    sample = np.random.choice(x, size = (x.size, n_sample), replace = True)
    return sample

def mu_3_i(arr_i):
    mu_3_i = 0
    x_mean_i = np.mean(arr_i)
    for jj in range(len(arr_i)):
        mu_3_i += (arr_i[jj] - x_mean_i)**3
    return mu_3_i/len(arr_i)

a = "0,069 0,093 0,158 0,199 0,339 0,385 0,388 0,452 0,482 0,517 0,543 0,648 0,719 0,735 0,789 0,944 0,996 1,071 1,136 1,297 1,888 2,125 2,306 3,291 3,585"
a = a.replace(',','.')

x = list(map(float, a.split(' ')))
x = np.array(x)

n_full=1000
k = round(1+np.log2(n_full))

x_boot = get_bootstrap(x, n_full)
print(x_boot.shape)


'''assimetration'''

alpha_1 = np.mean(x_boot, axis = 0)
alpha_2 = np.mean(x_boot**2, axis = 0)
mu_2 = alpha_2 - alpha_1**2
mu_3 = np.apply_along_axis(mu_3_i, 0, x_boot)
x_boot_assim = mu_3 / (mu_2 ** (3/2))
l = np.max(x_boot_assim) - np.min(x_boot_assim)
delta = l/k
print('l, k, delta = ', l, k, delta)
plt.hist(x_boot_assim, bins = k, density=True, color='y')
plt.title('Bootstrap для коэффициента асимметрии')
plt.xlabel('x', loc='right')
plt.ylabel('~_P(x)', loc='top')
plt.yticks(np.arange(0, 1.05, 0.05))
plt.ylim(0, 1.05)
plt.grid()
plt.show()