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
    SHAB=1

def Main():
    shab: Shablon
    command_select=sys.argv[1] #Команда
    command_select=command_select.lower()
    if command_select == str(Commands.NONE.name.lower()):
        print("Тест!")
    if command_select == str(Commands.SHAB.name.lower()):
        fileshab=sys.argv[2]
        print(f"Шаблон: {fileshab}")
        res=setting.ReadShablon(fileshab)
        if res[0]:
            shab=res[2]
            #-------------Cap-------------
            setting.CreateDir(shab.CapDir)
            if shab.Run_Cap_Select=="dwn":
                res=setting.DownloadFile(shab.Run_Cap_Url,f"{dir_path}/{shab.Run_Cap_Path}")
            if shab.Run_Cap_Select=="f":
                pass 
            #-------------Словари---------
            if shab.Run_Dicts_Command=="0":
                print("--------------Словари--------------")
                pass
                # listdictsall=[]
                # for i,li in enumerate(app_service.GetNamesDicts()):
                #     print(f"{i}) {li}")
                #     listdictsall.append(li)
            if shab.Run_Dicts_Command=="1":
                pass 
            if shab.Run_Dicts_Command=="2":
                pass 
            if shab.Run_Dicts_Command=="3":
                pass 
    elif command_select != str(Commands.NONE.name.lower()) and \
        command_select != str(Commands.SHAB.name.lower()):
        print("Нету такой {0} команды!".format(command_select))


if __name__ == '__main__':
    Main()
