import math

b = int(input("За этот месяц кв/ч: "))
a = int(input("За прошлый месяц кв/ч: "))

print("\n",int(math.fabs(b-a)*4.69), "руб.\n")

input("Введите что-нибудь, чтобы продолжить")
