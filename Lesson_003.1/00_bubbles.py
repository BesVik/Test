# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

#point = sd.get_point(200, 200)
#radius = 50
#for _ in range(3):
#    radius = radius + 5
#    sd.circle(center_position=point, radius=radius)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

#def bubble(point, step):
#    radius = 50
#    for _ in range(3):
#        radius += step
#        sd.circle(point, radius=radius, color=sd.COLOR_RED)

#point = sd.get_point(300, 200)
#bubble(point=point, step=5)

# Нарисовать 10 пузырьков в ряд
#def bubble(point, step):
#    radius = 50
#    for _ in range(1):
#        radius += step
#        sd.circle(point, radius=radius, color=sd.COLOR_RED, width=2)

#for x in range(100, 1100, 100):
#   point = sd.get_point(x, 200)
#   bubble(point=point, step=5)

# Нарисовать три ряда по 10 пузырьков
#def bubble(point, step):
#    radius = 50
#    for _ in range(1):
#        radius += step
#        sd.circle(point, radius=radius, color=sd.COLOR_RED, width=3)

#for y in range(100, 301, 100):
#    for x in range(100, 1001, 100):
#        point = sd.get_point(x, y)
#        bubble(point=point, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
#def bubble(point, step):
#    radius = 50
#    for _ in range(1):
#        radius += step
#        sd.circle(point, radius=radius, color=sd.COLOR_RED, width=4)

#for _ in range(100):
#    point = sd.random_point()
#    bubble(point=point, step=5)

sd.pause()