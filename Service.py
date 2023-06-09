import os, sys, time, re, json, datetime, random
from enum import Enum
from SettingService import Setting, Shablon
from App_Process2 import AppProcessLinex, SelectProgram, SelectPlatform

dir_path = os.path.dirname(os.path.realpath(__file__))

#---------Библиотека-----------
setting=Setting()
app_service=AppProcessLinex("none")
#------------------------------

class Commands(Enum):
    """Команды"""
    NONE=0,
    SHAB=1,
    PROG=2,
    TEST=3

def Main():
    listdictsall=[] #Список Имен Словарей
    filepath="" #Cap Файлы
    shab: Shablon
    command_select=sys.argv[1] #Команда
    commandrun2_new=""
    #-----------------Данные------------------
    folderdicts=app_service.app.SettingApp["FolderDicts"]["Folder"]
    filecap=app_service.app.SettingApp["FolderHC22000_Cap"]
    #----------------------------------------
    command_select=command_select.lower()
    #----------------------------------------
    if command_select == str(Commands.PROG.name.lower()):
        progsel=sys.argv[2]
        progsel=progsel.lower()
        print(f"Програма: {progsel}")
        if progsel=="cpu":
            app_service.Download_ProgramNew(SelectProgram.CPU)
        if progsel=="gpu":
            app_service.Download_ProgramNew(SelectProgram.GPU)
        print(f"Програма {progsel} Загружена!")
    if command_select == str(Commands.TEST.name.lower()):
        progsel=sys.argv[2]
        progsel=progsel.lower()
        print(f"Програма: {progsel}")
        #---------------Програма CPU/GPU----------------------
        commandsintez=None
        if progsel=="cpu":
            commandsintez=app_service.GetCommand(SelectProgram.CPU)
        if progsel=="gpu":
            commandsintez=app_service.GetCommand(SelectProgram.GPU)
        command1=f"chmod +x {commandsintez[1]}"
        command2=f"{commandsintez[1]} --help"
        #print(command1)
        #print(command2)
        os.system(command1)
        os.system(command2)
    if command_select == str(Commands.NONE.name.lower()):
        print("Тест!")
    if command_select == str(Commands.SHAB.name.lower()):
        fileshab=sys.argv[2]
        print(f"Шаблон: {fileshab}")
        res=setting.ReadShablon(fileshab)
        if res[0]:
            shab=res[2]
            #-------------Cap-------------
            setting.CreateDir(f"{dir_path}/{shab.CapDir}") #Создание папки Cap
            if shab.Run_Cap_Select=="dwn":
                res=setting.DownloadFile(shab.Run_Cap_Url,f"{dir_path}/{shab.Run_Cap_Path}")
                filepath=f"{dir_path}/{shab.Run_Cap_Path}"
            if shab.Run_Cap_Select=="f":
                filepath=f"{dir_path}/{shab.Run_Cap_Path}" 
            #----------------Словари-------------------
            print("--------------Словари--------------")
            for i,li in enumerate(app_service.GetNamesDicts()):
                print(f"{i}) {li}")
                listdictsall.append(li)
            #-------------Словари Команды--------------
            if shab.Run_Dicts_Command=="0":
                pass
            if shab.Run_Dicts_Command=="1":
                numselect_dict=int(shab.Run_Dicts_Select)
                name_dict=listdictsall[numselect_dict]
                print(f"Выбран Словарь: {name_dict}")
                #---------------Скачивание Словарей---------------
                app_service.DownLoad_Dicts_One(name_dict)
                #---------------Програма CPU/GPU----------------------
                commandsintez=None
                if shab.Select_Program=="cpu":
                    commandsintez=app_service.GetCommand(SelectProgram.CPU)
                if shab.Select_Program=="gpu":
                    commandsintez=app_service.GetCommand(SelectProgram.GPU)
                #-----------------Словари------------------
                commanddicts=""
                listdicts=app_service.GetFilesFindDict(name_dict)
                for li in listdicts:
                    commanddicts+=f'"{dir_path}/{folderdicts}/{li}" '
                commanddicts=commanddicts[:-1]
                #----------------------------------------
                #-----------------Доступ-----------------
                app_service.Access_Folder_Linex(dir_path,SelectPlatform.NONE) #Доступ
                #----------------------------------------
                if shab.Select_Program=="cpu":
                    command1=f"chmod +x {commandsintez[1]}"
                    os.system(command1)
                    commandrun2=f'{commandsintez[1]} -w {commanddicts} "{filepath}"'
                    print(commandrun2)
                    os.system(commandrun2)
                    commandrun2_new=commandrun2
                if shab.Select_Program=="gpu":
                    command1=f"chmod +x {commandsintez[1]}"
                    os.system(command1)
                    commandrun2=f'{commandsintez[1]} -m 22000 -a 0 -w 1 "{filepath}" {commanddicts}'
                    print(commandrun2)
                    os.system(commandrun2)
                    commandrun2_new=commandrun2
            if shab.Run_Dicts_Command=="2":
                #---------------Скачивание Словарей---------------
                number_dict=int(shab.Run_Dicts_Select)
                app_service.DownLoad_Dicts_Pack(number_dict)
                #---------------Програма CPU/GPU----------------------
                commandsintez=None
                if shab.Select_Program=="cpu":
                    commandsintez=app_service.GetCommand(SelectProgram.CPU)
                if shab.Select_Program=="gpu":
                    commandsintez=app_service.GetCommand(SelectProgram.GPU)
                #-----------------Словари------------------
                commanddicts=""
                listdicts=app_service.GetFilesPackDict(number_dict, shab.Arhive_Pack1, shab.Arhive_Pack2, shab.Arhive_Pack3)
                for li in listdicts:
                    commanddicts+=f'"{dir_path}/{folderdicts}/{li}" '
                commanddicts=commanddicts[:-1]
                #----------------------------------------
                #-----------------Доступ-----------------
                app_service.Access_Folder_Linex(dir_path,SelectPlatform.NONE) #Доступ
                #----------------------------------------
                if shab.Select_Program=="cpu":
                    command1=f"chmod +x {commandsintez[1]}"
                    os.system(command1)
                    commandrun2=f'{commandsintez[1]} -w {commanddicts} "{filepath}"'
                    print(commandrun2)
                    os.system(commandrun2)
                    commandrun2_new=commandrun2
                if shab.Select_Program=="gpu":
                    command1=f"chmod +x {commandsintez[1]}"
                    os.system(command1)
                    commandrun2=f'{commandsintez[1]} -m 22000 -a 0 -w 1 "{filepath}" {commanddicts}'
                    print(commandrun2)
                    os.system(commandrun2)
                    commandrun2_new=commandrun2
            if shab.Run_Dicts_Command=="3":
                #---------------Скачивание Словарей---------------
                app_service.DownLoad_Dicts_All()
                #---------------Програма CPU/GPU----------------------
                commandsintez=None
                if shab.Select_Program=="cpu":
                    commandsintez=app_service.GetCommand(SelectProgram.CPU)
                if shab.Select_Program=="gpu":
                    commandsintez=app_service.GetCommand(SelectProgram.GPU)
                #-----------------Словари------------------
                commanddicts=""
                listdicts=app_service.GetFilesAllDict()
                for li in listdicts:
                    commanddicts+=f'"{dir_path}/{folderdicts}/{li}" '
                commanddicts=commanddicts[:-1]
                #----------------------------------------
                #-----------------Доступ-----------------
                app_service.Access_Folder_Linex(dir_path,SelectPlatform.NONE) #Доступ
                #----------------------------------------
                if shab.Select_Program=="cpu":
                    command1=f"chmod +x {commandsintez[1]}"
                    os.system(command1)
                    commandrun2=f'{commandsintez[1]} -w {commanddicts} "{filepath}"'
                    print(commandrun2)
                    os.system(commandrun2)
                    commandrun2_new=commandrun2
                if shab.Select_Program=="gpu":
                    command1=f"chmod +x {commandsintez[1]}"
                    os.system(command1)
                    commandrun2=f'{commandsintez[1]} -m 22000 -a 0 -w 1 "{filepath}" {commanddicts}'
                    print(commandrun2)
                    os.system(commandrun2)
                    commandrun2_new=commandrun2
    elif command_select != str(Commands.NONE.name.lower()) and \
        command_select != str(Commands.PROG.name.lower()) and \
        command_select != str(Commands.TEST.name.lower()) and \
        command_select != str(Commands.SHAB.name.lower()):
        print("Нету такой {0} команды!".format(command_select))
    return commandrun2_new
    


if __name__ == '__main__':
    Main()
