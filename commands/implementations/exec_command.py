import subprocess
from commands.command_base import CommandBase

class ExecCommand(CommandBase):
  def run_command(self, command_data):
    print ('running command')
    command_to_run = command_data['command']
    args = command_data['args']
    try:
      result = subprocess.run([command_to_run, args], capture_output=True, text=True, check=True)
      return {"Status": "Success", "output": result.stdout}
    except subprocess.CalledProcessError as e:
      return {"Status": "Failed", "error": e.stderr}