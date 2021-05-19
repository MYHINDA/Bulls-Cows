# import random
# from random import randint

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
PINK = (255, 0, 255)
ORANGE = (255,145,0)
LIGHT_GREEN = (100,255,100)

convertor = {
    0:BLACK,
    1:WHITE,
    2:YELLOW,
    3:BLUE,
    4:CYAN,
    5:RED,
    6:PINK,
    7:GREEN,
    8:LIGHT_GREEN,
    9:ORANGE
}

def convertNumToColor(num):
    if num > 9:
        new_num = [int(x) for x in str(num)]
        new_colors = []
        for digit in new_num:
            new_colors.append(convertNumToColor(digit))
    if num in convertor.keys():
        return convertor[num]
    return new_colors

def convertColorToNum(color):
    for num, c in convertor.items():
        if c == color:
            return num

def convertListColorsToNum(list_colors):
    new_num = []
    for color in list_colors:
        new_num.append(convertColorToNum(color))
    return new_num




# class game(object):
#     color_list = [YELLOW, RED, GREEN, MAGENTA, BLUE, WHITE, BLACK, CYAN]
#     feedback_list = [YELLOW, RED]
#     def __init__(self, name, level):
#         self.name = name
#         self.level = level

#     def start(self):
#         # index
#     def play():
#         covered = random.choices(color_list,k=4)
#         guess = input() #4 colors
#         guesses = guess.split() #list of 4 colors
#         feedback = []
#         for g in guesses:
            



       
    

# def flow():
#     init()# enter your name and choose a level + checking name in table
#     start(name, level) #starting a game board
#     play() # moves and feedback + score
#     finish() # print total score + insert info to table


