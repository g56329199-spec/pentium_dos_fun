import os
import sys
import datetime
import time

print("Pentium_DOS Version 1.0 [Created by Gleb]")
time.sleep(3)
print(datetime.datetime.now())
print("RAM>>>16KB")
print("CPU>>>pentium 1 core 0.5 super max")
time.sleep(3)
os.system('clear')

while True:
    
    vvod = input("pentium_dos>>>")
    
    if vvod == "help":
        print("help - all commands view")
        print("gleb - creator info")
        print("shut_up_sys - system off")
        print("game - doom")
        print("cls - clear all")
        print("echo - your text in dos")
        print("mini_ai - ai 0.0.1")
        
    elif vvod == "gleb":
        print("10 years old")
        print("create this pentium_dos")
    
    elif vvod == "shut_up_sys":
        print(":( okay")
        break
    
    elif vvod == "game":
        print("Загрузка текстур Doom...")
        print("Инициализация звукового движка...")
        time.sleep(1) # Небольшая пауза для эффекта
        os.system('python3 doom_text.py') # Запускаем файл игры
        print("Возврат в Pentium_DOS...")
        
    elif vvod == "cls":
        os.system('clear')
        
    elif vvod.startswith("echo "):
        # echo выводит всё, что написано после пробела
        text = vvod[5:] 
        print(text)
        
    elif vvod == "mini_ai":
        os.system('python3 mini_ai.py')
    else:
        # Если команда не найдена
        print(f"Bad command or file name: '{vvod}'")