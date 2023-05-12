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
            print("Выбрано CPU Медленый Процесс")
            hc22000cap=app.InputWhile("Файлы hc22000, cap (dwn если надо скачать): ")
            if hc22000cap=="dwn":
                urldwn=app.InputWhile("Url: ")
                filepath=app.InputWhile("Файлы hc22000, cap: ")
                mask=app.InputWhile("Маска WIFI: ")
                if app.LinkValid(urldwn) and app.MaskValide(mask) and app.GetFileInfo(filepath)[0]:
                    res=app.DownloadFile(urldwn, filepath)
                    if res:
                        print(f"Файл {filepath} Скачен!")
        if select=="2":
            print("Выбрано GPU Ускоренный Процесс")
            hc22000cap=input("Файлы hc22000, cap (dwn если надо скачать): ")
        elif select!="1" and select!="2":
            print("Не Выбрано 1 или 2")
if platform_select=="service":
    pass
if platform_select=="mobile":
    pass