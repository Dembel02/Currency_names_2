# 10. (МОДУЛЬ 4) В проекте создать новый модуль bornyearforewer.py
# 11. Написать или модернизировать программу (МОДУЛЬ 2) используя условные операторы и цикл while:
# Работа программы аналогично МОДУЛЬ 2, но спрашиваем пользователя до тех пор, пока он не введет верный год рождения.
# После ввода верного года рождения выводим в терминал 'Верно' и выходим из программы

year = None
while year != 1799:
    year = int(input("Введите год рождения А.С.Пушкина"))
print("Верно")