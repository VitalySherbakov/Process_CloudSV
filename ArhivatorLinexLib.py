import os,sys
from enum import Enum
#---------------------
# pip install alive-progress
# pip install py7zr
# pip install zip_files - Встроеная zip_files иногда не обязательно устанавливать
# pip install rarfile
#---------------------
# apt-get install p7zip-full
# sudo apt-get install rar
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
            os.system(f"7z a '{arhive_name}.7z' '{dir}/*'")
            Flag=True
        if select==SelectArhive.ZIP:
            os.system(f"zip -r -j '{arhive_name}.zip' '{dir}/'")
            Flag=True
        if select==SelectArhive.RAR:
            os.system(f"rar a -ep1 '{arhive_name}.rar' '{dir}/'")
            Flag=True
        return [Flag,arhivepath,dir]
    def Extract(self, arhive_name: str, dir: str, select: SelectArhive):
        """Распаковка Архива"""
        Flag,arhivepath=False,""
        if select==SelectArhive.SEVENZ:
            os.system(f"7z x '{arhive_name}.7z' -o '{dir}'")
            Flag=True
        if select==SelectArhive.ZIP:
            os.system(f"unzip '{arhive_name}.zip' -d '{dir}'")
            Flag=True
        if select==SelectArhive.RAR:
            os.system(f"unrar '{arhive_name}.rar' x '{dir}'")
            Flag=True
        return [Flag,arhivepath,dir] 