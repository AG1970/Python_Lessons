# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:54:08 2018

@author: gaikaal1
"""

__author__ = "Александр Гайкалов"

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.
 
# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
 
class Person:
    def __init__(self, name, surname, patronymic, birth_date):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.birth_date = birth_date
   
    def get_full_name(self):
        return self.surname + " " + self.name + " " + self.patronymic
   
    def get_surname_initials(self):
        return self.surname + " " + self.name[0] + "." + self.patronymic[0] + "."
   
    def set_name(self, new_name):
        self.name = new_name
        
class Pedagogue(Person):
    def __init__(self, name, surname, patronymic, birth_date, school, teach_subject):
        Person.__init__(self, name, surname, patronymic, birth_date)
        self.school = school
        self.teach_subject = teach_subject
        
class Band:
    def __init__(self, Band, Pedagogues):
        self._Band = {"Band_num": int(Band.split()[0]), "Band_let": Band.split()[1]}
        self.Pedagogues_dict = {t.teach_subject: t for t in Pedagogues}
        
    @property
    def Band(self):
        return "{} {}".format(self._Band["Band_num"], self._Band["Band_let"])
    
class pupil(Person):
    def __init__(self, name, surname, patronymic, birth_date, school, Band, parents):
        Person.__init__(self, name, surname, patronymic, birth_date)
        self.school = school
        self.Band = Band
        self.parents = parents
        
    def next_class(self):
        self._Band["Band_num"] += 1
        
Pedagogues = [Pedagogue("Сюзанна", "Черторыльская", "Геннадьвна", "11.11.1980", "школа 732", "математика"),
            Pedagogue("Надежда", "Суровая", "Анатольевна", "10.12.1981", "школа 732", "русский язык"),
            Pedagogue("Екатерина", "Фёдорова", "Ивановна", "01.10.1969", "школа 732", "литература"),
            Pedagogue("Елизавета", "Романова", "Алексеевна", "14.02.1981", "школа 732", "математика"),
            Pedagogue("Виктор", "Черномырдин", "Степанович", "09.04.1938", "школа 635", "изящная словестность"),
            Pedagogue("Пётр", "Николаев", "Анатльевич", "18.02.2001", "школа 635", "математика"),
            Pedagogue("Полиграф", "Шариков", "Полиграфович", "19.11.1924", "школа 635", "ОБЖ"),
            Pedagogue("Арина", "Голубка", "Родионовна", "11.10.1982", "школа 635", "литература")]

Bands = [Band("7 А", [Pedagogues[0], Pedagogues[1], Pedagogues[2]]),
         Band("8 А", [Pedagogues[3], Pedagogues[1], Pedagogues[2]]),
         Band("8 Б", [Pedagogues[5], Pedagogues[4], Pedagogues[2]]),
         Band("9 А", [Pedagogues[2], Pedagogues[6], Pedagogues[4]]),
         Band("9 Б", [Pedagogues[5], Pedagogues[6], Pedagogues[7]])]

parents = [Person("Алексей", "Романов", "Михайлович", "12.11.1979"),
           Person("Прасковья", "Романова", "Фёдоровна", "12.10.1984"),
           Person("Пётр", "Николаев", "Анатольевич", "18.02.1971"),
           Person("Прасковья", "Романова", "Фёдоровна", "12.10.1984"),
           Person("Самсон", "Могарыч", "Анатольевич", "14.07.1981"),
           Person("Надежда", "Могарыч", "Андреева", "11.10.1982")]


pupils = [pupil("Пётр", "Романов", "Алексеевич", "10.11.2008", "школа 732", Bands[0], [parents[0], parents[1]]),
          pupil("Анна", "Романова", "Иоановна", "10.01.1996", "школа 732", Bands[0], [parents[0], parents[1]]),
          pupil("Алоизий", "Могарыч", "Александрович", "04.11.2003", "школа 635", Bands[2], [parents[4], parents[5]]),
          pupil("Анна", "Романова", "Иоановна", "12.11.1999", "школа 732", Bands[1], [parents[2]]),
          pupil("Ян", "Петров", "Александрович", "10.11.1999", "школа 732", Bands[1], [parents[0], parents[1]]),
          pupil("Сергей", "Сергеев", "Иванович", "11.11.1999", "школа 635", Bands[2], []),
          pupil("Инна", "Александрова", "Павловна", "03.11.1999", "школа 635", Bands[3], [parents[0], parents[1]]),
          pupil("Пульхерия", "Яковлева", "Алексеевна", "11.11.1999", "школа 635", Bands[3], [])]

# 1. Получить полный список всех классов школы
print("1. Полный список всех классов школы")
for cl in Bands:
    print(cl.Band)
print("-"*20)

# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
def get_list_pupils(Band):
    return [st.get_surname_initials() for st in pupils if st.Band == Band]
print("2. Список всех учеников в", Bands[0].Band)
print(get_list_pupils(Bands[0]))
print("-"*20)

# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
print("3. Список всех предметов ученика", pupils[0].get_surname_initials())
for subject in pupils[0].Band.Pedagogues_dict.keys():
    #Ученик --> Класс --> Учителя --> Предметы
    print(subject)    
#print(pupils[0].Band.Pedagogues_dict.keys())
print("-"*20)

# 4. Узнать ФИО родителей указанного ученика
print("4. ФИО родителей ученика", pupils[0].get_surname_initials())
for parent in pupils[0].parents:
    print(parent.get_full_name())
print("-"*20)

# 5. Получить список всех Учителей, преподающих в указанном классе
print("5. Список учителей в классе", Bands[0].Band)
for Pedagogue in Bands[0].Pedagogues_dict.values():
    print(Pedagogue.get_full_name())
