import os, sys, time, re, json, datetime, random

dir_path = os.path.dirname(os.path.realpath(__file__))

class Setting(object):
    settingfile=f"{dir_path}/SettingApp.json"
    Version=""
    def __init__(self, encod="utf-8"):
        super(Setting, self).__init__()
        if os.path.exists(self.settingfile):
            try:
                with open(self.settingfile, 'r', encoding=encod) as f:
                    data = json.load(f)
                    #self.Version = float(data['Version'])
                    #os.system(f"title Linex (v {self.Version:.f3})")
            except Exception as ex:
                print(f"ERROR SETTING: {ex}!")
        else:
            print(f"ERROR: Нету {self.settingfile} Файла!")

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
