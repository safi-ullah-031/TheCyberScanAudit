import subprocess
import logging

def run_command(command, shell=True):
    try:
        result = subprocess.run(command, shell=shell, capture_output=True, text=True)
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except Exception as e:
        logging.error(f"Error running command '{command}': {e}")
        return '', str(e), 1
