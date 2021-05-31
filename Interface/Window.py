from GLOBAL import *
from VerticalScrolledFrame import *
from Backup import *
from Interface.Edit_View import *
import os

class Window(Tk):
    def __init__(self):
        super().__init__()
        print("Starting Interface")
        self.last_selected = None
        self.edit_view = None

        self.main_view = Frame(self)
        self.main_view.pack(expand=True, fill=BOTH)

        self.title(f"FNBackup - {Global.VERSION}")
        self.geometry("700x400")
        self.resizable(True, True)
        self.iconbitmap("icon.ico")

        self.top_bar = Frame(self.main_view)
        self.top_bar.pack(fill=X)

        self.leftPane = VerticalScrolledFrame(self.main_view)
        self.leftPane.pack(fill=BOTH, side=LEFT)
        self.rightPane = Frame(self.main_view)
        self.rightPane.pack(expand=True, fill=BOTH, side=RIGHT)

        self.backups_list_view = Frame(self.leftPane.interior, width=200)
        self.backups_list_view.pack(fill=X)


        self.add_directory_button = ttk.Button(self.top_bar, text="+", command=self.add_directory, width=3)
        self.add_directory_button.pack(side=LEFT)

        self.about_button = ttk.Button(self.top_bar, text="About", command=self.open_about_page)
        self.about_button.pack(side=LEFT)

        self.settings_button = ttk.Button(self.top_bar, text="Settings", command=lambda: os.system("start settings/config.txt"))
        self.settings_button.pack(side=LEFT)

        self.startup_button = ttk.Button(self.top_bar, text="Add to system startup", command=Global.create_startup_task)
        self.startup_button.pack(side=LEFT)

        self.refresh_button = ttk.Button(self.top_bar, text="Refresh", command=lambda: [self.update_backup_list_view()])
        self.refresh_button.pack(side=LEFT)

        self.update_tasks()
        self.update_backup_list_view()

        self.mainloop()

    def open_about_page(self):
        self.temp_win = Tk()
        self.temp_win.title("About FNBackup")
        self.temp_win.resizable(False, False)

        Label(self.temp_win, text="FNBackup", font="Consolas 20").pack(pady=(10, 0))

        self.about_frame = Frame(self.temp_win); self.about_frame.pack(padx=10, pady=10)

        Label(self.about_frame, text="Developer: Konstantin Ehmann").pack(anchor=W)
        Label(self.about_frame, text=f"Version: {Global.VERSION}").pack(anchor=W)
        Label(self.about_frame, text="Instruction on how to use: https://ksite.ddns.net").pack(anchor=W)

    def update_tasks(self):
        self.after(50, self.update_tasks)

        # update if number of backups changes
        if len(Global.backups) != Global.last_backup_list_lenght:
            self.update_backup_list_view()
            self.update()

        # update if selection changes
        try:
            if self.last_selected.tab_selected:
                pass
            else:
                self.update_backup_list_view()

        except:
            pass

        if Global.req_ref:
            Global.req_ref = False
            self.update_backup_list_view()

        # save selected item
        for i in Global.backups:
            if i.tab_selected:
                self.last_selected = i
                i.running = False


    def update_backup_list_view(self):
        # clear backups_frame
        self.backups_list_view.destroy()
        self.backups_list_view = Frame(self.leftPane.interior, width=200)
        self.backups_list_view.pack(fill=X)

        self.update()
        for i in Global.backups:
            item_frame = Frame(self.backups_list_view)
            state = Frame(item_frame, bg="orange", height=20, width=20)
            state.pack(side=RIGHT, padx=3)
            item_frame.pack()

            if i.paused:
                state.config(bg="red")

            if i.running:
                state.config(bg="green")


            if i.tab_selected:
                Button(item_frame, text=i.name, bg="lightblue", command=i.select(), width=20).pack(side=LEFT)
                try:
                    self.edit_view.destroy()
                except:
                    pass
                self.edit_view = Edit_View(self.rightPane, i, self)
                self.edit_view.pack(expand=True, fill=BOTH, padx=5, pady=5)
            else:
                Button(item_frame, text=i.name, command=i.select, width=20).pack(side=LEFT)


        Global.last_backup_list_lenght = len(Global.backups)


    def add_directory(self):
        i = Backup("", "", f"BackupFolder {len(Global.backups)+1}", "20:00")
        i.select()
        self.last_selected = i