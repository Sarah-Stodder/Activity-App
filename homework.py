import os
from colors import *
import requests



def output():
    while True:
        user_output = input("Bored? Find an Activity to try! Just type find! or Quit: ")
        if user_output[0].lower() == "q":
                print ("Ok.Bye Enjoy Your Activity")
                break
        elif user_output[0].lower()== "f":
             minn= input("What is your budgets minimum?: ")
             maxx =input("What is the maximum of your budget?: ")
             what_kind= input("What kind of activity would you like to try?: \n education \n recreational \n social \n diy  \n cooking  \n music \n busywork \n Type your choice: ")
             if what_kind[0].lower() == "d":
                kind="diy"
             elif what_kind[0].lower() == "e":
                kind="education"
             elif what_kind[0].lower() == "r":
                kind="recreational"
             elif what_kind[0].lower() == "s":
                kind="social"
             elif what_kind[0].lower() == "c":
                kind="cooking"
             elif what_kind[0].lower() == "m":
                kind="music"
             elif what_kind[0].lower() == "b":
                kind="busywork"
             else:
                return "You broke it!"
      

             url = f'http://www.boredapi.com/api/activity?type={kind}&minprice={minn}&maxprice={maxx}'
             response = requests.get(url)
             data = response.json()
             print_blue(f"Your random activity is: {data['activity']}")
             print_red(data['type'])
             print_yellow(f"This activity is ment for :{data['participants']} people to enjoy!")
             print_green(f"The estimated cost is: ${data['price']}")

        else:
                print("That is not a valid command stupido")
                break

output()