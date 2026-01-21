import math

root = math.sqrt(36)
from math import sqrt , pi


import random 

number = random.randint(1,10)

choice = random.choice(["apple" , "banana", "grapes", "orange"])

print("Number : " , number)
print("Choice :", choice)


import datetime

today = datetime.date.today()
 
print(today)

import os 

curr_dir = os.getcwd()

print("Current directory: " , curr_dir)


import json


data = {"name": "gaurav" , "age" : 25}

json_strin = json.dumps(data)

print(json_strin)