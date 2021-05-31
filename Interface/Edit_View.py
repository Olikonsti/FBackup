from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from GLOBAL import *
import tkinter.ttk as ttk
import pickle

class Edit_View(LabelFrame):
    def __init__(self, parent, instance, window):
        super(Edit_View, self).__init__(parent, text="Edit")
        self.instance = instance
        self.window = window

        self.src_dir = self.instance.src
        self.dest_dir = self.instance.dest
        self.time = self.instance.time

        self.top_bar = Frame(self)
        self.top_bar.pack(fill=X)

        self.name = ttk.Entry(self.top_bar)
        self.name.insert(0, instance.name)
        self.name.pack(side=LEFT)

        self.delete_button = Button(self.top_bar, text="-", width=3, command=self.delete_backup)
        self.delete_button.pack(side=RIGHT)

        self.pause_button = Button(self.top_bar, text="Pause Timer", bg="lightgrey", command=self.pause_pressed)
        if self.instance.paused:
            self.pause_button.config(text="Start Timer", bg="orange")
        self.pause_button.pack(side=RIGHT)

        self.start_now = Button(self.top_bar, text="Start Manually", command=self.run_manu)
        self.start_now.pack(side=RIGHT)

        self.apply_button = ttk.Button(self, text="Save", command=self.apply)
        self.apply_button.pack(side=BOTTOM, anchor=E)

        self.src_frame = LabelFrame(self, text="Source Dir")
        self.src = Label(self.src_frame, text=instance.src)
        self.src.pack(side=LEFT)
        self.src_select = Button(self.src_frame, text="Select Folder", command=self.sel_src)
        self.src_select.pack(side=RIGHT)
        self.src_frame.pack(anchor=W)

        self.dest_frame = LabelFrame(self, text="Destination Dir")
        self.dest = Label(self.dest_frame, text=instance.dest)
        self.dest.pack(side=LEFT)
        self.dest_select = Button(self.dest_frame, text="Select Folder", command=self.sel_dest)
        self.dest_select.pack(side=RIGHT)
        self.dest_frame.pack(anchor=W)

        self.line = Frame(self)
        self.line.pack(anchor=W, fill=X)
        self.time_frame = LabelFrame(self.line, text="Time")
        self.time_frame.pack(side=LEFT)
        self.time_entry = ttk.Entry(self.time_frame)
        self.time_entry.insert(0, instance.time)
        self.time_entry.pack()

        self.weekday_frame = LabelFrame(self.line, text="Weekday")
        self.weekday_frame.pack(side=LEFT, padx=10)
        self.weekday_var = StringVar()
        weekdays = ["Everyday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.weekend_menu = ttk.OptionMenu(self.weekday_frame, self.weekday_var, self.instance.weekday,*weekdays)
        self.weekend_menu.pack()

        self.counter = Label(self, text=f"Backup {instance.count} times made (since last backup_list_view update)")
        self.counter.pack(anchor=W)

        self.run_attrs = LabelFrame(self, text="Run code in object (Advanced Options)")
        self.run_attrs.pack(anchor=W, side=BOTTOM)
        self.run_entry = ttk.Entry(self.run_attrs, width=30)
        self.run_entry.pack(side=LEFT)
        self.run_button = ttk.Button(self.run_attrs, text="Run", command=lambda: self.instance.exec_code(self.run_entry.get()))
        self.run_button.pack(side=RIGHT)

    def run_manu(self):
        Thread(target=lambda: self.instance.run(1)).start()

    def cmd_list(self):
        print("""---COMMANDS---
        self.keep_second_last = True/False
        self.name = string
        
        ------
        """)

    def sel_src(self):
        self.src_dir = filedialog.askdirectory()
        self.src.config(text=self.src_dir)

    def sel_dest(self):
        self.dest_dir = filedialog.askdirectory()
        self.dest.config(text=self.dest_dir)

    def apply(self):
        self.counter.config(text=f"Backup {self.instance.count} times made (since last backup_list_view update)")
        self.instance.src = self.src_dir
        self.instance.dest = self.dest_dir
        self.instance.name = self.name.get()
        self.instance.time = self.time_entry.get()
        self.instance.weekday = self.weekday_var.get()

        self.window.update_backup_list_view()

        f = open("backups.dump", "wb")
        pickle.dump(Global.backups, f)
        f.close()


    def delete_backup(self):
        result = messagebox.askquestion("Confirmation", f"Are you sure you want to delete the Backup folder '{self.instance.name}'")
        if result == "yes":
            self.instance.delete()
            self.destroy()
            try:
                Global.backups[0].select()
            except:pass
            del self

    def pause_pressed(self):
        if self.instance.paused:
            self.instance.paused = False
            self.pause_button.config(text="Pause Timer", bg="lightgrey")
        else:
            self.instance.paused = True
            self.pause_button.config(text="Start Timer", bg="orange")

        Global.request_refresh()




