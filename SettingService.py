import os, sys, time, re, json, datetime, random
from os.path import basename
import requests
import urllib.request
from alive_progress import alive_bar
from alive_progress.styles import showtime

dir_path = os.path.dirname(os.path.realpath(__file__))

class Shablon(object):
    """Шаблон"""
    Dicts="",
    """Папка Словарей"""
    DictsDownload=""
    """Папка Архитвов Словарей Скачивания"""
    CapDir=""
    """Папка WIFI"""
    CPU_Dir=""
    """CPU Папка"""
    CPU_Url=""
    """CPU Ссылка"""
    CPU_Arhive=""
    """CPU Архив"""
    CPU_Run=""
    """CPU Файл Запуска"""
    GPU_Dir=""
    """GPU Папка"""
    GPU_Url=""
    """GPU Ссылка"""
    GPU_Arhive=""
    """GPU Архив"""
    GPU_Run=""
    """GPU Файл Запуска"""
    Arhive_Pack1=[]
    """Список Архивов Пачки 1"""
    Arhive_Pack2=[]
    """Список Архивов Пачки 2"""
    Arhive_Pack3=[]
    """Список Архивов Пачки 3"""
    Select_Program=""
    """Програма Выбраная"""
    Run_Cap_Select=""
    """Выбрать что делать"""
    Run_Cap_Url=""
    """Сскачать Ссылка"""
    Run_Cap_Path=""
    """Путь к Файлу"""
    Run_Dicts_Command=""
    """Команда Что делать"""
    Run_Dicts_Select=""
    """Значение в Зависимости Команды"""
    Arhive_7z_Dir=""
    """Папка Архиватора 7z"""
    Arhive_7z_Run=""
    """Файл Архиватора 7z"""
    Arhive_RAR_Dir=""
    """Папка Архиватора RAR"""
    Arhive_RAR_Run=""
    """Файл Архиватора RAR"""
    Arhive_ZIP_Dir=""
    """Папка Архиватора ZIP"""
    Arhive_ZIP_Run=""
    """Файл Архиватора ZIP"""

class Setting(object):
    """Настройки Приложения"""
    Encode="utf-8"
    """Кодировка"""
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
        self.Encode=encod
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
    def ReadShablon(self, file: str):
        """Чтение Шаблона"""
        Flag,lines_shab=False,[]
        shab=Shablon()
        if os.path.exists(file)==True:
            with open(file, 'r', encoding=self.Encode) as f:
                lines = f.readlines()
                for li in lines:
                    li=li.strip()
                    if li:
                        if (li in lines_shab)==False:
                            lines_shab.append(li)
            #--------Шаблон----------
            for li in lines_shab:
                li=str(li).strip()
                mass=li.split("=")
                if mass[0].lower()=="dict_dir":
                    shab.Dicts=mass[1]
                if mass[0].lower()=="dict_down":
                    shab.DictsDownload=mass[1] 
                if mass[0].lower()=="cap_dir":
                    shab.CapDir=mass[1]
                if mass[0].lower()=="cpu_dir":
                    shab.CPU_Dir=mass[1]
                if mass[0].lower()=="cpu_url":
                    shab.CPU_Url=mass[1]
                if mass[0].lower()=="cpu_arhive":
                    shab.CPU_Arhive=mass[1]
                if mass[0].lower()=="cpu_run":
                    shab.CPU_Run=mass[1]
                if mass[0].lower()=="gpu_dir":
                    shab.GPU_Dir=mass[1]
                if mass[0].lower()=="gpu_url":
                    shab.GPU_Url=mass[1]
                if mass[0].lower()=="gpu_arhive":
                    shab.GPU_Arhive=mass[1]
                if mass[0].lower()=="gpu_run":
                    shab.GPU_Run=mass[1]
                if mass[0].lower()=="arhive_pack1":
                    shab.Arhive_Pack1=list(eval(mass[1]))
                if mass[0].lower()=="arhive_pack2":
                    shab.Arhive_Pack2=list(eval(mass[1]))
                if mass[0].lower()=="arhive_pack3":
                    shab.Arhive_Pack3=list(eval(mass[1]))
                if mass[0].lower()=="run_select_program":
                    shab.Select_Program=mass[1]
                if mass[0].lower()=="run_cap_select":
                    shab.Run_Cap_Select=mass[1]
                if mass[0].lower()=="run_cap_url":
                    shab.Run_Cap_Url=mass[1]
                if mass[0].lower()=="run_cap_path":
                    shab.Run_Cap_Path=mass[1]
                if mass[0].lower()=="run_dicts_command":
                    shab.Run_Dicts_Command=mass[1]
                if mass[0].lower()=="run_dicts_select":
                    shab.Run_Dicts_Select=mass[1]
                if mass[0].lower()=="arhive_7z_dir":
                    shab.Arhive_7z_Dir=mass[1]
                if mass[0].lower()=="arhive_7z_run":
                    shab.Arhive_7z_Run=mass[1]
                if mass[0].lower()=="arhive_rar_dir":
                    shab.Arhive_RAR_Dir=mass[1]
                if mass[0].lower()=="arhive_rar_run":
                    shab.Arhive_RAR_Run=mass[1]
                if mass[0].lower()=="arhive_zip_dir":
                    shab.Arhive_ZIP_Dir=mass[1]
                if mass[0].lower()=="arhive_zip_run":
                    shab.Arhive_ZIP_Run=mass[1]
            Flag=True
        return [Flag,lines_shab,shab]
    def DownloadFile(self, url: str, filepath: str, style="classic"):
        """Скачивание Файлов"""
        Flag=False
        try:
            print(f"Скачивание {filepath}...")
            #pathdir=os.path.dirname(filepath)
            #self.CreateDir(pathdir)
            # urllib.request.urlretrieve(url, filepath)
            # print(f"Файл: {filepath} Загружен!")
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
    def ExtractArhive(self, arhiv: str, dir: str):
        """Распаковка Архива"""
        if os.path.exists(arhiv):
            self.CreateDir(dir)
            pass 
        else:
            print(f"Нету {arhiv} Архива!")