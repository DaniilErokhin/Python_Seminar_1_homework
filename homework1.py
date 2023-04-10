#Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
number = int(input('Введите число:'))
if number == 1:
    print(f'Понедельник')
if number == 2:
    print(f'Вторник')
if number == 3:
    print(f'Среда')
if number == 4:
    print(f'Четверг')
if number == 5:
    print(f'Пятница')
if number == 6:
    print(f'Суббота')
if number == 7:
    print(f'Воскресенье')
else:
    print(f'Нет такого дня')

#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
def inputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Нужно вводить целые числа")
    return a

def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment

print("Введите координаты точки А")
pointA = inputNumbers(2)
print("Введите координаты точки В")
pointB = inputNumbers(2)

print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}")

#Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
def Quater():
    number = int(input('Введите номер четверти: '))
    if(number == 1):
        print(f"x > 0 and y > 0")
    if(number == 2):
        print(f"x < 0 and y > 0")
    if(number == 3):
        print(f"x < 0 and y < 0")
    if(number == 4):
        print(f"x > 0 and y < 0")
Quater()

#Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.

N = int(input("Введите число:"))
i = 0
while i < N:
    print(f'{i}\t', end ='')
    i += 2