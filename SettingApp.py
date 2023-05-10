import os, sys, time, re, json, datetime, random
from os.path import basename

dir_path = os.path.dirname(os.path.realpath(__file__))

class Setting(object):
    """Настройки Приложения"""
    settingfile=f"{dir_path}/SettingApp.json"
    """Файл Настроек"""
    Version=""
    """Версия"""
    Dicts=None
    """Данные Словари"""
    SettingApp=None
    """Данные Настройки"""
    def __init__(self, encod="utf-8"):
        super(Setting, self).__init__()
        if os.path.exists(self.settingfile):
            try:
                with open(self.settingfile, 'r', encoding=encod) as f:
                    data = json.load(f)
                    self.SettingApp=data
                    self.Version = float(data['Version'])
                    filedicts=data['FileDicts']
                    fullfiledicts=f"{dir_path}/{filedicts}"
                    self.Dicts=self.ReadDicts(fullfiledicts)
            except Exception as ex:
                print(f"ERROR SETTING: {ex}!")
        else:
            print(f"ERROR: Нету {self.settingfile} Файла!")
    def Title(self):
        """Титулка"""
        title=f"title Linex v {self.Version:.3f}"
        os.system(title)
    def CreateDir(self, dir: str):
        """Создать Папку"""
        if os.path.exists(dir)==False:
            os.mkdir(dir)
    def ReadDicts(self, file: str, encod="utf-8"):
        """Чтение Словарей"""
        data=None
        if os.path.exists(file):
            try:
                with open(file, 'r', encoding=encod) as f:
                    data = json.load(f)
            except Exception as ex:
                print(f"ERROR DICTS: {ex}!")
        else:
            print(f"ERROR: Нету {file} Файла!")
        return data
    def GetGoogleLink(self, link: str):
        """Получить Прямую Ссылку на Google Link"""
        url_down=None
        if not link.strip():
            print("Ссылка Пуста!")
        else:
            repl="https://drive.google.com/file/d/"
            link=link.strip() #удаления пробелов с начала и конца строки
            id_disk=link.replace(repl,"")
            masss=id_disk.split('/')
            id_disk=masss[0]
            url_down=f"https://drive.google.com/uc?export=download&confirm=no_antivirus&id={id_disk}"
        return url_down
    def GetFileInfo(self,file: str):
        """Получить данные о файле"""
        Flag=False
        filename,file_extension="",""
        if os.path.exists(file):
            fileinfo=basename(file)
            filename, file_extension = os.path.splitext(fileinfo) 
            Flag=True
        return [Flag,filename,file,file_extension]
