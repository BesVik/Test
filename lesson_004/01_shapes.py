# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 800)

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

def triangle(point=sd.get_point(300, 300), angle=0, length=200):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=240, length=length, width=3)
    v3.draw()


triangle(point=sd.get_point(300, 300), angle=0, length=200)

def qvadrat():
    point = sd.get_point(500, 500)
    sd.square(left_bottom=point, side=100, color=sd.COLOR_YELLOW, width=3)


qvadrat()

def pyatiugolnik(point_, angle_=0, length_=100, width_=3):
    v1_ = sd.get_vector(start_point=point_, angle=angle_, length=length_, width=width_)
    v1_.draw()

    v2_ = sd.get_vector(start_point=v1_.end_point, angle=angle_ + 72, length=length_, width=width_)
    v2_.draw()

    v3_ = sd.get_vector(start_point=v2_.end_point, angle=angle_ + 144, length=length_, width=width_)
    v3_.draw()

    v4_ = sd.get_vector(start_point=v3_.end_point, angle=angle_ + 216, length=length_, width=width_)
    v4_.draw()

    v5_ = sd.get_vector(start_point=v4_.end_point, angle=angle_ + 288, length=length_, width=width_)
    v5_.draw()


point = sd.get_point(100, 100)

pyatiugolnik(point, angle_=0, length_=100, width_=3)

def sixangle(point__, angle__=0, length__=100, width__=3):
    v1__ = sd.get_vector(start_point=point__, angle=angle__, length=length__, width=width__)
    v1__.draw()

    v2__ = sd.get_vector(start_point=v1__.end_point, angle=angle__ + 60, length=length__, width=width__)
    v2__.draw()

    v3__ = sd.get_vector(start_point=v2__.end_point, angle=angle__ + 120, length=length__, width=width__)
    v3__.draw()

    v4__ = sd.get_vector(start_point=v3__.end_point, angle=angle__ + 180, length=length__, width=width__)
    v4__.draw()

    v5__ = sd.get_vector(start_point=v4__.end_point, angle=angle__ + 240, length=length__, width=width__)
    v5__.draw()

    v6__ = sd.get_vector(start_point=v5__.end_point, angle=angle__ + 300, length=length__, width=width__)
    v6__.draw()
point = sd.get_point(800, 600)

sixangle(point, angle__=0, length__=100, width__=3)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
