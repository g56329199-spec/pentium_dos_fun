# doom_text.py
import os
import random
import time

def start_doom():
    player_x, player_y = 1, 1
    monster_x, monster_y = 8, 8
    map_size = 10
    
    print("=== TEXT DOOM v0.1 ===")
    print("Управление: w (вверх), s (вниз), a (влево), d (вправо), q (выход)")
    
    while True:
        # Очистка экрана для эффекта анимации
        os.system('clear')
        
        # Отрисовка карты
        for y in range(map_size):
            row = ""
            for x in range(map_size):
                if x == player_x and y == player_y:
                    row += "@ " # Игрок
                elif x == monster_x and y == monster_y:
                    row += "M " # Монстр
                else:
                    row += ". " # Пол
            print(row)
            
        # Проверка столкновения
        if player_x == monster_x and player_y == monster_y:
            print("💀 GAME OVER! Монстр тебя поймал!")
            break
            
        # Ход монстра (простой ИИ)
        if random.randint(0, 1) == 0:
            monster_x += random.choice([-1, 1])
        else:
            monster_y += random.choice([-1, 1])
            
        # Управление
        move = input("Ход >> ").lower()
        if move == 'q': break
        if move == 'w' and player_y > 0: player_y -= 1
        if move == 's' and player_y < map_size - 1: player_y += 1
        if move == 'a' and player_x > 0: player_x -= 1
        if move == 'd' and player_x < map_size - 1: player_x += 1

if __name__ == "__main__":
    start_doom()