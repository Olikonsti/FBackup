import shutil
import datetime
import os
import time

from GLOBAL import Global
from shutil import *



class Backup:
    def __init__(self, src, dest, name, time):
        self.src = src
        self.dest = dest
        self.name = name
        self.weekday = "Everyday"
        self.time = time
        self.count = 0
        self.paused = False
        self.running = False
        self.already_ran = False
        self.last_folder = ""
        self.second_last_folder = ""
        self.keep_second_last = True

        self.tab_selected = False

        Global.backups.append(self)

    def select(self):
        for i in Global.backups:
            i.deselect()
        self.tab_selected = True

    def deselect(self):
        self.tab_selected = False

    def edit(self):
        pass

    def exec_code(self, code):
        try:
            exec(code)
            print("---Code ran sucessfully---")
        except Exception as e:
            print(e)

    def delete(self):
        Global.backups.remove(self)
        del self

    def run(self, mode=0):
        self.running = True
        Global.request_refresh()
        print(f"----RUN----({self.name})")
        if self.src == "" or self.dest == "":
            print(f"{self.name}: skipping, No SRC/DEST defined")
        else:
            if not self.paused or mode == 1:

                if self.keep_second_last:
                    self.count += 1
                    now = datetime.datetime.now()
                    self.folder = self.dest + f"/{now.day}_{now.month}_{now.year}_H{now.hour}_{now.minute}_{now.second}"
                    shutil.copytree(self.src, self.folder)

                    try:
                        shutil.rmtree(self.second_last_folder)
                    except Exception as e:
                        print(f"last backup not found!: {e}")
                    self.second_last_folder = self.last_folder
                    self.last_folder = self.folder
                else:
                    self.count += 1
                    now = datetime.datetime.now()
                    self.folder = self.dest + f"/{now.day}_{now.month}_{now.year}_H{now.hour}_{now.minute}_{now.second}"
                    shutil.copytree(self.src, self.folder)
                    try:
                        shutil.rmtree(self.last_folder)
                    except Exception as e:
                        print(f"last backup not found!: {e}")
                    self.last_folder = self.folder
            else:
                print(f"{self.name}: paused!")
        print(f"----FINISH----({self.name})")
        time.sleep(3)
        self.running = False
        Global.request_refresh()