import pickle
import datetime
import time

from GLOBAL import *
from Interface.Window import *
from infi.systray import SysTrayIcon



class Service():
    def __init__(self):
        try:
            f = open("backups.dump", "rb")
            Global.backups = pickle.load(f)
            f.close()
        except:
            pass

        # start modules if enabled
        if Global.START_WITH_SERVICE:
            self.queue = []
            Thread(target=self.bg_loop).start()
            Thread(target=self.queue_thread).start()
            try:
                menu_options = (("Open GUI", None, self.open_win),)
                systray = SysTrayIcon("icon.ico", f"FNBackup - {Global.VERSION}", menu_options, on_quit=self.close)
                systray.start()
            except:
                print("Systray could not be started!")

        if Global.START_WITH_INTERFACE:
            Window()


    def open_win(self, lel=None):
        Window()

    def close(self, lel=None):
        Global.RUNNING = False

    def bg_loop(self):
        print("Starting BG task")

        for i in Global.backups:
            i.already_ran = False

        while Global.RUNNING:
            now = datetime.datetime.now()
            for i in Global.backups:

                if i.time == str(now.hour) + ":" + str(now.minute) and not i.already_ran:
                    if i.weekday == "Everyday" or datetime.datetime.today().strftime('%A') == i.weekday:
                        i.already_ran = True
                        self.queue.append(i)
                        print(f"Adding Backup '{i.name}' to queue")
                    else:
                        print(f"{i.name}: Pass, not correct weekday")

                if i.time == str(now.hour) + ":" + str(now.minute - 2) and i.already_ran:
                    i.already_ran = False
                    print(f"Reset Backup.already_ran for '{i.name}'")

            time.sleep(5)
            f = open("backups.dump", "wb")
            pickle.dump(Global.backups, f)
            f.close()

    def queue_thread(self):
        print("Starting Queue thread")
        while Global.RUNNING:
            self.queue_copy = self.queue.copy()
            for i in self.queue_copy:
                print(f"Starting queue run for {i.name}")
                i.run()
                try:
                    self.queue.remove(i)
                except Exception as e:
                    print(e)
                print(f"Finished queue run for {i.name}")
            time.sleep(20)



