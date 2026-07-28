#math module
'''import math
print(math.pi) 
print(math.pi*3)
print(math.sqrt(2))
print(math.pow(2,2))
print(math.log(10))
print(math.tan(45))
print(math.cos(60))
print(math.sin(30))
print(math.ceil(4.9))
print(math.floor(6.9))'''

'''from math import pi,sqrt,log,tan
print(pi)
print(sqrt(2))
print(log(20))
print(tan(45))
print(cos(60))#error
print(math.pi)#error'''

#system(sys) module
'''import sys
print(sys.path)
print(sys.version)'''

#os module
'''import os
print(os.path)
print(os.getcwd())
print(os.listdir())
print(os.chdir("C:\\Users\\mythr\\Downloads"))
print(os.listdir())
print(os.mkdir("july27"))'''
#cwd-current working directory
#ch dir-change directory
#list dir-list directories in desktop 
#mkdir-making directory

#random module
'''import random
a=random.sample(range(20,40,),5) 
print(a)'''

#randint()
'''import random
a=random.randint(20,50)
print(a)'''

#choice()
'''import random
a=[10,30,50,60,80]
b=random.choice(a)
print(b)'''

#task
#dice code
while True:
    roll = int(input("Enter the roll of dice (1-6): "))

    if 1 <= roll <= 6:
        print("Dice shows:", roll)
    else:
        print("Invalid dice number!")

    option = int(input("Roll again?\n1. Yes\n2. No\nEnter your choice: "))

    if option == 2:
        print("Game Over!")
        break
    elif option != 1:
        print("Invalid choice! Exiting...")
        break


