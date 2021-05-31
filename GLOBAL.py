from tkinter import *
import tkinter.ttk as ttk
import time
from threading import *
import os
from tkinter import filedialog



class GLOBAL():
    def __init__(self):
        print("Preparing Global Class...")

        # settings
        self.START_WITH_INTERFACE = True
        self.START_WITH_SERVICE = True

        try:
            f = open("settings/config.txt", "r")
            exec(f.read())
            f.close()
        except:print("error loading config file")

        self.RUNNING = True

        # env_vars
        self.VERSION = 1.2
        self.PATH = os.getcwd()+"\\"
        self.DATA_FOLDER = "DATA/"

        # runtime vars
        self.last_backup_list_lenght = 0
        self.backups = []
        self.req_ref = False

    def request_refresh(self):
        self.req_ref = True


    def create_startup_task(self):
        """
        Only works on windows
        """

        exec("global USER_NAME; import getpass; USER_NAME = getpass.getuser()")

        print("creating startup task for windows")
        f = open(f"C:\\Users\\{USER_NAME}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\FBackup.bat", "w")
        f.write('cd /d ' + self.PATH + ' & start main.exe')
        f.close()

Global = GLOBAL()
