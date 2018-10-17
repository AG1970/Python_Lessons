__author__ = 'Александр Гайкалов'

import os
import sys
import shutil

"""
Функции для задания Normal
"""

def full_path(dir_name):
    """
    Служебная функция: возвращает полный путь к указанной папке
    """
    return (os.path.join(os.getcwd(),dir_name))

def go_to_dir(dir_name):
    """
    Переход к указанной папке
    """
    try:
        os.chdir(full_path(dir_name))
        print("Успешно перешел в ", dir_name)
    except FileNotFoundError:
        print("Невозможно перейти в ", dir_name)            

def lst_current_dir(path):
    """
    Вызывает список директорий и файлов в указанной папке
    """     
    for dirname, dirnames, filenames in os.walk(path):
       # сначала выводятся все поддиреrтории
        for subdirname in dirnames:
            print("\nПоддиректории:\n",os.path.join(dirname, subdirname))
        # затем все файлы
        for filename in filenames:
            print("\nФайлы:\n",os.path.join(dirname, filename))
            

def del_dir(dir_name):
    """
    Удаляет указанную папку
    """ 
    try:
        os.rmdir(full_path(dir_name))
    except FileNotFoundError:
        print("Невозможно удалить, папки {} в директории нет".format(dir_name))
    else:
        print("Успешно удалена папка ", dir_name)

def new_dir(dir_name):
    """
    Создает указанную папку
    """ 
    try:
        os.mkdir(full_path(dir_name))        
    except FileExistsError:
        print("Невозможно создать, папка {} уже существует".format(dir_name))
    else:
        print("Успешно cоздана папка", dir_name)


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

print("\nЗадача-1.1 Создание директорий\n")
print("В папке ", os.path.dirname(__file__))

"""
Ввел параметр количества папок, чтобы показать срабатываение try-except
"""

d = int(input("Введите количество создаваемых папок: "))+1 #Кл-во новых папок

# Создаем новые папки в цикле
for i in range(1,d):
    dir_n = "dir_"+ str(i)
    new_dir(dir_n)
   

print("-"*20) # Служебная строка для разделения задач

print("\nЗадача-1.2 Удаление директорий")

"""
Ввел подтверждение на удаление, чтобы при отмене удаления можно было проверить
создание папок, а также увидеть их список в задаче 2.
"""
n = input("Нажмите Y чтобы удалить созданные директории dir_1 - dir_9:")

if n.lower() == "y":
    # Удаляем директории в цикле
    for i in range(1,10):
        dir_n = "dir_"+ str(i)
        del_dir(dir_n)         
else:
    print("Удаление папок отменено")
    
print("-"*20) # Служебная строка для разделения задач

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print("\nЗадача-2 Список папок\n")
"""
Не использовал функцию, поскольку требуются только папки
"""
path = os.path.dirname(__file__)
print("Дериктория {} содержит папки: ".format(path))

"""
Если отменить удаление в предыдущей задаче, то тут можно увидеть список 
созданных в 1-й задаче директорий
"""

for dirname, dirnames, filenames in os.walk(path):
    for subdirname in dirnames:
        #print(os.path.join(dirname, subdirname)) Выводит папку и путь к ней
 # Выводит только название папки:
        d = list(os.path.split(subdirname))
        print ("\t- ",d[-1])
       
print("-"*20) # Служебная строка для разделения задач

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

print("\nЗадача-3 Копия исполняемого файла\n")
current_file = sys.argv[0]
print ("Скрипт выполняется в файле:\n", current_file)
backup_file = current_file + ".backup" #Название резевной копии исполняемого файла
shutil.copyfile(current_file, backup_file)
print ("\nРезервная копия исполняемого файла:\n", backup_file)






