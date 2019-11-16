# @Time :2019/11/12 13:54
# @Auther :Ming
# @Software: PyCharm
import random
def shaizi():
        dice_tpl= '''\
        ┌─────────┐,┌─────────┐,┌─────────┐,┌─────────┐,┌─────────┐,┌─────────┐
        │         │,│    ●    │,│●        │,│ ●     ● │,│ ●     ● │,│ ●     ● │
        │    ●    │,│         │,│    ●    |,│         │,│    ●    │,│ ●     ● │
        │         │,│    ●    │,│        ●│,│ ●     ● │,│ ●     ● │,│ ●     ● │
        └─────────┘,└─────────┘,└─────────┘,└─────────┘,└─────────┘,└─────────┘'''
        i = 0
        j = 0
        dice_lines = dice_tpl.split('\n')
        while i < 5:
            dice_lines[i] = dice_lines[i].split(',')
            i = i + 1

        dice = []
        for i in range(6):
            dice.append(dice_lines[0][i]+'\n'+dice_lines[1][i]+'\n'+dice_lines[2][i]+'\n'+ dice_lines[3][i] +'\n'+ dice_lines[4][i])
        while(1):
            print('If points >= 10 belong to big, < 10 belong to small ')
            number = int(input('Please select your options:  big(0)  or  small(1)  exit(2)\n'))
            if number == 2:
                break
            sum = 0
            for i in range(3):
                j = random.randint(1,6)
                sum = sum + j
                print(dice[j-1])
            if((sum >= 10 and number == 0)or(sum < 10 and number == 1)):
                print('the points is :%d'%sum)
                print('Congratulations on your guess')
            else:
                print('the points is :%d' % sum)
                print('sorry,your guess is wrong')
        print('thanks for you try,welcome next time come back')
