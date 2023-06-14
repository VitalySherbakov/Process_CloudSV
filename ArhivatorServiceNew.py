from enum import Enum
import os
from SettingService import Setting
import py7zr

dir_path = os.path.dirname(os.path.realpath(__file__))

class SelectArhive(Enum):
    """Выбор Архиватора"""
    RAR=1
    """RAR Архив (Упаковка с Ошыбкой, Распаковка тоже)"""
    ZIP=2
    """ZIP Архив"""
    SEVENZ=3
    """7z Архив"""
    TAR=4
    """TAR Архив"""

class ArhiveService(object):
    """Архиваторы Service"""
    app: Setting
    """Приложение"""
    def __init__(self):
        super(ArhiveService, self).__init__()
        self.app = Setting()
    def Pack (self, dir: str, arhive_name: str, select: SelectArhive):
        """Создание Архива"""
        Flag,arhivepath=False,""
        if select==SelectArhive.SEVENZ:
            # exearhiv=self.app.SettingApp["Arhivators"]["7z"]
            # exearhiv=f"{dir_path}/{exearhiv}"
            # os.system(f'"{exearhiv}" a "{arhive_name}.7z" "{dir}/*"')
            # Создаем объект архива
            with py7zr.SevenZipFile(f'{arhive_name}.7z', 'w') as archive:
                # Добавляем файлы в архив
                archive.writeall(dir)
            Flag=True
        if select==SelectArhive.ZIP:
            exearhiv=self.app.SettingApp["Arhivators"]["ZIP"]
            exearhiv=f"{dir_path}/{exearhiv}"
            os.system(f'"{exearhiv}" -r -j "{arhive_name}.zip" "{dir}/"')
            Flag=True
        if select==SelectArhive.RAR:
            exearhiv=self.app.SettingApp["Arhivators"]["RAR"]
            exearhiv=f"{dir_path}/{exearhiv}"
            os.system(f'"{exearhiv}" a -ep1 "{arhive_name}.rar" "{dir}/"')
            Flag=True
        return [Flag,arhivepath,dir]
    def Extract(self, arhive_name: str, dir: str, select: SelectArhive):
        """Распаковка Архива"""
        Flag,arhivepath=False,""
        if select==SelectArhive.SEVENZ:
            # exearhiv=self.app.SettingApp["Arhivators"]["7z"]
            # exearhiv=f"{dir_path}/{exearhiv}"
            # os.system(f'"{exearhiv}" x "{arhive_name}.7z" -o "{dir}"')
            with py7zr.SevenZipFile(f"{arhive_name}.7z", mode='r') as archive:
                archive.extractall(dir)
            Flag=True
        if select==SelectArhive.ZIP:
            exearhiv=self.app.SettingApp["Arhivators"]["ZIP"]
            exearhiv=f"{dir_path}/{exearhiv}"
            os.system(f'"{exearhiv}" "{arhive_name}.zip" -d "{dir}"')
            Flag=True
        if select==SelectArhive.RAR:
            exearhiv=self.app.SettingApp["Arhivators"]["RAR"]
            exearhiv=f"{dir_path}/{exearhiv}"
            os.system(f'"{exearhiv}" "{arhive_name}.rar" x "{dir}"')
            Flag=True
        return [Flag,arhivepath,dir]
    def ExtractFull(self, arhive_full: str, dir: str, select: SelectArhive):
        """Распаковка Архива"""
        Flag,arhivepath=False,""
        if select==SelectArhive.TAR:
            command=f'tar -xvf "{arhive_full}" -C "{dir}"'
            #print(command)
            os.system(command)
            Flag=True
        if select==SelectArhive.SEVENZ:
            # exearhiv=self.app.SettingApp["Arhivators"]["7z"]
            # exearhiv=f"{dir_path}/{exearhiv}"
            # os.system(f'"{exearhiv}" x "{arhive_name}.7z" -o "{dir}"')
            with py7zr.SevenZipFile(arhive_full, mode='r') as archive:
                archive.extractall(dir)
            Flag=True
        if select==SelectArhive.ZIP:
            exearhiv=self.app.SettingApp["Arhivators"]["ZIP"]
            exearhiv=f"{dir_path}/{exearhiv}"
            os.system(f'"{exearhiv}" "{arhive_full}" -d "{dir}"')
            Flag=True
        if select==SelectArhive.RAR:
            exearhiv=self.app.SettingApp["Arhivators"]["RAR"]
            exearhiv=f"{dir_path}/{exearhiv}"
            os.system(f'"{exearhiv}" "{arhive_full}" x "{dir}"')
            Flag=True
        return [Flag,arhivepath,dir]