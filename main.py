import time
import os
from watchdog.observers import Observer
from file_watcher import fileWatcher
from commands.implementations.exec_command import ExecCommand

def watch_folder(folder_path, command_executer):
    event_handler = fileWatcher(command_executer, f'{folder_path}\\output')
    observer = Observer()
    observer.schedule(event_handler, path=f'{folder_path}\\input', recursive=False)
    
    print(f"Watching folder: {folder_path}")
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    folder_path_to_watch = os.getcwd()
    command = ExecCommand()
    watch_folder(folder_path_to_watch, command)