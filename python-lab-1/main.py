# Приклад

from math import cos, exp, log10, acos, sin, sqrt, atan
#
# x = float(input("Ввeдіть зачення x:"))
#
# y = ((exp(-x) - 9.3) / (log10(x) - cos(x ** 2))) ** -0.3
# print("Результат обчислення:", y)



# 1 - 12 option

z = float(input("Ввeдіть зачення z:"))

g = acos(((z - log10(z)) / (1 + cos(3) * z)) + 1)

print("Результат обчислення:", g)



# 2 - 2 option

# t = float(input("Ввeдіть зачення t:"))
#
# w = ((sin(x ** 2) - cos((t - 1) ** 2) ** 4) / (atan(x + 2.6)) + sqrt(log10(t)) ** 3)
# print("Результат обчислення:", w)
