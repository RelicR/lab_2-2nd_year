'''знакопеременный ряд abs(x**n)/fact(n)'''
import random
from functools import lru_cache


@lru_cache()
def fact(a): #Функция вычисления факториала
    if a == 1:
        return 1
    elif a > 1:
        return fact(a-1)
    else:
        return 0


#k, t = map(int, input("Введите значения k-ранга матрицы и t-точности вычислений:\n").split())
k, t = random.randint(2, 10), random.randint(1, 5) #Задание рандомных значений ранга матрицы k и точности вычислений t
print(f"Ранг матрицы k = {k}, Точность вычислений t знаков = {t}\n")
t = 10**(-t)

#X = [[random.uniform(-10, 10) for i in range(k)] for j in range(k)]
X = [[0.0]*k for i in range(k)] #Задание матрицы значений для вычислений
print("Матрица X значений:")
for i in range(k*k): #Задание рандомных значений для элементов матрицы
    X[i // k][i % k] = random.uniform(-1, 1)
    print('%10f' %X[i // k][i % k], end='  ')
    if i % k == (k-1):
        print()
print()

res, prev = 0, 1
for i in range(k*k): #Цикл для вычисления суммы знакопеременного ряда
    res += (-1)**(i+1) * abs(X[i // k][i % k]) / fact(i+1)
    if abs(abs(res)-abs(prev)) < t:
        print(f"Цикл №{i}, Предыдущее значение: {prev}, Текущее значение: {res}, выход по условию t")
        break
    #print(abs(res-prev))
    print(f"Цикл №{i}, Предыдущее значение: {prev}, Текущее значение: {res}")
    prev = res
print('\nРезультат вычислений:', res, ', Точность вычислений {:0.9f}'.format(t))
