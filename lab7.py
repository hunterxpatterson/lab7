x = 1

while (x < 300):
    print x
    x = x + 2

myList = [1,2,3,4,5,6,7,8,9,10]
index = 0

while (index < len(myList)):
        print myList[index]
        index = index + 1
     
print 'Guess 1 thru 50'
import random
rand = random.randint(0,50)
userInput = int(raw_input())

while (userInput!=rand):
    userInput = int(raw_input())
    if userInput < rand:
        print 'too low'
    elif userInput > rand:
        print 'too high'
    else:
        print 'Correct'
    