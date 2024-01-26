import json
import os
from watchdog.events import FileSystemEventHandler

class fileWatcher(FileSystemEventHandler):
  def __init__(self, command, path_for_output) -> None:
    self._command = command
    self._path_for_output = path_for_output
    super().__init__()

  def on_created(self, event):
    print('file received')
    if event.is_directory:
      return
    filename = os.path.basename(event.src_path)
    if filename.endswith('.json'):
      try:
        with open(event.src_path, 'r') as file:
            json_data = json.load(file)  
      except Exception as e:
        print(f"Error reading JSON file: {e}")
        return
      output = self._command.run_command(json_data)
      with open(f'{self._path_for_output}\\{filename}', 'w+') as output_file:
        json.dump(output, output_file, indent=2)