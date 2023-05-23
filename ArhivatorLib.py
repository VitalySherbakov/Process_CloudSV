import py7zr,zipfile,rarfile,os,sys
from enum import Enum
from alive_progress import alive_bar
#---------------------
# pip install alive-progress
# pip install py7zr
# pip install zip_files - Встроеная zip_files иногда не обязательно устанавливать
# pip install rarfile
#---------------------

class SelectArhive(Enum):
    """Выбор Архиватора"""
    RAR=1
    """RAR Архив (Упаковка с Ошыбкой, Распаковка тоже)"""
    ZIP=2
    """ZIP Архив"""
    SEVENZ=3
    """7z Архив"""

class Arhive(object):
    """Архиваторы"""
    def __init__(self):
        super(Arhive, self).__init__()
        pass
    def Pack(self, dir: str, arhive_name: str, select: SelectArhive):
        """Создание Архива"""
        Flag,arhivepath=False,""
        if select==SelectArhive.SEVENZ:
            arhivepath=f"{arhive_name}.7z"
            with py7zr.SevenZipFile(arhivepath, 'w') as archive:
                archive.writeall(dir)
                Flag=True
        if select==SelectArhive.ZIP:
            arhivepath=f"{arhive_name}.zip"
            with zipfile.ZipFile(arhivepath, 'w') as archive:
                archive.write(dir)
                Flag=True
        if select==SelectArhive.RAR:
            arhivepath=f"{arhive_name}.rar"
            if os.path.exists(dir):
                listfiles=os.listdir(dir)
                with rarfile.RarFile(arhivepath, 'r') as rar_ref:
                    rar_ref.printdir()
                    # for li in listfiles:
                    #     rar_ref.add(f"{dir}\\{li}")
                    Flag=True
        return [Flag,arhivepath,dir]
    def Extract(self, arhive_name: str, dir: str, select: SelectArhive):
        """Распаковка Архива"""
        Flag,arhivepath=False,""
        if select==SelectArhive.SEVENZ:
            arhivepath=f"{arhive_name}.7z"
            if os.path.exists(arhivepath):
                with py7zr.SevenZipFile(arhivepath, "r") as archive:
                    archive.extractall(dir)
                    Flag=True
        if select==SelectArhive.ZIP:
            arhivepath=f"{arhive_name}.zip"
            if os.path.exists(arhivepath):
                with zipfile.ZipFile(arhivepath, 'r') as zip_ref:
                    zip_ref.extractall(dir)
                    Flag=True 
        if select==SelectArhive.RAR:
            arhivepath=f"{arhive_name}.rar"
            if os.path.exists(arhivepath):
                with rarfile.RarFile(arhivepath, 'r') as rar_ref:
                    rar_ref.extractall(dir)
                    Flag=True
        return [Flag,arhivepath,dir]


# arh=Arhive()
# res=arh.Extract("zerkalo","Dicts2", SelectArhive.ZIP)
# print(res[0])