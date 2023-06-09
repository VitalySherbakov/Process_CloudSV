import os, sys, time, re, json, datetime, random
from SettingApp import Setting
from App_Process import AppProcessLinex, SelectProgram
from ArhivatorLinexLib import ArhiveLinex, SelectArhive

dir_path = os.path.dirname(os.path.realpath(__file__))

platform_name=sys.argv[1] #Получить Платформу для доступа