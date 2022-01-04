import random
import os
from game_data import data
from art import logo
from art import vs
rep = 1
score =0

print(logo)

while rep >0:
    

    #choosing 1
    pickA = random.choice(list(data))
    print(pickA['name'])
    print("a ",pickA['description'])
    print("from ",pickA['country'])
    follow1 =pickA['follower_count']
    print(vs)

    #choosing 2
    pickB = random.choice(list(data))
    print(pickB['name'])
    print("a ",pickB['description'])
    print("from ",pickB['country'])
    follow2 =pickB['follower_count']

    choose = int(input("\nWho has more follower count??(1/2): "))

    if choose == 1:

      if follow1 >= follow2:
        print(f"correct {pickA['name']} has {follow1 - follow2} more followers  {pickB['name']} 🎉 🎉")
        score=score+1
        print(f"\n||your score = {score} ||\n")


      else:
        print(f"Naah {pickB['name']} has {follow2 - follow1} more followers  {pickA['name']}😥")
        rep=0
        print(f"\n||your score = {score} ||\n")
    elif choose==2:
        if follow2 >= follow1:
            print(f"correct {pickB['name']} has {follow2 - follow1} more followers  {pickA['name']} 🎉 🎉")
            score=score+1
            print(f"\n||your score = {score} ||\n")


        else:
            print(f"Naah {pickA['name']} has {follow1 - follow2} more followers  {pickB['name']}😥")
            rep=0
            print(f"\n||your score = {score} ||\n")
