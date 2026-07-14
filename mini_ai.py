import os
import sys
import datetime
import random

print("--- GLEB AI v1.0 LOADED ---")

while True:
    # Приводим ввод к нижнему регистру и убираем лишние пробелы
    ai_say = input("hello>>> ").strip().lower()
    
    if ai_say == "exit":
        print("AI is sleeping...")
        break
        
    elif ai_say == "hello" or ai_say == "hi":
        print("How are you? (good/bad)")
        # Здесь можно было бы добавить второй input, но пока оставим просто ответ
        
    elif ai_say == "good":
        print("Great! Let's code something!")
        
    elif ai_say == "bad":
        print("Oh no... Maybe play a game?")
        
    elif ai_say == "stupid ai":
        print(":(")
        print("I'm trying my best...")
        
    elif ai_say == "give me small code":
        print('Here it is: print("Hello World")')
        
    elif ai_say == "time":
        print(datetime.datetime.now())
        
    elif ai_say == "who are you":
        print("I am Gleb's personal AI assistant.")
        
    elif ai_say == "gleb":
        print("Gleb is the creator! He is 10 years old and very smart.")
        
    else:
        # ИИ отвечает случайной фразой, если не понял
        answers = [
            "I don't understand.",
            "Can you repeat?",
            "That's interesting...",
            "Error 404: Logic not found."
        ]
        print(random.choice(answers))