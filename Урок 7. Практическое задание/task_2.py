"""
Задание 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.

Единственный класс этого проекта — одежда (класс Clothes).

К типам одежды в этом проекте относятся пальто и костюм.

У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property

Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57

Два класса: абстрактный и Clothes
"""

+
+ from abc import ABC, abstractmethod
+
+
+ class AbstractClass(ABC):
+  @abstractmethod
+   def coat(self):
+       pass
+
+   @abstractmethod
+   def suit(self):
+       pass
+
+
+ class Clothes(AbstractClass):
+
+   def __init__(self, v, h):
+       self.v = v
+       self.h = h
+
+   def coat(self):
+       result = round(self.v / 6.5 + 0.5, 2)
+       return f'Расход ткани на пальто = {result}'
+
+   def suit(self):
+       result = round(2 * self.h + 0.3, 2)
+       return f'Расход ткани на костюм = {result}'
+
+   @property
+   def total_consumption(self):
+       return f'Общий расход ткани = {self.v / 6.5 + 0.5 + 2 * self.h + 0.3 :.2f}'
+
+
+ a = Clothes(7, 10)
+ print(a.coat())
+ print(a.suit())
+ print(a.total_consumption)
+
+
+
+
