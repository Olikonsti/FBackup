# FNBackup
 Create Backups with python  
 more info: https://ksite.ddns.net/services/themes/Ksite_Pages/fnbackup.html

![image](https://user-images.githubusercontent.com/68354546/120193068-4193a500-c21c-11eb-9d9e-9fc1a878047e.png)

# Instuctions/Help

## Quick Start Guide
### Tips: 
please start the program only once. When you close the gui the Program WONT CLOSE. It will run in the background. You can open the gui back up by rightclicking the Windows System Tray icon "FB" and then press "Open GUI". You can also COMPLEATLY CLOSE the program in the system tray.

### Adding Program to Windows Startup
 Just press "Add to system startup". It will create a .bat file in the "shell:startup" folder.  
 By default FNBackup opens up with a gui at system startup. You can change that by clicking on "Settings" and changing the option "self.START_WITH_INTERFACE" to "False"  
 
### Creating a new BackupFolder Entry  
 Press the small "+" button in the top left corner.  
 You can change the Name of the backup directory by typing in the top entry box.  
 Now select a source and destination directory.  
 Select a time and a weekday.  
 
 PRESS ON SAVE!  
 
 You can also prevent a backup from beeing made in time by pressing "Pause Timer".  
 You can also start a backup manually ba pressing "Start Manually".  
 
## Backup Activity indicator
![image](https://user-images.githubusercontent.com/68354546/120196856-9f29f080-c220-11eb-8dbd-3e3447db57e7.png)  
 Orange: Waiting for correct time to start making the Backup  
 Red: Backup will not be made when the time is ready. The Backup is paused  
 Green: Backup is currently beeing made! Please dont start it again manually! You can start other Backups manually  
