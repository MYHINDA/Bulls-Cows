import random
import convertNumAndColor as cnac


def getDigits(num):
    return [int(i) for i in str(num)]   

def noDuplicates(num):
    num_li = getDigits(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False
  
# secret code  
def generateNum():
    while True:
        num = random.randint(1000,9999)
        if noDuplicates(num):
            # secret_colors = cnac.convertNumToColor(num)
            # return secret_colors
            return num

def numOfBullsCows(num,guess):
    bull_cow = [0,0]
    num_li = getDigits(num)
    guess_li = getDigits(guess)
      
    for i,j in zip(num_li,guess_li):
        if j in num_li:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1 
    return bull_cow

# start play   
num = generateNum()
tries =int(input('Enter number of tries: '))

# lower level is to change the condition to while True
while tries > 0:
    user_guess_color_str = input("Enter your guess: ")
    user_guess_color = user_guess_color_str.split()
    user_guess_num = cnac.convertListColorsToNum(user_guess_color)
      
    if not noDuplicates(user_guess_num):#for higher lever, we let duplicates.
        print("you have repeated colors. Try again.")
        continue
    if len(str(user_guess_num)) != 4:
        print("Enter 4 colors only. Try again.")
        continue
      
    bull_cow = numOfBullsCows(num,user_guess_num)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    tries -=1
      
    if bull_cow[0] == 4:
        print("You guessed right!")
        break
else:
    secret_colors = ', '.join(cnac.convertNumToColor(num))
    print(f"You ran out of tries. colors are {secret_colors}")
