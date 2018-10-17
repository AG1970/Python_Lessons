# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:05:27 2018

@author: gaikaal1
"""

__author__ = 'Александр Гайкалов'

# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os

class Worker:
   def __init__(self, line):
      self.name = line.split()[0]
      self.surname = line.split()[1]
      self.salary = int(line.split()[2])
      self.job = line.split()[3]
      self.basic_hours = int(line.split()[4])
      self.full_name = f"{self.name} {self.surname}"

   def payroll(self, hours):
      overtime = hours - self.basic_hours
      return int(self.salary * (1 + 2 * overtime / self.basic_hours)
                 if overtime > 0 else self.salary * (1 + overtime / self.basic_hours))
workers = []

#Загрузка списка работников с окладами
path = os.path.join('data', 'workers')

with open(path, "r", encoding='UTF-8') as f:
   f.readline()  # Удаление заголовка таблицы
   for line in f.readlines():
        workers.append(Worker(line))

#Загрузка времязатрат
path = os.path.join('data', 'hours_of')

with open(path, "r", encoding='UTF-8') as f:
   f.readline() # Удаление заголовка таблицы
   hours_of = f.readlines()
   hours_of_worker = {}

for hours in hours_of:
   hours_data = hours.split()
   worker = f"{hours_data[0]} {hours_data[1]}"  # Работник (Имя Фамилия)
   hours_of_worker[worker] = hours_data[2]

payroll_dict = {}  # Словарь для хранения зарплат с учётом переработок
for worker in workers:
    payroll_dict[worker.full_name] = worker.payroll(int(hours_of_worker[worker.full_name]))

# Печать зарплат с учётом переработок
align = max(map(len, payroll_dict.keys()))
print(f"Работник         Зарплата")
for k, v in payroll_dict.items():
    print(f"{k} {v:>{align - len(k) + 6}}")
