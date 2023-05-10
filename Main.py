import os, sys, time, re, json, datetime, random
from SettingApp import Setting

dir_path = os.path.dirname(os.path.realpath(__file__))

platform_select=sys.argv[1].lower()

app = Setting()

if platform_select=="linex":
    while True:
        current_date = datetime.datetime.now()
        current_date_str = current_date.strftime("%d.%m.%Y %H:%M:%S")
        print(f"-------------------------{current_date_str}--------------------------")
        select=input("Выберете CPU=1/GPU=2: ")
        if select=="1":
            print("Выбрано CPU")
            hc22000cap=input("Файлы hc22000, cap: ")
            res=app.GetFileInfo(hc22000cap)
            mask=input("Маска WIFI: ")
            res2=app.MaskValide(mask)
            print(res)
            print(res2)
        if select=="2":
            print("Выбрано GPU")
            hc22000cap=input("Файлы hc22000, cap: ")
            res=app.GetFileInfo(hc22000cap)
            print(res)
        elif select!="1" and select!="2":
            print("Не Выбрано 1 или 2")
if platform_select=="service":
    pass
if platform_select=="mobile":
    pass