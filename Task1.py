import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts


#Нормальное распределение

mu = 5
sigma = 2

norm_rv = sts.norm(loc=mu, scale=sigma)

x = np.linspace(0,10)
pdf = norm_rv.pdf(x)
plt.plot(x, pdf)

x = np.linspace(0,10)
cdf = norm_rv.cdf(x)
plt.plot(x, cdf)

plt.ylabel('$f(x),F(x)$')
plt.xlabel('$x$')

print('Вероятность что значение будет больше 7', 1-norm_rv.cdf(7))


#Распределение пуасона

mu=5
poisson_rv=sts.poisson(mu)

x = np.linspace(0,10,11)
cdf = poisson_rv.cdf(x)
plt.plot(x, cdf)

pmf = poisson_rv.pmf(x)
plt.plot(x, pmf)

print('Вероятность что значение будет больше 2 но меньше 10', poisson_rv.cdf(10)-poisson_rv.cdf(2))
