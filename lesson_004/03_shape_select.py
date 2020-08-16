# -*- coding: utf-8 -*-

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


import simple_draw as sd

sd.resolution = (800, 900)

print('Список доступных фигур')
figure_dict = {
    1: 'треугольник',
    2: 'квадрат',
    3: 'пятиугольник',
    4: 'шестиугольник'
}

for code_figure in figure_dict:
    print(code_figure, ':', figure_dict[code_figure])

user_input = input("Введите, номер желаемой фигуры: ")
code_figure = int(user_input)
if code_figure < 1 or code_figure > 4:
    print('Вы ввели некоректный номер')
print('Вы ввели', code_figure, ' : ', figure_dict[code_figure])

point_0 = sd.get_point(220, 350)
point_1 = sd.get_point(220, 350)
point_2 = sd.get_point(220, 350)
point_3 = sd.get_point(220, 350)


def drawing_figure(point, angle, length, step):
    v = sd.get_vector(start_point=point, angle=angle, length=length, width=4)
    for angle in range(0, 360, step):
        v = sd.get_vector(start_point=v.end_point, angle=angle, length=length, width=4)
        v.draw()


def triangle(point, angle, length, side):
    step = 360 // side
    drawing_figure(point, angle, length, step)


def square(point, angle, length, side):
    step = 360 // side
    drawing_figure(point, angle, length, step)


def pentagon(point, angle, length, side):
    step = 360 // side
    drawing_figure(point, angle, length, step)


def hexagon(point, angle, length, side):
    step = 360 // side
    drawing_figure(point, angle, length, step)


drawing_figure_dict = {
    1: lambda: triangle(point=point_0, angle=0, length=120, side=3),
    2: lambda: square(point=point_1, angle=0, length=120, side=4),
    3: lambda: pentagon(point=point_2, angle=0, length=120, side=5),
    4: lambda: hexagon(point=point_3, angle=0, length=120, side=6)
}

for drawing_code_figure in drawing_figure_dict:
    print(drawing_code_figure, ':', drawing_figure_dict[drawing_code_figure])
drawing_code_figure = int(user_input)
print('Вы ввели', drawing_code_figure, ' : ', drawing_figure_dict[drawing_code_figure])

drawing_figure_dict[drawing_code_figure]()

sd.pause()
