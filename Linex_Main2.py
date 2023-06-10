import os, sys, time, re, json, datetime, random
from SettingApp import Setting
from App_Process import AppProcessLinex, SelectProgram, SelectPlatform
from ArhivatorLinexLib import ArhiveLinex, SelectArhive

dir_path = os.path.dirname(os.path.realpath(__file__))

platform_name=sys.argv[1] #Получить Платформу для доступа

app = Setting()
app_linex=AppProcessLinex(platform_name)
app_arhive=ArhiveLinex()

app = Setting()
app_linex=AppProcessLinex(platform_name)
app_arhive=ArhiveLinex()

Accesss=False #Доступ
filepath=""

while True:
    current_date = datetime.datetime.now()
    current_date_str = current_date.strftime("%d.%m.%Y %H:%M:%S")
    print(f"-------------------------{current_date_str}--------------------------")
    #-----------------Доступ-----------------
    app_linex.Access_Folder_Linex(dir_path,SelectPlatform.NONE) #Доступ
    #----------------------------------------
    print(f"Платформа: {platform_name}")
    #print("Скачать GPU-CPU=3")
    print("Выбрать CPU=1")
    print("Выбрать GPU=2")
    select=input("Выберете 1/2: ")
    # if select=="3":
    #     app_linex.DownLoad_Program(SelectProgram.CPU) #Проверка CPU
    #     app_linex.DownLoad_Program(SelectProgram.GPU) #Проверка GPU
    if select=="1":
        print("Выбрано CPU Медленый Процесс")
        print("dwn - если надо скачать hc22000 или cap")
        print("f - eсли надо указать путь к hc22000 или cap")
        hc22000cap=app.InputWhile("Команда dwn/f: ")
        if hc22000cap=="dwn":
            urldwn=app.InputWhile("Url: ")
            filepath=app.InputWhile("Имя файла hc22000 или cap: ")
            if app.LinkValid(urldwn)==False:
                print(f"Ссылка {urldwn} Указана Не Верно!")
            res=app_linex.DownLoad_HC220002(urldwn, filepath)
            filepath=res[1]
            Accesss=app.GetFileInfo(filepath)[0]
        if hc22000cap=="f":
            filepath=app.InputWhile("Имя файла hc22000 или cap: ")
            filecap=app_linex.app.SettingApp["FolderHC22000_Cap"]
            filepath=f"{dir_path}/{filecap}/{filepath}"
            Accesss=app.GetFileInfo(filepath)[0]
        if Accesss:
            print(f"Файл {filepath} Есть!")
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
                #---------------Скачивание Словарей---------------
                app_linex.DownLoad_Dicts_One(name_dict)
                #---------------Програма CPU----------------------
                commandsintez=app_linex.GetCommand(SelectProgram.CPU)
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
                #-----------------Доступ-----------------
                app_linex.Access_Folder_Linex(dir_path,SelectPlatform.NONE) #Доступ
                #----------------------------------------
                commandrun2=f'{commandsintez[0]} -w {commanddicts} "{dir_path}/{filecap}/{filepath}"'
                print(commandrun2)
                os.system(commandrun2)
            if selectdicts=="2":
                number_dict=app.InputWhile("Укажы Номер Пачки Словарей 1-3: ")
                #---------------Скачивание Словарей---------------
                number_dict=int(number_dict)
                app_linex.DownLoad_Dicts_Pack(number_dict)
                #---------------Програма CPU----------------------
                commandsintez=app_linex.GetCommand(SelectProgram.CPU)
                #-----------------Данные------------------
                folderdicts=app_linex.app.SettingApp["FolderDicts"]["Folder"]
                filecap=app_linex.app.SettingApp["FolderHC22000_Cap"]
                #-----------------Словари------------------
                commanddicts=""
                listdicts=app_linex.GetFilesPackDict(number_dict)
                for li in listdicts:
                    commanddicts+=f'"{dir_path}/{folderdicts}/{li}" '
                commanddicts=commanddicts[:-1]
                #----------------------------------------
                #-----------------Доступ-----------------
                app_linex.Access_Folder_Linex(dir_path,SelectPlatform.NONE) #Доступ
                #----------------------------------------
                commandrun2=f'{commandsintez[0]} -w {commanddicts} "{dir_path}/{filecap}/{filepath}"'
                print(commandrun2)
                #os.system(commandrun2)
            if selectdicts=="3":
                #---------------Скачивание Словарей---------------
                app_linex.DownLoad_Dicts_All()
                #---------------Програма CPU----------------------
                commandsintez=app_linex.GetCommand(SelectProgram.CPU)
                #-----------------Данные------------------
                folderdicts=app_linex.app.SettingApp["FolderDicts"]["Folder"]
                filecap=app_linex.app.SettingApp["FolderHC22000_Cap"]
                #-----------------Словари------------------
                commanddicts=""
                listdicts=app_linex.GetFilesAllDict()
                for li in listdicts:
                    commanddicts+=f'"{dir_path}/{folderdicts}/{li}" '
                commanddicts=commanddicts[:-1]
                #----------------------------------------
                #-----------------Доступ-----------------
                app_linex.Access_Folder_Linex(dir_path,SelectPlatform.NONE) #Доступ
                #----------------------------------------
                commandrun2=f'{commandsintez[0]} -w {commanddicts} "{dir_path}/{filecap}/{filepath}"'
                print(commandrun2)
                #os.system(commandrun2)
    if select=="2":
        print("Выбрано GPU Ускоренный Процесс")
        hc22000cap=app.InputWhile("Файлы hc22000, cap (dwn если надо скачать): ")
    elif select!="1" and select!="2":
        print("Не Выбрано 1 или 2")