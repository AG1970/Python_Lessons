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


