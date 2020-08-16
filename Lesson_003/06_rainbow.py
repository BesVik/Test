# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(point, radius=radius, color=sd.COLOR_RED)

point = sd.get_point(300, 200)
bubble(point=point, step=5)
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.pause()
