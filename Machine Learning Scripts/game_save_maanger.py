# game_save_manager.py

import os
import shutil
import time
import psutil

GAME_PROCESS_NAME = "game_name.exe"  # Replace with the actual game process name
SAVE_FILE_PATH = "C:/Games/GameName/saves/savefile.dat"
BACKUP_FILE_PATH = "C:/Games/GameName/saves/backup_savefile.dat"

def is_game_running(process_name):
    """Checks if a process with the given name is running."""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False

def backup_save_file():
    """Creates a backup of the game save file."""
    if os.path.exists(SAVE_FILE_PATH):
        shutil.copy(SAVE_FILE_PATH, BACKUP_FILE_PATH)
        print("Backup created successfully.")
    else:
        print("Save file does not exist.")

def restore_save_file():
    """Restores the backup save file."""
    if os.path.exists(BACKUP_FILE_PATH):
        shutil.copy(BACKUP_FILE_PATH, SAVE_FILE_PATH)
        print("Save file restored successfully.")
    else:
        print("Backup file does not exist.")

if __name__ == "__main__":
    print("Waiting for game process to start...")
    while True:
        if is_game_running(GAME_PROCESS_NAME):
            print(f"{GAME_PROCESS_NAME} is running. Creating backup...")
            backup_save_file()
            break
        time.sleep(5)  # Check every 5 seconds

# Call this function whenever you want to restore the backup
# restore_save_file()
