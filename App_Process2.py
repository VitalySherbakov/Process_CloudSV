import os, sys, time, re, json, datetime, random
# import requests
# from alive_progress import alive_bar
# from alive_progress.styles import showtime
from os.path import basename
from SettingService import Setting
#from ArhivatorLib import Arhive, SelectArhive
#from ArhivatorLinexLib import ArhiveLinex, SelectArhive
from ArhivatorServiceNew import ArhiveService, SelectArhive
from enum import Enum

dir_path = os.path.dirname(os.path.realpath(__file__))

class SelectProgram(Enum):
    """Выбор Програмы CPU/GPU"""
    CPU=1
    """CPU Программа -> aircrack-ng"""
    GPU=2
    """GPU Программа -> hashcat"""
class SelectPlatform(Enum):
    """Выбор Платформы"""
    NONE=0
    """Пусто"""
    Debian=1
    """Debian"""
    Ubuntu=2
    """Ubuntu"""

class AppProcessLinex(object):
    """Процесс Общий"""
    app=None
    """Приложение"""
    #arh: Arhive
    arh: ArhiveService
    """Архиватор"""
    platform: SelectProgram
    """Платформа"""
    def __init__(self, platform_name: str):
        super(AppProcessLinex, self).__init__()
        self.app = Setting()
        #self.arh=Arhive()
        self.arh=ArhiveService()
        self.platform=self.GetPlatform(platform_name)
    def GetCommand(self, program: SelectProgram):
        """Команды Запуска Прогамы"""
        if program==SelectProgram.CPU:
            dir=self.app.SettingApp["Urls_GPU_CPU_Full"][1]["Dir"]
            file=self.app.SettingApp["Urls_GPU_CPU_Full"][1]["Run"]
            runfile=f"{dir_path}/{dir}/{file}"
            rundir=f"{dir_path}/{dir}"
        if program==SelectProgram.GPU:
            dir=self.app.SettingApp["Urls_GPU_CPU_Full"][0]["Dir"]
            file=self.app.SettingApp["Urls_GPU_CPU_Full"][0]["Run"]
            runfile=f"{dir_path}/{dir}/{file}"
            rundir=f"{dir_path}/{dir}"
        return [file, runfile, rundir]
    def Access_Folder_Linex(self, folder: str, selectplatform:  SelectPlatform):
        """Дать Полный Доступ к Папке и ей Подкоталогов"""
        Flag=False
        #----------------Доступ-----------------
        if selectplatform==SelectPlatform.Debian:
            os.system(f"chmod -R +x {folder}/*")
            os.system(f'chmod -R 777 "{folder}"')
            Flag=True
        if selectplatform==SelectPlatform.Ubuntu:
            os.system(f"chmod -R +x {folder}/*")
            os.system(f'chmod -R 777 "{folder}"')
            Flag=True
        if selectplatform==SelectPlatform.NONE:
            os.system(f"chmod -R +x {folder}/*")
            os.system(f'chmod -R 777 "{folder}"')
            Flag=True
        #---------------------------------------
        return Flag
    def GetPlatform(self, platform_name: str):
        """Получить Платформу"""
        select=SelectPlatform.NONE
        if platform_name=="Debian":
            select=SelectPlatform.Debian
        if platform_name=="Ubuntu":
            select=SelectPlatform.Ubuntu
        return select
    def GetNamesDicts(self):
        """Список Имен Словарей"""
        listing=[]
        for li in self.app.Dicts:
            listing.append(li["Name"])
        return listing
    def GetFilesFindDict(self, name: str):
        """Найти Список Файлов Словарей под Именем"""
        listing=[]
        for li in self.app.Dicts:
            if li["Name"]==name:
                listing=li["Files"]
        return listing
    def GetFilesPackDict(self, number: int, arhiv1: list, arhiv2: list, arhiv3: list):
        """Найти Список Файлов Словарей под Пачкай"""
        listing,packslist=[],[]
        if number==1:
            #packslist=self.app.SettingApp["ArhivesPack1"]
            packslist=arhiv1
        if number==2:
            #packslist=self.app.SettingApp["ArhivesPack2"]
            packslist=arhiv2
        if number==3:
            #packslist=self.app.SettingApp["ArhivesPack3"]
            packslist=arhiv3
        for name in packslist:
            res=[val for val in self.app.Dicts if val['Name']==name]
            for li in res:
                for file in li["Files"]:
                    if (file in listing)==False:
                        listing.append(file)
        return listing
    def GetFilesAllDict(self):
        """Список Файлов Словарей Все"""
        listing=[]
        for li in self.app.Dicts:
            for li2 in li["Files"]:
                if (li2 in listing)==False: #убирающий повторения
                    listing.append(li2)
    def Download_ProgramNew(self, select: SelectProgram):
        """Загрузка Програмы CPU/GPU"""
        Flag=False
        url,dirpath,file="","",""
        if select==SelectProgram.GPU:
            url=self.app.SettingApp["Urls_GPU_CPU_Full"][0]["GPU"]
            dirpath=self.app.SettingApp["Urls_GPU_CPU_Full"][0]["Dir"]
            file=self.app.SettingApp["Urls_GPU_CPU_Full"][0]["File"]
        if select==SelectProgram.CPU:
            url=self.app.SettingApp["Urls_GPU_CPU_Full"][1]["CPU"]
            dirpath=self.app.SettingApp["Urls_GPU_CPU_Full"][1]["Dir"]
            file=self.app.SettingApp["Urls_GPU_CPU_Full"][1]["File"]
        downprogram=f"{dir_path}/{file}" #загрузка програмы
        dirextract=f"{dir_path}/{dirpath}" #распаковка
        Flag=self.app.DownloadFile(url,downprogram)
        if Flag:
            self.__ExtractArhive(downprogram,dirextract)
            if os.path.exists(downprogram): #Удаляем Архив
                os.remove(downprogram)
        return [Flag]
    def DownLoad_Program(self, select: SelectProgram):
        """Загрузка Програмы CPU/GPU"""
        Flag=False
        url,dirpath,file="","",""
        if select==SelectProgram.GPU:
            url=self.app.SettingApp["Urls_GPU_CPU_Full"][0]["GPU"]
            dirpath=self.app.SettingApp["Urls_GPU_CPU_Full"][0]["Dir"]
            file=self.app.SettingApp["Urls_GPU_CPU_Full"][0]["File"]
        if select==SelectProgram.CPU:
            url=self.app.SettingApp["Urls_GPU_CPU_Full"][1]["CPU"]
            dirpath=self.app.SettingApp["Urls_GPU_CPU_Full"][1]["Dir"]
            file=self.app.SettingApp["Urls_GPU_CPU_Full"][1]["File"]
        downprogram=f"{dir_path}/{file}" #загрузка програмы
        dirextract=f"{dir_path}/{dirpath}" #распаковка
        #print(f"Файл: {downprogram}")
        #print(f"Распаковка: {dirextract}")
        res=self.__DownLoadGoogleLink(url, downprogram)
        Flag=res[0]
        if Flag:
            res2=self.app.GetFileInfo(downprogram)
            if res2[0]:
                filename=f"{dir_path}/{res2[1]}"
                #print(f"Имя2: {filename}")
                self.__ExtractArhiveKey("7z",filename,dirextract)
                self.Access_Folder_Linex(dirextract, self.platform)
            else:
                print(f"Программа2 {file} не Загружена!")
        else:
            Flag=self.__DownLoadDirect(url, downprogram)
            res2=self.app.GetFileInfo(downprogram)
            if res2[0]:
                filename=f"{dir_path}/{res2[1]}"
                #print(f"Имя: {filename}")
                self.__ExtractArhiveKey("7z",filename,dirextract)
                self.Access_Folder_Linex(dirextract, self.platform)
        return Flag
    def DownLoad_HC22000(self, url: str, file: str):
        """Загрузка hc22000"""
        Flag=False
        dirpath=self.app.SettingApp["FolderHC22000_Cap"]
        self.__CreateFolder(f"{dir_path}/{dirpath}")
        res=self.__DownLoadGoogleLink(url, f"{dir_path}/{dirpath}/{file}")
        Flag=res[0]
        if res[0]==False:
            Flag=self.__DownLoadDirect(url, f"{dir_path}/{dirpath}/{file}")
        return [Flag,f"{dir_path}/{dirpath}/{file}"]
    def DownLoad_HC220002(self, url: str, file: str):
        """Загрузка hc22000"""
        Flag=False
        dirpath=self.app.SettingApp["FolderHC22000_Cap"]
        self.__CreateFolder(f"{dir_path}/{dirpath}")
        #res=self.__DownLoadGoogleLink(url, f"{dir_path}/{dirpath}/{file}")
        #Flag=self.__DownLoadDirect(url, f"{dir_path}/{dirpath}/{file}")
        Flag=self.app.DownloadFile2(url,f"{dir_path}/{dirpath}/{file}")
        return [Flag,f"{dir_path}/{dirpath}/{file}"]
    def Get_HC22000_Files(self):
        """Получить Спысок Файлив"""
        listfiles=[]
        dirpath=self.app.SettingApp["FolderHC22000_Cap"]
        self.__CreateFolder(f"{dir_path}/{dirpath}")
        files=os.listdir(f"{dir_path}/{dirpath}")
        for i,li in enumerate(files):
            #print(f"{i}) {li}")
            listfiles.append({"Number": i, "File": li})
        return listfiles
    def DownLoad_Dicts_All(self):
        """Загрузка Всех Словарей"""
        resultdown=False
        setting=self.app.SettingApp["Prioritet"]
        prioritet=self.app.SettingApp["PrioritetDown"]
        if prioritet["GoogleLink"]==1:
            if setting["7z"]==1 and setting["ZIP"]==2 and setting["RAR"]==3:
                resultdown=self.__GoogleLinks_Full_Downloads("7z", "ZIP", "RAR")
            if setting["7z"]==1 and setting["ZIP"]==3 and setting["RAR"]==2:
                resultdown=self.__GoogleLinks_Full_Downloads("7z", "RAR", "ZIP")
            #--------------------------------------------------------------
            if setting["ZIP"]==1 and setting["7z"]==2 and setting["RAR"]==3:
                resultdown=self.__GoogleLinks_Full_Downloads("ZIP", "7z", "RAR")
            if setting["ZIP"]==1 and setting["7z"]==3 and setting["RAR"]==2:
                resultdown=self.__GoogleLinks_Full_Downloads("ZIP", "RAR", "7z")
            #--------------------------------------------------------------
            if setting["RAR"]==1 and setting["7z"]==2 and setting["ZIP"]==3:
                resultdown=self.__GoogleLinks_Full_Downloads("RAR", "7z", "ZIP")
            if setting["RAR"]==1 and setting["7z"]==3 and setting["ZIP"]==2:
                resultdown=self.__GoogleLinks_Full_Downloads("RAR", "ZIP", "7z")
        if prioritet["Directlink"]==1:
            if setting["7z"]==1 and setting["ZIP"]==2 and setting["RAR"]==3:
                resultdown=self.__DirectLinks_Full_Downloads("7z", "ZIP", "RAR")
            if setting["7z"]==1 and setting["ZIP"]==3 and setting["RAR"]==2:
                resultdown=self.__DirectLinks_Full_Downloads("7z", "RAR", "ZIP")
            #--------------------------------------------------------------
            if setting["ZIP"]==1 and setting["7z"]==2 and setting["RAR"]==3:
                resultdown=self.__DirectLinks_Full_Downloads("ZIP", "7z", "RAR")
            if setting["ZIP"]==1 and setting["7z"]==3 and setting["RAR"]==2:
                resultdown=self.__DirectLinks_Full_Downloads("ZIP", "RAR", "7z")
            #--------------------------------------------------------------
            if setting["RAR"]==1 and setting["7z"]==2 and setting["ZIP"]==3:
                resultdown=self.__DirectLinks_Full_Downloads("RAR", "7z", "ZIP")
            if setting["RAR"]==1 and setting["7z"]==3 and setting["ZIP"]==2:
                resultdown=self.__DirectLinks_Full_Downloads("RAR", "ZIP", "7z")
        return resultdown
    def DownLoad_Dicts_Pack(self, pack: int):
        """Загрузка Пачки"""
        resultdown=False
        setting=self.app.SettingApp["Prioritet"]
        prioritet=self.app.SettingApp["PrioritetDown"]
        if prioritet["GoogleLink"]==1:
            if setting["7z"]==1 and setting["ZIP"]==2 and setting["RAR"]==3:
                resultdown=self.__GoogleLinks_Pack_Downloads(pack,"7z", "ZIP", "RAR")
            if setting["7z"]==1 and setting["ZIP"]==3 and setting["RAR"]==2:
                resultdown=self.__GoogleLinks_Pack_Downloads(pack,"7z", "RAR", "ZIP")
            #--------------------------------------------------------------
            if setting["ZIP"]==1 and setting["7z"]==2 and setting["RAR"]==3:
                resultdown=self.__GoogleLinks_Pack_Downloads(pack,"ZIP", "7z", "RAR")
            if setting["ZIP"]==1 and setting["7z"]==3 and setting["RAR"]==2:
                resultdown=self.__GoogleLinks_Pack_Downloads(pack,"ZIP", "RAR", "7z")
            #--------------------------------------------------------------
            if setting["RAR"]==1 and setting["7z"]==2 and setting["ZIP"]==3:
                resultdown=self.__GoogleLinks_Pack_Downloads(pack,"RAR", "7z", "ZIP")
            if setting["RAR"]==1 and setting["7z"]==3 and setting["ZIP"]==2:
                resultdown=self.__GoogleLinks_Pack_Downloads(pack,"RAR", "ZIP", "7z")
        if prioritet["Directlink"]==1:
            if setting["7z"]==1 and setting["ZIP"]==2 and setting["RAR"]==3:
                resultdown=self.__DirectLinks_Pack_Downloads(pack,"7z", "ZIP", "RAR")
            if setting["7z"]==1 and setting["ZIP"]==3 and setting["RAR"]==2:
                resultdown=self.__DirectLinks_Pack_Downloads(pack,"7z", "RAR", "ZIP")
            #--------------------------------------------------------------
            if setting["ZIP"]==1 and setting["7z"]==2 and setting["RAR"]==3:
                resultdown=self.__DirectLinks_Pack_Downloads(pack,"ZIP", "7z", "RAR")
            if setting["ZIP"]==1 and setting["7z"]==3 and setting["RAR"]==2:
                resultdown=self.__DirectLinks_Pack_Downloads(pack,"ZIP", "RAR", "7z")
            #--------------------------------------------------------------
            if setting["RAR"]==1 and setting["7z"]==2 and setting["ZIP"]==3:
                resultdown=self.__DirectLinks_Pack_Downloads(pack,"RAR", "7z", "ZIP")
            if setting["RAR"]==1 and setting["7z"]==3 and setting["ZIP"]==2:
                resultdown=self.__DirectLinks_Pack_Downloads(pack,"RAR", "ZIP", "7z")
        return resultdown
    def DownLoad_Dicts_One(self, name: str):
        """Загрузка Один"""
        resultdown=False
        setting=self.app.SettingApp["Prioritet"]
        prioritet=self.app.SettingApp["PrioritetDown"]
        if prioritet["GoogleLink"]==1:
            if setting["7z"]==1 and setting["ZIP"]==2 and setting["RAR"]==3:
                resultdown=self.__GoogleLinks_One_Downloads(name,"7z", "ZIP", "RAR")
            if setting["7z"]==1 and setting["ZIP"]==3 and setting["RAR"]==2:
                resultdown=self.__GoogleLinks_One_Downloads(name,"7z", "RAR", "ZIP")
            #--------------------------------------------------------------
            if setting["ZIP"]==1 and setting["7z"]==2 and setting["RAR"]==3:
                resultdown=self.__GoogleLinks_One_Downloads(name,"ZIP", "7z", "RAR")
            if setting["ZIP"]==1 and setting["7z"]==3 and setting["RAR"]==2:
                resultdown=self.__GoogleLinks_One_Downloads(name,"ZIP", "RAR", "7z")
            #--------------------------------------------------------------
            if setting["RAR"]==1 and setting["7z"]==2 and setting["ZIP"]==3:
                resultdown=self.__GoogleLinks_One_Downloads(name,"RAR", "7z", "ZIP")
            if setting["RAR"]==1 and setting["7z"]==3 and setting["ZIP"]==2:
                resultdown=self.__GoogleLinks_One_Downloads(name,"RAR", "ZIP", "7z")
        if prioritet["Directlink"]==1:
            if setting["7z"]==1 and setting["ZIP"]==2 and setting["RAR"]==3:
                resultdown=self.__DirectLinks_One_Downloads(name,"7z", "ZIP", "RAR")
            if setting["7z"]==1 and setting["ZIP"]==3 and setting["RAR"]==2:
                resultdown=self.__DirectLinks_One_Downloads(name,"7z", "RAR", "ZIP")
            #--------------------------------------------------------------
            if setting["ZIP"]==1 and setting["7z"]==2 and setting["RAR"]==3:
                resultdown=self.__DirectLinks_One_Downloads(name,"ZIP", "7z", "RAR")
            if setting["ZIP"]==1 and setting["7z"]==3 and setting["RAR"]==2:
                resultdown=self.__DirectLinks_One_Downloads(name,"ZIP", "RAR", "7z")
            #--------------------------------------------------------------
            if setting["RAR"]==1 and setting["7z"]==2 and setting["ZIP"]==3:
                resultdown=self.__DirectLinks_One_Downloads(name,"RAR", "7z", "ZIP")
            if setting["RAR"]==1 and setting["7z"]==3 and setting["ZIP"]==2:
                resultdown=self.__DirectLinks_One_Downloads(name,"RAR", "ZIP", "7z")
        return resultdown
    def __GoogleLinks_Full_Downloads(self, keyarhiv: str, keyarhiv2: str, keyarhiv3: str):
        """Скачивание Словарей"""
        dictformats={"ZIP": "zip", "RAR": "rar", "7z": "7z"}
        resultdown=False
        for li in self.app.Dicts:
            #-----------------Проверка Наличия Словарей---------------
            dirdicts=f"{dir_path}/{self.app.SettingApp['FolderDicts']['Folder']}"
            filesdicts=li["Files"]
            #---------------------------------------------------------
            if self.__ExistFiles(dirdicts,filesdicts)==False:
                urldown=li["Urls"][keyarhiv]
                urldirect=self.app.GetGoogleLink(urldown)
                filepath=f"{dir_path}/{self.app.SettingApp['FolderDicts']['ArhivesDown']}/{li['Name']}.{dictformats[keyarhiv]}"
                filepathname=f"{dir_path}/{self.app.SettingApp['FolderDicts']['ArhivesDown']}/{li['Name']}"
                dirpath=f"{dir_path}/{self.app.SettingApp['FolderDicts']['ArhivesDown']}"
                dirpath_extract=f"{dir_path}/{self.app.SettingApp['FolderDicts']['Folder']}"
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
                        else:
                            resultdown=self.__ExtractArhiveKey(keyarhiv3, filepathname, dirpath_extract)
                            #resultdown=True
                    else:
                        resultdown=self.__ExtractArhiveKey(keyarhiv2, filepathname, dirpath_extract)
                        #resultdown=True
                else:
                    resultdown=self.__ExtractArhiveKey(keyarhiv, filepathname, dirpath_extract)
                    #resultdown=True
        return resultdown
    def __GoogleLinks_Pack_Downloads(self,pack: int, keyarhiv: str, keyarhiv2: str, keyarhiv3: str):
        """Пачка Скачивание Словарей"""
        dictformats={"ZIP": "zip", "RAR": "rar", "7z": "7z"}
        resultdown=False
        names=[]
        if pack==1:
            names=self.app.SettingApp["ArhivesPack1"]
        if pack==2:
            names=self.app.SettingApp["ArhivesPack2"]
        if pack==3:
            names=self.app.SettingApp["ArhivesPack3"]
        for li in self.app.Dicts:
            if li["Name"] in names:
                #-----------------Проверка Наличия Словарей---------------
                dirdicts=f"{dir_path}/{self.app.SettingApp['FolderDicts']['Folder']}"
                filesdicts=li["Files"]
                #---------------------------------------------------------
                if self.__ExistFiles(dirdicts,filesdicts)==False:
                    urldown=li["Urls"][keyarhiv]
                    urldirect=self.app.GetGoogleLink(urldown)
                    filepath=f"{dir_path}/{self.app.SettingApp['FolderDicts']['ArhivesDown']}/{li['Name']}.{dictformats[keyarhiv]}"
                    filepathname=f"{dir_path}/{self.app.SettingApp['FolderDicts']['ArhivesDown']}/{li['Name']}"
                    dirpath=f"{dir_path}/{self.app.SettingApp['FolderDicts']['ArhivesDown']}"
                    dirpath_extract=f"{dir_path}/{self.app.SettingApp['FolderDicts']['Folder']}"
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
                            else:
                                resultdown=self.__ExtractArhiveKey(keyarhiv3, filepathname, dirpath_extract)
                                #resultdown=True
                        else:
                            resultdown=self.__ExtractArhiveKey(keyarhiv2, filepathname, dirpath_extract)
                            #resultdown=True
                    else:
                        resultdown=self.__ExtractArhiveKey(keyarhiv, filepathname, dirpath_extract)
                        #resultdown=True
        return resultdown
    def __GoogleLinks_One_Downloads(self,name: str, keyarhiv: str, keyarhiv2: str, keyarhiv3: str):
        """Один Скачивание Словарей"""
        dictformats={"ZIP": "zip", "RAR": "rar", "7z": "7z"}
        resultdown=False
        for li in self.app.Dicts:
            if li["Name"]==name:
                #-----------------Проверка Наличия Словарей---------------
                dirdicts=f"{dir_path}/{self.app.SettingApp['FolderDicts']['Folder']}"
                filesdicts=li["Files"]
                #---------------------------------------------------------
                if self.__ExistFiles(dirdicts,filesdicts)==False:
                    urldown=li["Urls"][keyarhiv]
                    urldirect=self.app.GetGoogleLink(urldown)
                    filepath=f"{dir_path}/{self.app.SettingApp['FolderDicts']['ArhivesDown']}/{li['Name']}.{dictformats[keyarhiv]}"
                    filepathname=f"{dir_path}/{self.app.SettingApp['FolderDicts']['ArhivesDown']}/{li['Name']}"
                    dirpath=f"{dir_path}/{self.app.SettingApp['FolderDicts']['ArhivesDown']}"
                    dirpath_extract=f"{dir_path}/{self.app.SettingApp['FolderDicts']['Folder']}"
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
                            else:
                                resultdown=self.__ExtractArhiveKey(keyarhiv3, filepathname, dirpath_extract)
                                #resultdown=True
                        else:
                            resultdown=self.__ExtractArhiveKey(keyarhiv2, filepathname, dirpath_extract)
                            #resultdown=True
                    else:
                        resultdown=self.__ExtractArhiveKey(keyarhiv, filepathname, dirpath_extract)
                        #resultdown=True
        return resultdown
    def __DirectLinks_Full_Downloads(self, keyarhiv: str, keyarhiv2: str, keyarhiv3: str):
        """Скачивание Словарей"""
        dictformats={"ZIP": "zip", "RAR": "rar", "7z": "7z"}
        resultdown=False
        for li in self.app.Dicts:
            #-----------------Проверка Наличия Словарей---------------
            dirdicts=f"{dir_path}/{self.app.SettingApp['FolderDicts']['Folder']}"
            filesdicts=li["Files"]
            #---------------------------------------------------------
            if self.__ExistFiles(dirdicts,filesdicts)==False:
                urldown=li["Urls"][keyarhiv]
                urldirect=self.app.GetGoogleLink(urldown)
                filepath=f"{dir_path}/{self.app.SettingApp['FolderDicts']['ArhivesDown']}/{li['Name']}.{dictformats[keyarhiv]}"
                filepathname=f"{dir_path}/{self.app.SettingApp['FolderDicts']['ArhivesDown']}/{li['Name']}"
                dirpath=f"{dir_path}/{self.app.SettingApp['FolderDicts']['ArhivesDown']}"
                dirpath_extract=f"{dir_path}/{self.app.SettingApp['FolderDicts']['Folder']}"
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
                        else:
                            resultdown=self.__ExtractArhiveKey(keyarhiv3, filepathname, dirpath_extract)
                            #resultdown=True
                    else:
                        resultdown=self.__ExtractArhiveKey(keyarhiv2, filepathname, dirpath_extract)
                        #resultdown=True
                else:
                    resultdown=self.__ExtractArhiveKey(keyarhiv, filepathname, dirpath_extract)
                    #resultdown=True
        return resultdown
    def __DirectLinks_Pack_Downloads(self,pack: int, keyarhiv: str, keyarhiv2: str, keyarhiv3: str):
        """Пачка Скачивание Словарей"""
        dictformats={"ZIP": "zip", "RAR": "rar", "7z": "7z"}
        resultdown=False
        names=[]
        if pack==1:
            names=self.app.SettingApp["ArhivesPack1"]
        if pack==2:
            names=self.app.SettingApp["ArhivesPack2"]
        if pack==3:
            names=self.app.SettingApp["ArhivesPack3"]
        for li in self.app.Dicts:
            if li in names:
                #-----------------Проверка Наличия Словарей---------------
                dirdicts=f"{dir_path}/{self.app.SettingApp['FolderDicts']['Folder']}"
                filesdicts=li["Files"]
                #---------------------------------------------------------
                if self.__ExistFiles(dirdicts,filesdicts)==False:
                    urldown=li["Urls"][keyarhiv]
                    urldirect=self.app.GetGoogleLink(urldown)
                    filepath=f"{dir_path}/{self.app.SettingApp['FolderDicts']['ArhivesDown']}/{li['Name']}.{dictformats[keyarhiv]}"
                    filepathname=f"{dir_path}/{self.app.SettingApp['FolderDicts']['ArhivesDown']}/{li['Name']}"
                    dirpath=f"{dir_path}/{self.app.SettingApp['FolderDicts']['ArhivesDown']}"
                    dirpath_extract=f"{dir_path}/{self.app.SettingApp['FolderDicts']['Folder']}"
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
                            else:
                                resultdown=self.__ExtractArhiveKey(keyarhiv3, filepathname, dirpath_extract)
                                #resultdown=True
                        else:
                            resultdown=self.__ExtractArhiveKey(keyarhiv2, filepathname, dirpath_extract)
                            #resultdown=True
                    else:
                        resultdown=self.__ExtractArhiveKey(keyarhiv, filepathname, dirpath_extract)
                        #resultdown=True
        return resultdown
    def __ExistFiles(self, dir: str, listfiles: list):
        """Проверка наличия Файлов"""
        Flag=False
        for li in listfiles:
            if self.app.GetFileInfo(f"{dir}/{li}")[0]==True:
                Flag=True
            else:
                Flag=False
                break
        return Flag
    def __DirectLinks_One_Downloads(self,name: str, keyarhiv: str, keyarhiv2: str, keyarhiv3: str):
        """Один Скачивание Словарей"""
        dictformats={"ZIP": "zip", "RAR": "rar", "7z": "7z"}
        resultdown=False
        for li in self.app.Dicts:
            if li["Name"]==name:
                #-----------------Проверка Наличия Словарей---------------
                dirdicts=f"{dir_path}/{self.app.SettingApp['FolderDicts']['Folder']}"
                filesdicts=li["Files"]
                #---------------------------------------------------------
                if self.__ExistFiles(dirdicts,filesdicts)==False:
                    urldown=li["Urls"][keyarhiv]
                    urldirect=self.app.GetGoogleLink(urldown)
                    filepath=f"{dir_path}/{self.app.SettingApp['FolderDicts']['ArhivesDown']}/{li['Name']}.{dictformats[keyarhiv]}"
                    filepathname=f"{dir_path}/{self.app.SettingApp['FolderDicts']['ArhivesDown']}/{li['Name']}"
                    dirpath=f"{dir_path}/{self.app.SettingApp['FolderDicts']['ArhivesDown']}"
                    dirpath_extract=f"{dir_path}/{self.app.SettingApp['FolderDicts']['Folder']}"
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
                            else:
                                resultdown=self.__ExtractArhiveKey(keyarhiv3, filepathname, dirpath_extract)
                                #resultdown=True
                        else:
                            resultdown=self.__ExtractArhiveKey(keyarhiv2, filepathname, dirpath_extract)
                            #resultdown=True
                    else:
                        resultdown=self.__ExtractArhiveKey(keyarhiv, filepathname, dirpath_extract)
                        #resultdown=True
        return resultdown
    def __ExtractArhiveKey(self, keyarhiv: str, name: str, dirpath_extract: str):
        """Распаковка в Зависимости Ключа 7z, ZIP, RAR"""
        resultextract=False
        if keyarhiv=="7z":
            resultextract=self.__ExtractArhive(name,dirpath_extract,SelectArhive.SEVENZ)[0]
        if keyarhiv=="ZIP":
            resultextract=self.__ExtractArhive(name,dirpath_extract,SelectArhive.ZIP)[0]
        if keyarhiv=="RAR":
            resultextract=self.__ExtractArhive(name,dirpath_extract,SelectArhive.RAR)[0]
        return resultextract
    def __ExtractArhive(self, arhive_name: str, dir: str, select: SelectArhive):
        """Распаковка"""
        self.__CreateFolder(dir) #Создание Папки куда распаковывать
        res=self.arh.Extract(arhive_name,dir,select)
        return res
    def __DownLoadGoogleLink(self, url: str, file: str):
        """Скачивание Google Link"""
        Flag,error=False,""
        try:
            urlgoogle=self.app.GetGoogleLink(url)
            Flag=self.app.DownloadFile(urlgoogle, file)
        except Exception as ex:
            error=f"ERROR: {ex}!"
        return [Flag,error]
    def __DownLoadDirect(self, url: str, file: str):
        """Скачивание Прямая Ссылка"""
        Flag,error=False,""
        try:
            Flag=self.app.DownloadFile(url,file)
        except Exception as ex:
            error=f"ERROR: {ex}!"
        return [Flag,error]
    def __CreateFolder(self, dir: str):
        """Создание Папки"""
        Flag,error=False,""
        try:
            self.app.CreateDir(dir)
        except Exception as ex:
            error=f"ERROR: {ex}!"
        return [Flag,error]



# app=AppProcessLinex()
# app.GetNamesDicts()