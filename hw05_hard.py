# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 08:34:02 2018

@author: gaikaal1
"""
__author__ = 'Александр Гайкалов'

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.
 # Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.
 # P.S. По возможности, сделайте кросс-платформенную реализацию.
 # Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

import os
import sys

import shutil

print('sys.argv = ', sys.argv)

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")    
    print("ping - тестовый ключ")
    
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")

def make_dir():
     if not dir_name:
         print("Необходимо указать имя директории вторым параметром")
         return
     dir_path = os.path.join(os.getcwd(), dir_name)
     try:
         os.mkdir(dir_path)
         print('директория {} создана'.format(dir_name))
     except FileExistsError:
         print('директория {} уже существует'.format(dir_name))
 
def ping():
    print("pong")

def copy_file():
    if not dir_name:
        print("Необходимо указать имя копируемого файла вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        shutil.copyfile(dir_path, f"{dir_path}.copy")
        print(f"{dir_path} copied")
    except FileNotFoundError:
        print(f'файл {dir_path} не найден')

def remove_file():
    if not dir_name:
        print("Необходимо указать имя удаляемого файла вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.remove(dir_path)
        print(f"{dir_path} removes")
    except FileNotFoundError:
        print(f'файл {dir_path} не найден')

def chdir():   # не проверялось под linux
  
    _full = (os.name == "posix") and dir_name.startswith("/") or\
            (os.name == "nt") and dir_name[0].lower() in \
            list(map(chr, range(ord('a'), ord('z') + 1)))
    if _full:
        try:
            os.chdir(dir_name)
        except OSError:
            print(f'{dir_name} not found')
    else:
        try:
            os.chdir(os.path.join(os.getcwd(), dir_name))
        except OSError:
            print(f'{dir_name} not found')
    print(os.getcwd())

def full_dirname():
    print(os.getcwd())

# справочник действий по ключам пользовтеля
    
do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": chdir,
    "ls": full_dirname
}

try:
     dir_name = sys.argv[2]
except IndexError:
     dir_name = None
 
try:
     key = sys.argv[1]
except IndexError:
     key = None
 
 
if key:
     if do.get(key):
         do[key]()
     else:
         print("Задан неверный ключ")
         print("Укажите ключ help для получения справки")
