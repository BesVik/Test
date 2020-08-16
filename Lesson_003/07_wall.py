# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
step = 0
for y in range(0, 1200, 50):
    y1 = y + 50
    step -= 50
    for x in range(step, 600, 100):
        x1 = x + 100
        point = simple_draw.get_point(x, y)
        point1 = simple_draw.get_point(x1, y1)
        simple_draw.rectangle(point, point1, color=simple_draw.COLOR_YELLOW, width=2)

simple_draw.pause()
