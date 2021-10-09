# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 15:51:32 2021

@author: ESHAN
"""
from pygame import mixer
import time

localtime = time.asctime(time.localtime(time.time()))

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break
        
def log_now(msg):
    f = open("E:\PROJECTS\PYTHON PROJECTS\HEALTH REMINDER\data\water, eyes & physical record.txt", "a") 
    if msg == "EyDone":
        f.write(f"\"I Have Done Eyes Exercise\"    [{time.asctime(time.localtime(time.time()))}]\n")
    if msg == "ExDone":
        f.write(f"\"I Have Done Physical Exercise\"    [{time.asctime(time.localtime(time.time()))}]\n")
    if msg == "Drank":
        f.write(f"\"I Have Drank Water\"    [{localtime}]\n")
initial_eyes_time = time.time()
initial_physical_time = time.time()
initial_water_time = time.time()

eyes_times = 30*60
pysical_time = 45*60
water_time = 60*60

while True: 
    if time.time() - initial_eyes_time > eyes_times:
        print("Time To Give Eyes Some Rest.....\n\n")
        print("Write \"EyDone\" to stop.")
        musiconloop("E:/PROJECTS/PYTHON PROJECTS/HEALTH REMINDER/data/alarm.mp3","EyDone")
        initial_eyes_time = time.time()
        log_now("EyDone")
    
    if time.time() - initial_physical_time > pysical_time:
        print("Time To Do Some Physical Movement.....\n\n")
        print("Write \"ExDone\" to stop.")
        musiconloop("E:/PROJECTS/PYTHON PROJECTS/HEALTH REMINDER/data/alarm.mp3","ExDone")
        initial_physical_time = time.time()
        log_now("ExDone")
    
    if time.time() - initial_water_time > water_time:
        print("Time To Drink Water For Healty Life.....\n\n")
        print("Write \"Drank\" to stop.")
        musiconloop("E:/PROJECTS/PYTHON PROJECTS/HEALTH REMINDER/data/alarm.mp3", "Drank")
        initial_water_time = time.time()
        log_now("Drank")
    
    
    

