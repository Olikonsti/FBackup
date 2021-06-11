from GLOBAL import *

class Settings(Tk):
    def __init__(self):
        super(Settings, self).__init__()
        self.title("FNBackup Settings")
        self.resizable(False, False)
        self.geometry("500x400")

        # settings
        self.apply_button = ttk.Button(self, text="Apply")
        self.apply_button.pack(side=BOTTOM, anchor=E, padx=10, pady=10)