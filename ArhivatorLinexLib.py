import os,sys
from enum import Enum
#---------------------
# pip install alive-progress
# pip install py7zr
# pip install zip_files - Встроеная zip_files иногда не обязательно устанавливать
# pip install rarfile
#---------------------
# apt-get install p7zip-full
# sudo apt-get install unrar-free
# sudo apt-get install zip
#---------------------

class SelectArhive(Enum):
    """Выбор Архиватора"""
    RAR=1
    """RAR Архив (Упаковка с Ошыбкой, Распаковка тоже)"""
    ZIP=2
    """ZIP Архив"""
    SEVENZ=3
    """7z Архив"""

class ArhiveLinex(object):
    """Архиваторы Linex"""
    def __init__(self):
        super(ArhiveLinex, self).__init__()
        pass
    def Pack (self, dir: str, arhive_name: str, select: SelectArhive):
        """Создание Архива"""
        Flag,arhivepath=False,""
        if select==SelectArhive.SEVENZ:
            command=f"7z a '{arhive_name}.7z' '{dir}/*'"
            os.system(command)
            Flag=True
        if select==SelectArhive.ZIP:
            command=f"zip -r -j '{arhive_name}.zip' '{dir}/'"
            os.system(command)
            Flag=True
        if select==SelectArhive.RAR:
            command=f"rar a -ep1 '{arhive_name}.rar' '{dir}/'"
            os.system(command)
            Flag=True
        return [Flag,arhivepath,dir]
    def Extract(self, arhive_name: str, dir: str, select: SelectArhive):
        """Распаковка Архива"""
        Flag,arhivepath=False,""
        if select==SelectArhive.SEVENZ:
            command=f"7z x '{arhive_name}.7z' -o'{dir}'"
            print(command)
            os.system(command)
            Flag=True
        if select==SelectArhive.ZIP:
            command=f"unzip '{arhive_name}.zip' -d '{dir}'"
            os.system(command)
            Flag=True
        if select==SelectArhive.RAR:
            command=f"unrar '{arhive_name}.rar' x '{dir}'"
            os.system(command)
            Flag=True
        return [Flag,arhivepath,dir] 