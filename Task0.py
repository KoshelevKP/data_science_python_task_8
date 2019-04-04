import seaborn as sns
import numpy as np
import scipy.stats as sts

y = np.array([2, 8, 0, 4, 1, 9, 9, 0])

print('среднее: ', np.mean(y)) #Среднее значение велечины
print('медиана: ', np.median(y)) #Такое число что половина эдементов выборки больше него, а вторая половина меньше
print('мода: ', sts.mode(y)) #Значение которое встречается наиболее часто
print('квантили: ', np.quantile(y,0.25)) #Значения отделяющие 25% значений от верхней и нижней границы выборки
print('дисперсия: ', np.var(y)) #Разброс случайной велечины
print('стандартное отлонение: ', np.std(y)) #Рассеивание случайной велечины относительно математического ожидания
print('минимум: ', np.min(y)) #Минимальное значение в выборке
print('максимум: ', np.max(y)) #Максимальное значение в выборке
print('эксцесс:', sts.skew(y)) #Мера остроты пика
print('асиметрия:', sts.kurtosis(y)) #Отклонение от семетричности
sns.countplot(y, color='red')

y2 = 10-2*y
print(y2)

print('среднее: ', np.mean(y2)) 
print('медиана: ', np.median(y2)) 
print('мода: ', sts.mode(y2)) 
print('квантили: ', np.quantile(y2,0.25)) 
print('дисперсия: ', np.var(y2)) 
print('стандартное отлонение: ', np.std(y2)) 
print('минимум: ', np.min(y2)) 
print('максимум: ', np.max(y2)) 
print('эксцесс:', sts.skew(y2)) 
print('асиметрия:', sts.kurtosis(y2)) 

