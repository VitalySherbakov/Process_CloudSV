import os, sys, time, re, json, datetime, random
from SettingApp import Setting
from App_Process import AppProcessLinex, SelectProgram
from ArhivatorLinexLib import ArhiveLinex, SelectArhive

dir_path = os.path.dirname(os.path.realpath(__file__))

platform_name=sys.argv[1] #Получить Платформу для доступа

app = Setting()
app_linex=AppProcessLinex(platform_name)
app_arhive=ArhiveLinex()

app = Setting()
app_linex=AppProcessLinex(platform_name)
app_arhive=ArhiveLinex()

while True:
    current_date = datetime.datetime.now()
    current_date_str = current_date.strftime("%d.%m.%Y %H:%M:%S")
    print(f"-------------------------{current_date_str}--------------------------")
    print(f"Платформа: {platform_name}")
    print("Скачать GPU-CPU=3")
    print("Выбрать CPU=1")
    print("Выбрать GPU=2")
    select=input("Выберете 1/2/3: ")
    if select=="3":
        app_linex.DownLoad_Program(SelectProgram.CPU) #Проверка CPU
        app_linex.DownLoad_Program(SelectProgram.GPU) #Проверка GPU
    if select=="1":
        print("Выбрано CPU Медленый Процесс")
        print("dwn - если надо скачать hc22000 или cap")
        print("f - eсли надо указать путь к hc22000 или cap")
        hc22000cap=app.InputWhile("Команда dwn/f: ")
        if hc22000cap=="dwn":
            urldwn=app.InputWhile("Url: ")
            filepath=app.InputWhile("Имя файла hc22000 или cap: ")
            # mask=app.InputWhile("Маска WIFI: ")
            if app.LinkValid(urldwn)==False:
                print(f"Ссылка {urldwn} Указана Не Верно!")
            # if app.MaskValide(mask)==False:
            #     print(f"Или Маска {mask} Указана Не Верно!")
            if app.LinkValid(urldwn):
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
                        commandsintez=app_linex.GetCommand(SelectProgram.CPU)
                        #print(f"cd {commandsintez[2]}")
                        #os.system(f"cd {commandsintez[2]}") #переход к програме
                        #-----------------Тест------------------
                        #os.system(f"{commandsintez[0]} --help")
                        #-----------------Данные------------------
                        folderdicts=app_linex.app.SettingApp["FolderDicts"]["Folder"]
                        filecap=app_linex.app.SettingApp["FolderHC22000_Cap"]
                        #-----------------Словари------------------
                        commanddicts=""
                        listdicts=app_linex.GetFilesFindDict(name_dict)
                        for li in listdicts:
                            commanddicts+=f'"{dir_path}/{folderdicts}/{li}" '
                        commanddicts=commanddicts[:-1]
                        #----------------------------------------
                        #commandrun=f'{commandsintez[0]} -w {commanddicts} -b "{mask}" "{dir_path}/{filecap}/{filepath}"'
                        commandrun2=f'{commandsintez[0]} -w {commanddicts} "{dir_path}/{filecap}/{filepath}"'
                        print(commandrun2)
                        os.system(commandrun2)
                    if selectdicts=="2":
                        number_dict=app.InputWhile("Укажы Номер Пачки Словарей 1-3: ")
                        number_dict=int(number_dict)
                        res2=app_linex.DownLoad_Dicts_Pack(number_dict)
                        commandsintez=app_linex.GetCommand(SelectProgram.CPU)
                        os.system(f"cd {commandsintez[2]}") #переход к програме
                        os.system(f"{commandsintez[0]} --help")
                    if selectdicts=="3":
                        app_linex.DownLoad_Dicts_All()
                        platform=app_linex.GetPlatform(platform_name)
                        commandsintez=app_linex.GetCommand(SelectProgram.CPU,platform)
                        os.system(f"cd {commandsintez[2]}") #переход к програме
                        os.system(f"{commandsintez[0]} --help")
                else:
                    print(f"Файл {filepath} Не Скачен!")
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
    elif select!="1" and select!="2" and select!="3":
        print("Не Выбрано 1 или 2")