# import random
# from random import randint


# definition of the colors we will use.
BLACK = (0, 0, 0), 'BLACK'
WHITE = (255, 255, 255)
RED = (255, 0, 0), 'RED'
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
PINK = (255, 0, 255)
ORANGE = (255,145,0)
LIGHT_GREEN = (100,255,100)

# dict of colors and numbers with relations.
convertor = {
    0:'BLACK',
    1:'WHITE',
    2:'YELLOW',
    3:'BLUE',
    4:'CYAN',
    5:'RED',
    6:'PINK',
    7:'GREEN',
    8:'LIGHT_GREEN',
    9:'ORANGE'
}

# convert the 4 digits secret code to 4 correct colors. 
# add try/catch

def convertNumToColor(num):
    new_colors = []
    if num > 9:
        new_num = [int(x) for x in str(num)]
        for digit in new_num:
            new_colors.append(convertNumToColor(digit))
    elif num in convertor.keys():
        return convertor[num]
    else:
        return "wrong secret code!"
    return new_colors

# convert a color to a digit.
def convertColorToNum(color):
    for num, c in convertor.items():
        if c == color:
            return num

# convert a list of colors to a number.
def convertListColorsToNum(list_colors):
    new_num = []
    for color in list_colors:
        new_num.append(convertColorToNum(color))
        sec_num = convertListToInt(new_num)
    return sec_num

# convert a list of "int" to a number.
def convertListToInt(list):
    # Converting integer list to string list
    s = [str(i) for i in list]
    res = int("".join(s))
    return(res)


# print(convertNumToColor(1234))
# print(convertListColorsToNum([BLUE,GREEN,RED,YELLOW]))










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


