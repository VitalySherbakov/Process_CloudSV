import os, sys, time, re, json, datetime, random
from SettingApp import Setting
from App_Process import AppProcessLinex, SelectProgram, SelectPlatform
from ArhivatorLinexLib import ArhiveLinex, SelectArhive

dir_path = os.path.dirname(os.path.realpath(__file__))

#platform_name=sys.argv[1] #Получить Платформу для доступа
platform_name="None"
sessionfile="home.session"
sessionfile=f"{dir_path}/{sessionfile}"

app = Setting()
app_linex=AppProcessLinex(platform_name)
app_arhive=ArhiveLinex()

Accesss=False #Доступ
filepath, filenamecap="",""

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
        print("--------------Пароль--------------")
        listwifis=app_linex.Get_Pass_Files()
        for passw in listwifis:
            print(f'{passw["Number"]}) {passw["File"]} - [{passw["Pass"]}]')
        print("----------------------------------")
        print("--------------Cap--------------")
        listwifis=[]
        listwifis=app_linex.Get_HC22000_Files()
        for wifi in listwifis:
            print(f'{wifi["Number"]}) {wifi["File"]}')
        print("-------------------------------")
        print("s - если надо выбрать cap")
        print("dwn - если надо скачать cap")
        print("f - eсли надо указать путь к cap")
        hc22000cap=app.InputWhile("Команда s/dwn/f: ")
        if hc22000cap=="dwn":
            urldwn=app.InputWhile("Url: ")
            filepath=app.InputWhile("Имя файла cap: ")
            if app.LinkValid(urldwn)==False:
                print(f"Ссылка {urldwn} Указана Не Верно!")
            res=app_linex.DownLoad_HC220002(urldwn, filepath)
            filepath=res[1]
            capres=app.GetFileInfo(filepath)
            Accesss=capres[0]
            filenamecap=capres[1]
        if hc22000cap=="f":
            filepath=app.InputWhile("Имя файла cap: ")
            filecap=app_linex.app.SettingApp["FolderHC22000_Cap"]
            filepath=f"{dir_path}/{filecap}/{filepath}"
            capres=app.GetFileInfo(filepath)
            Accesss=capres[0]
            filenamecap=capres[1]
        if hc22000cap=="s":
            numbercap=app.InputWhile("Выбрать по номеру cap: ")
            numbersel=int(numbercap)
            filepath=listwifis[numbersel]["File"]
            filecap=app_linex.app.SettingApp["FolderHC22000_Cap"]
            filepath=f"{dir_path}/{filecap}/{filepath}"
            capres=app.GetFileInfo(filepath)
            Accesss=capres[0]
            filenamecap=capres[1]
        if Accesss:
            print(f"Файл {filepath} Есть!")
            print("--------------Словари--------------")
            listdictsall=[]
            for i,li in enumerate(app_linex.GetNamesDicts()):
                    print(f"{i}) {li}")
                    listdictsall.append(li)
            print("Способ Расшыфровки 1-один словарь")
            print("Способ Расшыфровки 2-пачка словарей")
            print("Способ Расшыфровки 3-все словари")
            selectdicts=app.InputWhile("Выбрать способ Расшыфровки 1,2,3: ")
            if selectdicts=="1":
                numselect_dict=app.InputWhile("Номер Словаря: ")
                numselect_dict=int(numselect_dict)
                name_dict=listdictsall[numselect_dict]
                print(f"Выбран Словарь: {name_dict}")
                #---------------Скачивание Словарей---------------
                app_linex.DownLoad_Dicts_One(name_dict)
                #---------------Програма CPU----------------------
                commandsintez=app_linex.GetCommand(SelectProgram.CPU)
                #-----------------Данные------------------
                folderdicts=app_linex.app.SettingApp["FolderDicts"]["Folder"]
                filecap=app_linex.app.SettingApp["FolderHC22000_Cap"]
                folderpass=app_linex.app.SettingApp["FolderPassSave"]
                #-----------------Папка Паролями------------------
                app.CreateDir(folderpass) #создание папки
                filepass=f"{dir_path}/{folderpass}/{filenamecap}.txt"
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
                commandrun2=""
                existsession=app.GetFileInfo(sessionfile)[0] #наличие сессии
                if existsession:
                    #commandrun2=f'{commandsintez[0]} -w {commanddicts} -R "{sessionfile}" -l "{filepass}" "{filepath}"'
                    commandrun2=f'{commandsintez[0]} -R "{sessionfile}"'
                else:
                    commandrun2=f'{commandsintez[0]} -w {commanddicts} -N "{sessionfile}" -l "{filepass}" "{filepath}"'
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
                folderpass=app_linex.app.SettingApp["FolderPassSave"]
                #-----------------Папка Паролями------------------
                app.CreateDir(folderpass) #создание папки
                filepass=f"{dir_path}/{folderpass}/{filenamecap}.txt"
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
                commandrun2=""
                existsession=app.GetFileInfo(sessionfile)[0] #наличие сессии
                if existsession:
                    #commandrun2=f'{commandsintez[0]} -w {commanddicts} -R "{sessionfile}" -l "{filepass}" "{filepath}"'
                    commandrun2=f'{commandsintez[0]} -R "{sessionfile}"'
                else:
                    commandrun2=f'{commandsintez[0]} -w {commanddicts} -N "{sessionfile}" -l "{filepass}" "{filepath}"'
                print(commandrun2)
                os.system(commandrun2)
            if selectdicts=="3":
                #---------------Скачивание Словарей---------------
                app_linex.DownLoad_Dicts_All()
                #---------------Програма CPU----------------------
                commandsintez=app_linex.GetCommand(SelectProgram.CPU)
                #-----------------Данные------------------
                folderdicts=app_linex.app.SettingApp["FolderDicts"]["Folder"]
                filecap=app_linex.app.SettingApp["FolderHC22000_Cap"]
                folderpass=app_linex.app.SettingApp["FolderPassSave"]
                #-----------------Папка Паролями------------------
                app.CreateDir(folderpass) #создание папки
                filepass=f"{dir_path}/{folderpass}/{filenamecap}.txt"
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
                commandrun2=""
                existsession=app.GetFileInfo(sessionfile)[0] #наличие сессии
                if existsession:
                    #commandrun2=f'{commandsintez[0]} -w {commanddicts} -R "{sessionfile}" -l "{filepass}" "{filepath}"'
                    commandrun2=f'{commandsintez[0]} -R "{sessionfile}"'
                else:
                    commandrun2=f'{commandsintez[0]} -w {commanddicts} -N "{sessionfile}" -l "{filepass}" "{filepath}"'
                print(commandrun2)
                os.system(commandrun2)
    if select=="2":
        print("Выбрано GPU Ускоренный Процесс")
        print("--------------Пароль--------------")
        listwifis=app_linex.Get_Pass_Files()
        for passw in listwifis:
            print(f'{passw["Number"]}) {passw["File"]} - [{passw["Pass"]}]')
        print("----------------------------------")
        print("--------------hc22000--------------")
        listwifis=[]
        listwifis=app_linex.Get_HC22000_Files()
        for wifi in listwifis:
            print(f'{wifi["Number"]}) {wifi["File"]}')
        print("s - если надо выбрать hc22000")
        print("dwn - если надо скачать hc22000")
        print("f - eсли надо указать путь к hc22000")
        hc22000cap=app.InputWhile("Команда s/dwn/f: ")
        if hc22000cap=="dwn":
            urldwn=app.InputWhile("Url: ")
            filepath=app.InputWhile("Имя файла hc22000: ")
            if app.LinkValid(urldwn)==False:
                print(f"Ссылка {urldwn} Указана Не Верно!")
            res=app_linex.DownLoad_HC220002(urldwn, filepath)
            filepath=res[1]
            Accesss=app.GetFileInfo(filepath)[0]
        if hc22000cap=="f":
            filepath=app.InputWhile("Имя файла hc22000: ")
            filecap=app_linex.app.SettingApp["FolderHC22000_Cap"]
            filepath=f"{dir_path}/{filecap}/{filepath}"
            Accesss=app.GetFileInfo(filepath)[0]
        if hc22000cap=="s":
            numbercap=app.InputWhile("Выбрать по номеру hc22000: ")
            numbersel=int(numbercap)
            filepath=listwifis[numbersel]["File"]
            filecap=app_linex.app.SettingApp["FolderHC22000_Cap"]
            filepath=f"{dir_path}/{filecap}/{filepath}"
            Accesss=app.GetFileInfo(filepath)[0]
        if Accesss:
            print(f"Файл {filepath} Есть!")
            print("--------------Словари--------------")
            listdictsall=[]
            for i,li in enumerate(app_linex.GetNamesDicts()):
                    print(f"{i}) {li}")
                    listdictsall.append(li)
            print("Способ Расшыфровки 1-один словарь")
            print("Способ Расшыфровки 2-пачка словарей")
            print("Способ Расшыфровки 3-все словари")
            selectdicts=app.InputWhile("Выбрать способ Расшыфровки 1,2,3: ")
            if selectdicts=="1":
                numselect_dict=app.InputWhile("Укажы Имя Словаря: ")
                numselect_dict=int(numselect_dict)
                name_dict=listdictsall[numselect_dict]
                print(f"Выбран Словарь: {name_dict}")
                #---------------Скачивание Словарей---------------
                app_linex.DownLoad_Dicts_One(name_dict)
                #---------------Програма CPU----------------------
                commandsintez=app_linex.GetCommand(SelectProgram.GPU)
                #-----------------Данные------------------
                folderdicts=app_linex.app.SettingApp["FolderDicts"]["Folder"]
                filecap=app_linex.app.SettingApp["FolderHC22000_Cap"]
                folderpass=app_linex.app.SettingApp["FolderPassSave"]
                #-----------------Папка Паролями------------------
                app.CreateDir(folderpass) #создание папки
                filepass=f"{dir_path}/{folderpass}/{filenamecap}.txt"
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
                commandrun2=f'{commandsintez[0]} -m 22000 -a 0 -w 1 "{filepath}" {commanddicts}'
                #print(commandrun2)
                os.system(commandrun2)
            if selectdicts=="2":
                number_dict=app.InputWhile("Укажы Номер Пачки Словарей 1-3: ")
                #---------------Скачивание Словарей---------------
                number_dict=int(number_dict)
                app_linex.DownLoad_Dicts_Pack(number_dict)
                #---------------Програма CPU----------------------
                commandsintez=app_linex.GetCommand(SelectProgram.GPU)
                #-----------------Данные------------------
                folderdicts=app_linex.app.SettingApp["FolderDicts"]["Folder"]
                filecap=app_linex.app.SettingApp["FolderHC22000_Cap"]
                folderpass=app_linex.app.SettingApp["FolderPassSave"]
                #-----------------Папка Паролями------------------
                app.CreateDir(folderpass) #создание папки
                filepass=f"{dir_path}/{folderpass}/{filenamecap}.txt"
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
                commandrun2=f'{commandsintez[0]} -m 22000 -a 0 -w 1 "{filepath}" {commanddicts}'
                #print(commandrun2)
                os.system(commandrun2)
            if selectdicts=="3":
                #---------------Скачивание Словарей---------------
                app_linex.DownLoad_Dicts_All()
                #---------------Програма CPU----------------------
                commandsintez=app_linex.GetCommand(SelectProgram.GPU)
                #-----------------Данные------------------
                folderdicts=app_linex.app.SettingApp["FolderDicts"]["Folder"]
                filecap=app_linex.app.SettingApp["FolderHC22000_Cap"]
                folderpass=app_linex.app.SettingApp["FolderPassSave"]
                #-----------------Папка Паролями------------------
                app.CreateDir(folderpass) #создание папки
                filepass=f"{dir_path}/{folderpass}/{filenamecap}.txt"
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
                commandrun2=f'{commandsintez[0]} -m 22000 -a 0 -w 1 "{filepath}" {commanddicts}'
                #print(commandrun2)
                os.system(commandrun2)
    elif select!="1" and select!="2":
        print("Не Выбрано 1 или 2")