import os

run = True
menu = True
play = False
rules = False
key = False

HP = 20
HPMAX = HP
ATK = 3
pot = 1
elix = 0 
gold = 0
x = 0
y = 0


#Рисуем карту. Пока вручную.

#        x = 0        x = 1     x = 2       x = 3        x = 4       x = 5              x = 6
map = [["plains",   "plains",   "plains",   "plains",   "forest",   "mountain",         "cave"],  # y = 0
       ["forest",   "forest",   "forest",   "forest",   "forest",      "hills",     "mountain"],  # y = 1
       ["forest",   "fields",   "bridge",   "plains",    "hills",     "forest",        "hills"],  # y = 2
       ["plains",     "shop",     "town",    "major",   "plains",      "hills",     "mountain"],  # y = 3
       ["plains",   "fields",   "fields",   "plains",    "hills",   "mountain",     "mountain"]]  # y = 4

y_len = len(map) - 1
x_len = len(map[0]) - 1

#Задали описание биомов через вложенный словарь, где t: Имя биома в игре, а e: может ли там находиться противник

biom = {
    "plains": {
        "t": "PLAINS",
        "e": True},
    "forest": {
        "t": "WOODS",
        "e": True},
    "fields": {
        "t": "FIELDS",
        "e": False},
    "bridge": {
        "t": "BRIDGE",
        "e": True},
    "town": {
        "t": "TOWN CENTRE",
        "e": False},
    "shop": {
        "t": "SHOP",
        "e": False},
    "major": {
        "t": "MAJOR",
        "e": False},
    "cave": {
        "t": "CAVE",
        "e": False},
    "mountain": {
        "t": "MOUNTAIN",
        "e": True},
    "hills": {
        "t": "HILLS",
        "e": True},
        }

# current_tile = map[y][x]
# print(current_tile)
# name_of_tile = biom[current_tile]["t"]
# print(name_of_tile)
# enemy_tile = biom[current_tile]["e"]
# print(enemy_tile)

# Функция для очистки экрана
def clear():
    os.system("cls")

# Функция для вывода красивого разделителя на экран

def draw():
    print("Xx-----------------xX")
    
# Сохраняем параметры персонажа в файл. Если добавляются новые параметры, необходимо их сюда внести. Всё передлываем в строку, чтобы не было ошибок
def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(elix) ,
        str(gold),
        str(x),
        str(y),
        str(key),
        str(HPMAX),
    ]

    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()


#Основной ход игры
while run:
    while menu:
        
        draw()
        print("1, NEW GAME")
        print("2, LOAD GAME")
        print("3, RULES")
        print("4, QUIT GAME")
        draw()
        
        # Что будет выводиться при вызове правил.
        if rules:
            clear()
            draw()
            print ("Rules must be here")
            draw()
            rules = False
            choice = ""
            input("> ")
        else: 
             choice = input("# ")
        # Новая игра
        if choice == "1":
            clear()
            name = input("# What's your name, Hero? ")
            menu = False
            play = True
        #Загрузка игры с проверкой на количество строк(должно соответствовать количеству сохраняемых параметров), 
        elif choice == "2":  
            try:
                f = open("load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 10:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1]) 
                    elix = int(load_list[4][:-1]) 
                    gold = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    HPMAX = int(load_list[9][:-1])
                    print("Welcome back, " + name + "!")
                    input("> ")
                    menu = False
                    play = True
                else:
                    print("Corrupt save file!")
                    input("> ")
            except OSError:
                print("No save file!")
                input("> ")
        #Вызов правил
        elif choice == "3":
            rules = True
        #Выход из игры
        elif choice == "4":
            clear()
            quit()


    while play:
        save() #autosave
        draw()
        clear()
        draw()
        print("LOCATION: " + biom[map[y][x]]["t"])
        draw()
        print("NAME: " + name)
        print("HP: " + str(HP) + "/" + str(HPMAX))
        print("ATK: " + str(ATK))
        print("POTIONS: " + str(pot))
        print("ELIXIRS: " + str(elix)) 
        print("GOLD: " + str(gold))
        print("COORD: ", x, y)
        draw()
        print("0 - SAVE AND QUIT")
        print("1 - NORTH")
        print("2 - EAST")
        print("3 - SOUTH")
        print("4 - WEST")
        draw()


        dest = input("# ")
        # Описывыем перемещение. Если 0 то сохранение и выход.
        if dest == "0":
            play = False
            menu = True
            save()
        elif dest == "1":
            if y > 0:
                y -= 1
            else:
                y = y_len
        elif dest == "2":
            if x < x_len:
                x += 1
            else:
                x = 0
        elif dest == "3":
            if y < y_len:
                y += 1
            else:
                y = 0
        elif dest == "4":
            if x > 0:
                x -= 1
            else:
                x = x_len
            