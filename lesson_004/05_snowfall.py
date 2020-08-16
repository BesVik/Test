# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (600, 600)

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

y = 550
points = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
while True:

    point = sd.get_point(points[sd.random_number(0, 9)], y)
    for _ in range(2):
        sd.snowflake(center=point, length=sd.random_number(10, 100))
    y -= 10
    if y <= 50:
        break
    sd.sleep(0.1)

    if sd.user_want_exit():
        break
sd.finish_drawing()
sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
