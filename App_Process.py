import os, sys, time, re, json, datetime, random
import requests
from alive_progress import alive_bar
from alive_progress.styles import showtime
from os.path import basename
from SettingApp import Setting

dir_path = os.path.dirname(os.path.realpath(__file__))

class AppProcessLinex(object):
    """Процесс Общий"""
    app=None
    def __init__(self):
        super(AppProcessLinex, self).__init__()
        self.app = Setting()
    def DownLoad_Dicts_All(self):
        """Загрузка Всех Словарей"""
        setting=self.app.SettingApp["Prioritet"]
        prioritet=self.app.SettingApp["PrioritetDown"]
        if prioritet["GoogleLink"]==1:
            if setting["7z"]==1 and setting["ZIP"]==2 and setting["RAR"]==3:
                self.__GoogleLinks_Full_Downloads("7z", "ZIP", "RAR")
            if setting["7z"]==1 and setting["ZIP"]==3 and setting["RAR"]==2:
                self.__GoogleLinks_Full_Downloads("7z", "RAR", "ZIP")
            #--------------------------------------------------------------
            if setting["ZIP"]==1 and setting["7z"]==2 and setting["RAR"]==3:
                self.__GoogleLinks_Full_Downloads("ZIP", "7z", "RAR")
            if setting["ZIP"]==1 and setting["7z"]==3 and setting["RAR"]==2:
                self.__GoogleLinks_Full_Downloads("ZIP", "RAR", "7z")
            #--------------------------------------------------------------
            if setting["RAR"]==1 and setting["7z"]==2 and setting["ZIP"]==3:
                self.__GoogleLinks_Full_Downloads("RAR", "7z", "ZIP")
            if setting["RAR"]==1 and setting["7z"]==3 and setting["ZIP"]==2:
                self.__GoogleLinks_Full_Downloads("RAR", "ZIP", "7z")
        if prioritet["Directlink"]==1:
            if setting["7z"]==1 and setting["ZIP"]==2 and setting["RAR"]==3:
                self.__DirectLinks_Full_Downloads("7z", "ZIP", "RAR")
            if setting["7z"]==1 and setting["ZIP"]==3 and setting["RAR"]==2:
                self.__DirectLinks_Full_Downloads("7z", "RAR", "ZIP")
            #--------------------------------------------------------------
            if setting["ZIP"]==1 and setting["7z"]==2 and setting["RAR"]==3:
                self.__DirectLinks_Full_Downloads("ZIP", "7z", "RAR")
            if setting["ZIP"]==1 and setting["7z"]==3 and setting["RAR"]==2:
                self.__DirectLinks_Full_Downloads("ZIP", "RAR", "7z")
            #--------------------------------------------------------------
            if setting["RAR"]==1 and setting["7z"]==2 and setting["ZIP"]==3:
                self.__DirectLinks_Full_Downloads("RAR", "7z", "ZIP")
            if setting["RAR"]==1 and setting["7z"]==3 and setting["ZIP"]==2:
                self.__DirectLinks_Full_Downloads("RAR", "ZIP", "7z")
    def DownLoad_Dicts_Pack(self, pack: int):
        """Загрузка Пачки"""
        setting=self.app.SettingApp["Prioritet"]
        prioritet=self.app.SettingApp["PrioritetDown"]
        if prioritet["GoogleLink"]==1:
            if setting["7z"]==1 and setting["ZIP"]==2 and setting["RAR"]==3:
                self.__GoogleLinks_Pack_Downloads(pack,"7z", "ZIP", "RAR")
            if setting["7z"]==1 and setting["ZIP"]==3 and setting["RAR"]==2:
                self.__GoogleLinks_Pack_Downloads(pack,"7z", "RAR", "ZIP")
            #--------------------------------------------------------------
            if setting["ZIP"]==1 and setting["7z"]==2 and setting["RAR"]==3:
                self.__GoogleLinks_Pack_Downloads(pack,"ZIP", "7z", "RAR")
            if setting["ZIP"]==1 and setting["7z"]==3 and setting["RAR"]==2:
                self.__GoogleLinks_Pack_Downloads(pack,"ZIP", "RAR", "7z")
            #--------------------------------------------------------------
            if setting["RAR"]==1 and setting["7z"]==2 and setting["ZIP"]==3:
                self.__GoogleLinks_Pack_Downloads(pack,"RAR", "7z", "ZIP")
            if setting["RAR"]==1 and setting["7z"]==3 and setting["ZIP"]==2:
                self.__GoogleLinks_Pack_Downloads(pack,"RAR", "ZIP", "7z")
        if prioritet["Directlink"]==1:
            if setting["7z"]==1 and setting["ZIP"]==2 and setting["RAR"]==3:
                self.__DirectLinks_Pack_Downloads(pack,"7z", "ZIP", "RAR")
            if setting["7z"]==1 and setting["ZIP"]==3 and setting["RAR"]==2:
                self.__DirectLinks_Pack_Downloads(pack,"7z", "RAR", "ZIP")
            #--------------------------------------------------------------
            if setting["ZIP"]==1 and setting["7z"]==2 and setting["RAR"]==3:
                self.__DirectLinks_Pack_Downloads(pack,"ZIP", "7z", "RAR")
            if setting["ZIP"]==1 and setting["7z"]==3 and setting["RAR"]==2:
                self.__DirectLinks_Pack_Downloads(pack,"ZIP", "RAR", "7z")
            #--------------------------------------------------------------
            if setting["RAR"]==1 and setting["7z"]==2 and setting["ZIP"]==3:
                self.__DirectLinks_Pack_Downloads(pack,"RAR", "7z", "ZIP")
            if setting["RAR"]==1 and setting["7z"]==3 and setting["ZIP"]==2:
                self.__DirectLinks_Pack_Downloads(pack,"RAR", "ZIP", "7z")
    def DownLoad_Dicts_One(self, name: str):
        """Загрузка Один"""
        setting=self.app.SettingApp["Prioritet"]
        prioritet=self.app.SettingApp["PrioritetDown"]
        if prioritet["GoogleLink"]==1:
            if setting["7z"]==1 and setting["ZIP"]==2 and setting["RAR"]==3:
                self.__GoogleLinks_One_Downloads(name,"7z", "ZIP", "RAR")
            if setting["7z"]==1 and setting["ZIP"]==3 and setting["RAR"]==2:
                self.__GoogleLinks_One_Downloads(name,"7z", "RAR", "ZIP")
            #--------------------------------------------------------------
            if setting["ZIP"]==1 and setting["7z"]==2 and setting["RAR"]==3:
                self.__GoogleLinks_One_Downloads(name,"ZIP", "7z", "RAR")
            if setting["ZIP"]==1 and setting["7z"]==3 and setting["RAR"]==2:
                self.__GoogleLinks_One_Downloads(name,"ZIP", "RAR", "7z")
            #--------------------------------------------------------------
            if setting["RAR"]==1 and setting["7z"]==2 and setting["ZIP"]==3:
                self.__GoogleLinks_One_Downloads(name,"RAR", "7z", "ZIP")
            if setting["RAR"]==1 and setting["7z"]==3 and setting["ZIP"]==2:
                self.__GoogleLinks_One_Downloads(name,"RAR", "ZIP", "7z")
        if prioritet["Directlink"]==1:
            if setting["7z"]==1 and setting["ZIP"]==2 and setting["RAR"]==3:
                self.__DirectLinks_One_Downloads(name,"7z", "ZIP", "RAR")
            if setting["7z"]==1 and setting["ZIP"]==3 and setting["RAR"]==2:
                self.__DirectLinks_One_Downloads(name,"7z", "RAR", "ZIP")
            #--------------------------------------------------------------
            if setting["ZIP"]==1 and setting["7z"]==2 and setting["RAR"]==3:
                self.__DirectLinks_One_Downloads(name,"ZIP", "7z", "RAR")
            if setting["ZIP"]==1 and setting["7z"]==3 and setting["RAR"]==2:
                self.__DirectLinks_One_Downloads(name,"ZIP", "RAR", "7z")
            #--------------------------------------------------------------
            if setting["RAR"]==1 and setting["7z"]==2 and setting["ZIP"]==3:
                self.__DirectLinks_One_Downloads(name,"RAR", "7z", "ZIP")
            if setting["RAR"]==1 and setting["7z"]==3 and setting["ZIP"]==2:
                self.__DirectLinks_One_Downloads(name,"RAR", "ZIP", "7z")
    def __GoogleLinks_Full_Downloads(self, keyarhiv: str, keyarhiv2: str, keyarhiv3: str):
        """Скачивание Словарей"""
        dictformats={"ZIP": "zip", "RAR": "rar", "7z": "7z"}
        for li in self.app.Dicts:
            urldown=li["Urls"][keyarhiv]
            urldirect=self.app.GetGoogleLink(urldown)
            filepath=f"{dir_path}\\{self.app.SettingApp['FolderDicts']['ArhivesDown']}\\{li['Name']}.{dictformats[keyarhiv]}"
            dirpath=f"{dir_path}\\{self.app.SettingApp['FolderDicts']['ArhivesDown']}"
            self.app.CreateDir(dirpath)
            res=self.app.DownloadFile(urldirect, filepath)
            if res==False:
                urldown2=li["Urls"][keyarhiv2]
                urldirect2=self.app.GetGoogleLink(urldown2)
                res2=self.app.DownloadFile(urldirect2, filepath)
                if res2==False:
                    urldown3=li["Urls"][keyarhiv3]
                    urldirect3=self.app.GetGoogleLink(urldown3)
                    res3=self.app.DownloadFile(urldirect3, filepath)
                    if res3==False:
                        print(f"{li['Name']} Нету Словаря Вообще на Скачивание!")
    def __GoogleLinks_Pack_Downloads(self,pack: int, keyarhiv: str, keyarhiv2: str, keyarhiv3: str):
        """Пачка Скачивание Словарей"""
        dictformats={"ZIP": "zip", "RAR": "rar", "7z": "7z"}
        names=[]
        if pack==1:
            names=self.app.SettingApp["ArhivesPack1"]
        if pack==2:
            names=self.app.SettingApp["ArhivesPack2"]
        if pack==3:
            names=self.app.SettingApp["ArhivesPack3"]
        for li in self.app.Dicts:
            if li["Name"] in names:
                urldown=li["Urls"][keyarhiv]
                urldirect=self.app.GetGoogleLink(urldown)
                filepath=f"{dir_path}\\{self.app.SettingApp['FolderDicts']['ArhivesDown']}\\{li['Name']}.{dictformats[keyarhiv]}"
                dirpath=f"{dir_path}\\{self.app.SettingApp['FolderDicts']['ArhivesDown']}"
                self.app.CreateDir(dirpath)
                res=self.app.DownloadFile(urldirect, filepath)
                if res==False:
                    urldown2=li["Urls"][keyarhiv2]
                    urldirect2=self.app.GetGoogleLink(urldown2)
                    res2=self.app.DownloadFile(urldirect2, filepath)
                    if res2==False:
                        urldown3=li["Urls"][keyarhiv3]
                        urldirect3=self.app.GetGoogleLink(urldown3)
                        res3=self.app.DownloadFile(urldirect3, filepath)
                        if res3==False:
                            print(f"{li['Name']} Нету Словаря Вообще на Скачивание!")
    def __GoogleLinks_One_Downloads(self,name: str, keyarhiv: str, keyarhiv2: str, keyarhiv3: str):
        """Один Скачивание Словарей"""
        dictformats={"ZIP": "zip", "RAR": "rar", "7z": "7z"}
        for li in self.app.Dicts:
            if li["Name"]==name:
                urldown=li["Urls"][keyarhiv]
                urldirect=self.app.GetGoogleLink(urldown)
                filepath=f"{dir_path}\\{self.app.SettingApp['FolderDicts']['ArhivesDown']}\\{li['Name']}.{dictformats[keyarhiv]}"
                dirpath=f"{dir_path}\\{self.app.SettingApp['FolderDicts']['ArhivesDown']}"
                self.app.CreateDir(dirpath)
                res=self.app.DownloadFile(urldirect, filepath)
                if res==False:
                    urldown2=li["Urls"][keyarhiv2]
                    urldirect2=self.app.GetGoogleLink(urldown2)
                    res2=self.app.DownloadFile(urldirect2, filepath)
                    if res2==False:
                        urldown3=li["Urls"][keyarhiv3]
                        urldirect3=self.app.GetGoogleLink(urldown3)
                        res3=self.app.DownloadFile(urldirect3, filepath)
                        if res3==False:
                            print(f"{li['Name']} Нету Словаря Вообще на Скачивание!")
    def __DirectLinks_Full_Downloads(self, keyarhiv: str, keyarhiv2: str, keyarhiv3: str):
        """Скачивание Словарей"""
        dictformats={"ZIP": "zip", "RAR": "rar", "7z": "7z"}
        for li in self.app.Dicts:
            urldown=li["Urls"][keyarhiv]
            urldirect=self.app.GetGoogleLink(urldown)
            filepath=f"{dir_path}\\{self.app.SettingApp['FolderDicts']['ArhivesDown']}\\{li['Name']}.{dictformats[keyarhiv]}"
            dirpath=f"{dir_path}\\{self.app.SettingApp['FolderDicts']['ArhivesDown']}"
            self.app.CreateDir(dirpath)
            res=self.app.DownloadFile(urldirect, filepath)
            if res==False:
                urldown2=li["Urls"][keyarhiv2]
                urldirect2=self.app.GetGoogleLink(urldown2)
                res2=self.app.DownloadFile(urldirect2, filepath)
                if res2==False:
                    urldown3=li["Urls"][keyarhiv3]
                    res3=self.app.DownloadFile(urldown3, filepath)
                    if res3==False:
                        print(f"{li['Name']} Нету Словаря Вообще на Скачивание!")
    def __DirectLinks_Pack_Downloads(self,pack: int, keyarhiv: str, keyarhiv2: str, keyarhiv3: str):
        """Пачка Скачивание Словарей"""
        dictformats={"ZIP": "zip", "RAR": "rar", "7z": "7z"}
        names=[]
        if pack==1:
            names=self.app.SettingApp["ArhivesPack1"]
        if pack==2:
            names=self.app.SettingApp["ArhivesPack2"]
        if pack==3:
            names=self.app.SettingApp["ArhivesPack3"]
        for li in self.app.Dicts:
            if li in names:
                urldown=li["Urls"][keyarhiv]
                urldirect=self.app.GetGoogleLink(urldown)
                filepath=f"{dir_path}\\{self.app.SettingApp['FolderDicts']['ArhivesDown']}\\{li['Name']}.{dictformats[keyarhiv]}"
                dirpath=f"{dir_path}\\{self.app.SettingApp['FolderDicts']['ArhivesDown']}"
                self.app.CreateDir(dirpath)
                res=self.app.DownloadFile(urldirect, filepath)
                if res==False:
                    urldown2=li["Urls"][keyarhiv2]
                    res2=self.app.DownloadFile(urldown2, filepath)
                    if res2==False:
                        urldown3=li["Urls"][keyarhiv3]
                        urldirect3=self.app.GetGoogleLink(urldown3)
                        res3=self.app.DownloadFile(urldirect3, filepath)
                        if res3==False:
                            print(f"{li['Name']} Нету Словаря Вообще на Скачивание!")
    def __DirectLinks_One_Downloads(self,name: str, keyarhiv: str, keyarhiv2: str, keyarhiv3: str):
        """Один Скачивание Словарей"""
        dictformats={"ZIP": "zip", "RAR": "rar", "7z": "7z"}
        for li in self.app.Dicts:
            if li["Name"]==name:
                urldown=li["Urls"][keyarhiv]
                urldirect=self.app.GetGoogleLink(urldown)
                filepath=f"{dir_path}\\{self.app.SettingApp['FolderDicts']['ArhivesDown']}\\{li['Name']}.{dictformats[keyarhiv]}"
                dirpath=f"{dir_path}\\{self.app.SettingApp['FolderDicts']['ArhivesDown']}"
                self.app.CreateDir(dirpath)
                res=self.app.DownloadFile(urldirect, filepath)
                if res==False:
                    urldown2=li["Urls"][keyarhiv2]
                    res2=self.app.DownloadFile(urldown2, filepath)
                    if res2==False:
                        urldown3=li["Urls"][keyarhiv3]
                        urldirect3=self.app.GetGoogleLink(urldown3)
                        res3=self.app.DownloadFile(urldirect3, filepath)
                        if res3==False:
                            print(f"{li['Name']} Нету Словаря Вообще на Скачивание!")


app=AppProcessLinex()
app.DownLoad_Dicts_Pack(3)