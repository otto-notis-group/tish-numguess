#numguess
from typing import Literal
import requests as rq
import os
import random as rn
def genrate():
    switch=rn.choice([1,2,3,4,5,6,7,8,9])
    print(switch)
    if switch==1:
        import time as tm
        return float(tm.strftime("%Y%H%M%S%S%Y"))+rn.uniform(1.0,0.3),"Tip:Current time (format:%Y%H%M%S%S%Y) + a random float between 0 and 1"
    elif switch==2:
        import tempfile
        return float(os.path.getsize(tempfile.gettempdir())+len(rq.get(rn.choice(["https://example.com","https://python.org"])).content)),"Tip:Size of temp directory + length(in bytes) of https://example.com/ or https://python.org/"
    elif switch==3:
        return float(int(rn.choice(["US","CN","JP","IN","GB","RU"])+rn.choice(["US","CN","JP","IN","GB","RU"]),36)+rn.uniform(1.0,0.3)),"Tip:Base 36 sum of 2 country codes + a random float between 0 and 1"
    elif switch==4:
        import sys
        return rn.uniform(sys.float_info.max,sys.float_info.min),"Tip:Random float between sys.float_info.max and sys.float_info.min"
    else:return genrate()
def numguess(n:float,target: float)-> str|Literal[""]:
    rtr=""
    if n>target:
        rtr+="Too high"
    elif n<target:rtr+="Too low"
    if len(str(int(n)))>len(str(int(target))):
        rtr+= " and too long on int part"
    elif len(str(int(n)))<len(str(int(target))):
        rtr+= " and too short on int part"
    if len(str(n).split(".")[1])>len(str(target).split(".")[1]):
        rtr+= " and too long on float part"
    elif len(str(n).split(".")[1])<len(str(target).split(".")[1]):
        rtr+= " and too short on float part"
    return rtr
print("Welcome to the number guessing game!")
while True:
    tgt,tip=genrate()
    rrst=True
    while rrst:
        print(tip)
        print(f"Length:{len(str(tgt))}")
        rst=float(input("Guess the number: "))
        print(f"floated:{rst}")
        rrst=numguess(rst,tgt)
        print(rrst)
    print("You guessed it!")

    