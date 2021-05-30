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
        self.RUNNING = True

        # env_vars
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
        print("creating startup task for windows")
        print(os.system(
            "cd /d %userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup & echo start " + self.PATH + "main.exe" + " > FBackup.bat"))


Global = GLOBAL()
