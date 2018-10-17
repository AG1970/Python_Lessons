# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 19:09:01 2018

@author: gaikaal1
"""
__author__ = 'Александр Гайкалов'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
class Point:
    """
    p(x, y)
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Segment:
    """
    p1(x1, y1)
    p2(x2, y2)
    y = k1*x + k2
    """
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
    
    @property
    def length(self):
        return ((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2) ** 0.5
    
    @property
    def k1(self):
        return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x) if self.p2.x - self.p1.x != 0 else float("inf")

class Trigon:
    """
    Вершины:
        p1(x1, y1)     
        p2(x2, y2)      
        p3(x3, y3)      
    Стороны:
        a(p1, p2): y = k1.a*x + k2.a
        b(p2, p3): y = k1.b*x + k2.b
        c(p3, p1): y = k1.c*x + k2.c
  
    """
    def __init__(self, *args):
        self.p1 = args[0]
        self.p2 = args[1]
        self.p3 = args[2]
        self.a = Segment(self.p1, self.p2)
        self.b = Segment(self.p2, self.p3)
        self.c = Segment(self.p3, self.p1)
        
    def perimetre(self):
        return self.a.length + self.b.length + self.c.length
    
    def area(self):
        # по формуле Герона, через полупериметр hp
        hp = self.perimetre() / 2
        return (hp * (hp - self.a.length) * (hp - self.b.length) * (hp - self.c.length))**0.5
    
    def height(self):
        # допустим, высота, опущенная на основание a
        return 2 * self.area() / self.a.length
    
Trigon = Trigon(Point(0, 0), Point(5, 0), Point(3, 4))
print(f"Площадь треугольника = {Trigon.area():.2f}")
print(f"Периметр треугольника = {Trigon.perimetre():.2f}")
print(f"Высота треугольника = {Trigon.height():.2f}")
print("-"*10)

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class Trapezium:
    """
    Вершины
        p1(x1, y1)      
        p2(x2, y2)    
        p3(x3, y3)      
        p4(x4, y4) 
    Стороны:
        a  ->  y = a.k1*x + a.k2
        b  ->  y = b.k1*x + b.k2
        c  ->  y = c.k1*x + c.k2
        d  ->  y = d.k1*x + d.k2
    """
    def __init__(self, *args):
        self.p1 = args[0]
        self.p2 = args[1]
        self.p3 = args[2]
        self.p4 = args[3]
        self.a = Segment(self.p1, self.p2)
        self.b = Segment(self.p2, self.p3)
        self.c = Segment(self.p3, self.p4)
        self.d = Segment(self.p4, self.p1)
        
    def is_isosceles(self):
        # проверка на условие равнобедренности трапеции
        if self.a.k1 == self.c.k1 and self.b.length == self.d.length:
            return True
        elif self.b.k1 == self.d.k1 and self.a.length == self.c.length:
            return True
            return False
     
    def area(self):
        return (self.a.length + self.c.length) / 2 * (self.d.length**2 - (self.a.length - self.c.length)**2 / 4)**0.5
    
    def perimetre(self):
        return self.a.length + self.b.length + self.c.length + self.d.length
    
    def height(self):
        if self.a.k1 == self.c.k1:
            h = 2 * self.area() / (self.a.length + self.c.length)
        else:
            h = 2 * self.area() / (self.b.length + self.d.length)
        return h

Trapezium1 = Trapezium(Point(0, 0), Point(6, 0), Point(2, 4), Point(4, 4))
print(Trapezium1.is_isosceles())
print(f"Площадь трапеции = {Trapezium1.area():.2f}")
print(f"Периметр трапеции = {Trapezium1.perimetre():.2f}")
print(f"Высота трапеции = {Trapezium1.height():.2f}")
print("-"*10)

Trapezium2 = Trapezium(Point(0, 0), Point(-6, 0), Point(-2, -4), Point(-4, -4))
print(Trapezium2.is_isosceles())
print(f"Площадь трапеции = {Trapezium2.area():.2f}")
print(f"Периметр трапеции = {Trapezium2.perimetre():.2f}")
print(f"Высота трапеции = {Trapezium2.height():.2f}")
print("-"*10)

Trapezium3 = Trapezium(Point(0, 0), Point(5, 0), Point(2, 4), Point(4, 4))
print(Trapezium3.is_isosceles())

