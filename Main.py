import os, sys, time, re, json, datetime, random
from SettingApp import Setting
from App_Process import AppProcessLinex
from ArhivatorLib import ArhiveLinex, SelectArhive

dir_path = os.path.dirname(os.path.realpath(__file__))

platform_select=sys.argv[1].lower()

app = Setting()
app_linex=AppProcessLinex()
app_arhive=ArhiveLinex()

if platform_select=="linex":
    while True:
        current_date = datetime.datetime.now()
        current_date_str = current_date.strftime("%d.%m.%Y %H:%M:%S")
        print(f"-------------------------{current_date_str}--------------------------")
        select=input("Выберете CPU=1/GPU=2: ")
        if select=="1":
            print("Выбрано CPU Медленый Процесс")
            print("dwn - если надо скачать hc22000 или cap")
            print("f - eсли надо указать путь к hc22000 или cap")
            hc22000cap=app.InputWhile("Команда dwn/f: ")
            if hc22000cap=="dwn":
                urldwn=app.InputWhile("Url: ")
                filepath=app.InputWhile("Имя файла hc22000 или cap: ")
                mask=app.InputWhile("Маска WIFI: ")
                if app.LinkValid(urldwn) and app.MaskValide(mask):
                    res=app_linex.DownLoad_HC22000(urldwn, filepath)
                    if res:
                        print(f"Файл {filepath} Скачен!")
                        print("Список Словарей 0-Все Словари")
                        print("Способ Расшыфровки 1-один словарь")
                        print("Способ Расшыфровки 2-пачка словарей")
                        print("Способ Расшыфровки 3-все словари")
                        selectdicts=app.InputWhile("Выбрать способ Расшыфровки 0,1,2,3: ")
                        if selectdicts=="0":
                            for i,li in enumerate(app_linex.GetNamesDicts()):
                                print(f"{i}) {li}")
                        if selectdicts=="1":
                            name_dict=app.InputWhile("Укажы Имя Словаря: ")
                            res2=app_linex.DownLoad_Dicts_One(name_dict)
                            commandsintez=f""
                            print(commandsintez)
                        if selectdicts=="2":
                            number_dict=app.InputWhile("Укажы Номер Пачки Словарей 1-3: ")
                            number_dict=int(number_dict)
                            res2=app_linex.DownLoad_Dicts_Pack(number_dict)
                            commandsintez=f""
                            print(commandsintez)
                        if selectdicts=="3":
                            app_linex.DownLoad_Dicts_All()
                            commandsintez=f""
                            print(commandsintez)
                    else:
                        print(f"Файл {filepath} Не Скачен!")
                else:
                    print(f"Ссылка {urldwn} Указана Не Верно!")
                    print(f"Файла {filepath} по пути нету, укажыте другой!")
                    print(f"Или Маска {mask} Указана Не Верно!")
            if hc22000cap=="f":
                filepath=app.InputWhile("Путь к Файла hc22000, cap: ")
                mask=app.InputWhile("Маска WIFI: ")
                if app.MaskValide(mask) and app.GetFileInfo(filepath)[0]:
                    print(f"Файл {filepath}!")
                    print("Способ Расшыфровки 1-один словарь")
                    print("Способ Расшыфровки 2-пачка словарей")
                    print("Способ Расшыфровки 3-все словари")
                else:
                    print(f"Файла {filepath} по пути нету, укажыте другой!")
                    print(f"Или Маска {mask} Указана Не Верно!")
        if select=="2":
            print("Выбрано GPU Ускоренный Процесс")
            hc22000cap=app.InputWhile("Файлы hc22000, cap (dwn если надо скачать): ")
        elif select!="1" and select!="2":
            print("Не Выбрано 1 или 2")
if platform_select=="service":
    pass
if platform_select=="mobile":
    pass
if platform_select=="test":
    name_dict=input("Имя Архива: ")
    res=app_linex.DownLoad_Dicts_One(name_dict)
    print(res)
    app_arhive.Extract(name_dict,"Dirs", SelectArhive.SEVENZ)