import os, sys, time, re, json, datetime, random

dir_path = os.path.dirname(os.path.realpath(__file__))

class Setting(object):
    settingfile=f"{dir_path}/SettingApp.json"
    Version=""
    Dicts=None
    def __init__(self, encod="utf-8"):
        super(Setting, self).__init__()
        if os.path.exists(self.settingfile):
            try:
                with open(self.settingfile, 'r', encoding=encod) as f:
                    data = json.load(f)
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
