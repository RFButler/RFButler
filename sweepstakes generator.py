# just a quick application I designed to play around with python and to learn more about it 

import random
from random import randrange

u_list = []  #user list
user = input("Input users followed by space: ")
u_list = user.split()

p_list = []  #player list (tbc)
players = input("Enter golfers group 1 followed by space: ")
p_list = players.split()
random.shuffle(p_list)

p_list1 = []  #player list (tbc)
players1 = input("Enter golfers group 2 followed by space: ")
p_list1 = players1.split()
random.shuffle(p_list1)

p_list2 = []  #player list (tbc)
players2 = input("Enter golfers group 3 followed by space: ")
p_list2 = players2.split()
random.shuffle(p_list2)

p_list3 = []  #player list (tbc)
players3 = input("Enter golfers group 4 followed by space: ")
p_list3 = players3.split()
random.shuffle(p_list3)

res = "\n".join("{} {} {} {} {}".format(x, y, z, a, b) for x, y, z, a, b in zip(u_list, p_list, p_list1, p_list2, p_list3))
print(res)
