import random


class Point():

  def __init__(self):
    print("Создание точки.")
    print("Введите координату 1 точки")
    self.x = random.randint(0, 100) / 10  #int(input())
    print("Введите координату 2 точки")
    self.y = random.randint(0, 100) / 10  #int(input())
    print("Создание точки произошло успешно")

  def show(self):
    print("Point (%.1f,%.1f)" % (self.x, self.y))

  def __repr__(self):
    #return str('Point')
    return str('Point (%.1f,%.1f)' % (self.x, self.y))

  def move(self, x, y):
    self.x = x
    self.y = y

# @property
# def x(self):
#   return self.__x

#@x.setter
#def x(self, x):
#  self.x = x

  def dist(self, point2):
    d = ((self.x - point2.x)**2 + (self.y - point2.y)**2)**0.5
    #d = ((self.x - point2.x())**2+(self.__y-point2.y())**2)**0.5
    return d


class Figure():

  def __init__(self):
    print("Создание figure.")

  def show(self):
    print("I am figure!")

  def perimeter(self):
    print("вычисление периметра.")

  def __repr__(self):
    return str('Figure')


class Triangle(Figure):

  def __init__(self):
    super().__init__()
    print("Создание треугольника.")
    self.__a = Point()
    self.__b = Point()
    self.__c = Point()
    print("Создание треугольника произошло успешно")

  def show(self):
    super().show()
    print("triangle")
    self.__a.show()
    self.__b.show()
    self.__c.show()

  def __repr__(self):
    s = str('Triangle: ') + str(self.__a) + "; " + str(self.__b) + "; " + str(
        self.__c) + "." + " Perimeter: " + str(self.perimeter())
    return s

  def perimeter(self):
    print("...вычисление периметра треугольника.")
    return (self.__a.dist(self.__b))


class Rectangle(Figure):

  def __init__(self):
    super().__init__()
    print("Создание прямоугольника.")
    self.__a = Point()
    self.__b = Point()
    self.__c = Point()
    self.__d = Point()
    print("Создание прямоугольника произошло успешно")

  def show(self):
    super().show()
    print("Rectangle")
    self.__a.show()
    self.__b.show()
    self.__c.show()
    self.__d.show()

  def __repr__(self):
    s = str('Rectangle: ') + str(self.__a) + "; " + str(self.__b) + "; " + str(
        self.__c) + "; " + str(self.__d) + "." + " Perimeter: " + str(
            self.perimeter())
    return s

  def perimeter(self):
    print("...вычисление периметра прямоугольника.")
    return (self.__a.dist(self.__b)) * 2
    # не работает
    #return (self.__a.dist(self.__b)+self.__b.dist(self.__c)+self.__c.dist(self.__d)+self.__d.dist(self.__a))


f = Figure()
f.show()
f.perimeter()
tr = Triangle()
tr.show()
print(tr.perimeter())

list_of_objects = []
for i in range(3):
  f = Triangle()
  list_of_objects.append(f)
for i in range(3):
  f = Rectangle()
  list_of_objects.append(f)

print("list_of_objects before sort:")
print(list_of_objects)
print("list_of_objects after sort:")
sorted(list_of_objects, key=lambda figure: figure.perimeter())
print(list_of_objects)
