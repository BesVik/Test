# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
#sd.resolution = (1200, 600)

# def smile(x, y, x1, y1):
center_position1 = sd.get_point(350, 260)
sd.circle(center_position1, radius=15, color=sd.COLOR_RED, width=1)

center_position2 = sd.get_point(450, 260)
sd.circle(center_position2, radius=15, color=sd.COLOR_RED, width=1)

point1 = sd.get_point(300, 200)
point2 = sd.get_point(500, 300)
sd.ellipse(point1, point2, color=sd.COLOR_RED, width=2)

start_point = sd.get_point(350, 230)
end_point = sd.get_point(450, 230)
sd.line(start_point, end_point, color=sd.COLOR_RED, width=1)

sd.pause()

# def bubble1(point, step):
#    radius = 10
#    for _ in range(1):
#        radius += step
#        sd.circle(point, radius=radius, color=sd.COLOR_RED)


# point = sd.get_point(350, 260)
# bubble1(point=point, step=5)


# def bubble2(new_point, new_step):
#    new_radius = 10
#    for _ in range(1):
#        new_radius += new_step
#        sd.circle(new_point, radius=new_radius, color=sd.COLOR_RED)


# point = sd.get_point(450, 260)
# bubble2(new_point=point, new_step=5)
