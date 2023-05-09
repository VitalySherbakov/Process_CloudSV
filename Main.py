import os, sys, time, re, json, datetime, random
from SettingApp import Setting

print("Скрипт Успешно запущен!")

app = Setting()

while True:
    select=input("Выберете CPU=1/GPU=2: ")
    if select=="1":
        print("Выбрано CPU")
    if select=="2":
        print("Выбрано GPU")
    elif select!="1" and select!="2":
        print("Не Выбрано 1 или 2")