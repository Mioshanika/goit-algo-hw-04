from pathlib import Path
from colorama import Fore

def print_folder_tree(path: str, level = 0) -> None:
    current_dir = Path(path)
    if (not Path.exists(current_dir)) or (not current_dir.is_dir()):
        return
    for item in Path.iterdir(current_dir):
        if item.is_dir():
            print(' '*4*level + Fore.BLUE + item.name + '/' + Fore.RESET)
            print_folder_tree(str(item), level+1)
        else:
            print(' '*4*level + Fore.GREEN + item.name + Fore.RESET)
