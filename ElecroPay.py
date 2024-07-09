from time import sleep

price_Kw = 5.10

while True:
    middlePower = int(input("\nСредняя мощность: 0-для выхода\n"))
    if middlePower == 0:
        print("Завершение программы через:")
        print("3")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        sleep(1)
        print("0")
        break
    print("Сумма",price_Kw * middlePower /1000 *31*24,"руб")