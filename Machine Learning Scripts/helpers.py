import psutil

def is_game_running(process_name):
    """Checks if a process with the given name is running."""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False