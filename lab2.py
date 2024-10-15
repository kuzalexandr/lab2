from abc import ABC, abstractmethod
import math

# Абстрактный класс Геометрическая фигура
class GeometricFigure(ABC):
  @abstractmethod
  def get_area(self):
    """Абстрактный метод для вычисления площади фигуры"""
    pass

  @classmethod
  @abstractmethod
  def get_figure_name(cls):
    """Абстрактный метод для возврата названия фигуры"""
    pass

# Класс Цвет фигуры
class FigureColor:
  def __init__(self, color): 
    self.color = color

# Класс Прямоугольник», наследуемый от Геометрическая фигура
class Rectangle(GeometricFigure):
  figure_name = "Прямоугольник"

  def __init__(self, width, height, color):
    self.width = width
    self.height = height
    self.color = FigureColor(color)

  def get_area(self):
    return self.width * self.height

  @classmethod
  def get_figure_name(cls):
    return cls.figure_name

  def __repr__(self): 
    return (f"Фигура: {self.get_figure_name()}, Ширина: {self.width}, "
        f"Высота: {self.height}, Цвет: {self.color.color}, "
        f"Площадь: {self.get_area():.2f}")

# Класс Круг, наследуемый от Геометрическая фигура
class Circle(GeometricFigure):
  figure_name = "Круг"

  def __init__(self, radius, color): 
    self.radius = radius
    self.color = FigureColor(color)

  def get_area(self):
    return math.pi * self.radius ** 2

  @classmethod
  def get_figure_name(cls):
    return cls.figure_name

  def __repr__(self):
    return (f"Фигура: {self.get_figure_name()}, Радиус: {self.radius}, "
        f"Цвет: {self.color.color}, Площадь: {self.get_area():.2f}")

# Класс Квадрат, наследуемый от Прямоугольник
class Square(Rectangle):
  figure_name = "Квадрат"

  def __init__(self, side_length, color): 
    super().__init__(side_length, side_length, color) # Исправлено: super().__init__

  @classmethod
  def get_figure_name(cls):
    return cls.figure_name

  def __repr__(self): 
    return (f"Фигура: {self.get_figure_name()}, Длина стороны: {self.width}, "
        f"Цвет: {self.color.color}, Площадь: {self.get_area():.2f}")

# Пример использования классов:
rect = Rectangle(3, 4, "синий")
circle = Circle(5, "красный")
square = Square(2, "зеленый")

# Вывод
print(rect)  # Фигура: Прямоугольник, Ширина: 3, Высота: 4, Цвет: синий, Площадь: 12.00
print(circle) # Фигура: Круг, Радиус: 5, Цвет: красный, Площадь: 78.54
print(square) # Фигура: Квадрат, Длина стороны: 2, Цвет: зеленый, Площадь: 4.00

