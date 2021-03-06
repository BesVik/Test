# -*- coding: utf-8 -*-
# Есть словарь координат городов
from pprint import pprint
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

moscow = {
     'Moscow_London': (((510 - 550) ** 2 + (510 - 370) ** 2)**0.5),
     'Moscow_Paris': (((550 - 480) ** 2 + (370 - 480) ** 2)**0.5)
  },

london = {
     'London_Paris': (((510 - 480) ** 2 + (510 - 480) ** 2)**0.5),
     'London_Moscow': (((510 - 550) ** 2 + (510 - 370) ** 2)**0.5)
  },

paris = {
     'Paris_London': (((510 - 480) ** 2 + (510 - 480) ** 2)**0.5),
     'Paris_Moscow': (((550 - 480) ** 2 + (370 - 480) ** 2)**0.5)
  }

distances = {
   'Moscow':
   {
     'Moscow_London': (((510 - 550) ** 2 + (510 - 370) ** 2)**0.5),
     'Moscow_Paris': (((550 - 480) ** 2 + (370 - 480) ** 2)**0.5)
   },
   'London':
   {
     'London_Paris': (((510 - 480) ** 2 + (510 - 480) ** 2)**0.5),
     'London_Moscow': (((510 - 550) ** 2 + (510 - 370) ** 2)**0.5)
   },
   'Paris':
   {
     'Paris_London': (((510 - 480) ** 2 + (510 - 480) ** 2)**0.5),
     'Paris_Moscow': (((550 - 480) ** 2 + (370 - 480) ** 2)**0.5)
   }
}

pprint(distances)





