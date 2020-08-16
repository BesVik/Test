# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения



# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()
import simple_draw as sd
import time

sd.resolution = (1200, 800)

start_point = sd.get_point(600, 1)


def draw_branch(root_point, angle, length):
    if length < 10:
        return
    b1 = sd.get_vector(start_point=root_point, angle=angle, length=length)
    b1.draw()
    b2 = sd.get_vector(start_point=root_point, angle=angle + 60, length=length)
    b2.draw()
    #time.sleep(0.01)
    next_point = b1.end_point
    next_angle = angle - 30
    next_length = length * .75
    next_point2 = b2.end_point
    next_angle2 = angle + 30
    next_length2 = length * .75
    draw_branch(root_point=next_point, angle=next_angle, length=next_length)
    draw_branch(root_point=next_point2, angle=next_angle2, length=next_length2)

draw_branch(root_point=start_point, angle=60, length=100)

sd.pause()

# def x(n):
#     if n == 1:
#         return 1
#     xb = x(n=n - 1)
#     return n * xb
#
# print(x(9))

sd.pause()


