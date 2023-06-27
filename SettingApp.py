import os, sys, time, re, json, datetime, random
import requests
import urllib.request
from alive_progress import alive_bar
from alive_progress.styles import showtime
from os.path import basename

dir_path = os.path.dirname(os.path.realpath(__file__))

class Setting(object):
    """Настройки Приложения"""
    __settingfile=f"{dir_path}/SettingApp.json"
    """Файл Настроек"""
    Version=""
    """Версия"""
    Dicts=None
    """Данные Словари"""
    SettingApp=None
    """Данные Настройки"""
    def __init__(self, encod="utf-8"):
        super(Setting, self).__init__()
        if os.path.exists(self.__settingfile):
            try:
                with open(self.__settingfile, 'r', encoding=encod) as f:
                    data = json.load(f)
                    self.SettingApp=data
                    self.Version = float(data['Version'])
                    filedicts=data['FileDicts']
                    fullfiledicts=f"{dir_path}/{filedicts}"
                    self.Dicts=self.ReadDicts(fullfiledicts)
            except Exception as ex:
                print(f"ERROR SETTING: {ex}!")
        else:
            print(f"ERROR: Нету {self.__settingfile} Файла!")
    def Title(self):
        """Титулка"""
        title=f"title Linex v {self.Version:.3f}"
        os.system(title)
    def CreateDir(self, dir: str):
        """Создать Папку"""
        if os.path.exists(dir)==False:
            os.mkdir(dir)
    def ReadFile(self, file: str, encod="utf-8"):
        """Чтение Файла"""
        text=""
        if os.path.exists(file):
            try:
                with open(file, 'r', encoding=encod) as f:
                    text = f.read()
            except Exception as ex:
                print(f"ERROR FILE: {ex}!")
        return text
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
    def MaskValide(self, mask: str):
        """Валидность Маски Устройства"""
        patterns = [
            r'^([0-9A-Fa-f]{2}[-:]){5}[0-9A-Fa-f]{2}$',
            r'^([0-9A-Fa-f]{2}[:]){5}[0-9A-Fa-f]{2}$',
            r'^([0-9A-Fa-f]{2}[.]){5}[0-9A-Fa-f]{2}$',
        ]
        #regex = re.compile('|'.join(patterns))
        pattern = r'^([0-9A-Za-z]{2}-){5}[0-9A-Za-z]{2}$'
        #regex = re.compile(r'^([0-9A-Fa-f]{2}[-:]){5}[0-9A-Fa-f]{2}$')
        if re.match(pattern, mask):
            return True
        else:
            return False
    def DownloadFile2(self, url: str, filepath: str, style="classic"):
        """Загрузить Файл 2"""
        Flag=False
        try:
            urllib.request.urlretrieve(url, filepath)
            # command=f'wget -O "{filepath}" "{url}"'
            # os.system(command)
            # response = requests.get(url, stream=True)
            # total_size = int(response.headers.get("content-length", 0))
            # block_size = 1024  # задайте размер блока загрузки по вашему усмотрению
            # with open(filepath, "wb") as f, alive_bar(total_size, bar=style) as bar:
            #     for data in response.iter_content(block_size):
            #         f.write(data)
            #         bar(len(data))
            Flag=True
        except Exception as ex:
            print(f"ERROR DOWNLOAD: {ex}!")
        return Flag
    def DownloadFile(self, url: str, filepath: str, style="classic"):
        """Загрузить Файл"""
        Flag=False
        try:
            #urllib.request.urlretrieve(url, filepath)
            # command=f'wget -O "{filepath}" "{url}"'
            # os.system(command)
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get("content-length", 0))
            block_size = 1024  # задайте размер блока загрузки по вашему усмотрению
            with open(filepath, "wb") as f, alive_bar(total_size, bar=style) as bar:
                for data in response.iter_content(block_size):
                    f.write(data)
                    bar(len(data))
            Flag=True
        except Exception as ex:
            print(f"ERROR DOWNLOAD: {ex}!")
        return Flag
    def LinkValid(self, url: str):
        """Проверка Ссылка"""
        Flag=False
        regex = r'^(https?://)?([a-zA-Z0-9-]+\.)*[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})(:\d{2,5})?(/.*)?$'
        if re.match(regex, url):
            Flag=True
        # response = requests.head(url)
        # if response.status_code in codes:
        #     Flag=True
        return Flag
    def Input(self, text: str):
        """Ввод Данных"""
        Flag=False
        res=input(text)
        res=res.strip()
        if not res.strip():
            Flag=False
        else:
            Flag=True
        return [Flag,res]
    def InputWhile(self, text: str):
        """Ввод Данных Цыкловый"""
        Flag,Res=True,""
        while Flag:
            Res=input(text)
            if not Res.strip():
                print("Пустое Значение!")
            else:
                Flag=False
        return Res

        
