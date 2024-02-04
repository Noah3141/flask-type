import os
from typing import Dict, List, Literal, Union
from colorama import Fore, Back, Style
from typing_extensions import override

class Print():
    def __init__(self, text: str):
        self.text = text
        self.red = Fore.RED + text + Fore.RESET
        self.blue = Fore.BLUE + text + Fore.RESET
        self.green = Fore.GREEN + text + Fore.RESET

    @override  
    def __repr__(self) -> str:
        return self.text
    
width = os.get_terminal_size().columns
LINE: Dict[Literal[
    '-', 
    '=', 
    '||',
    '=top',
    '=mid',
    '=bot',
    '-top',
    '-mid',
    '-bot',
], Print] = {
    '-':  Print('─' * width),
    '=': Print("═" * width),
    '||': Print('║'),
    '=top': Print('╔' + "═" * (width - 2) + '╗'),
    '=bot': Print('' + "═" * (width - 2) + ''),
    '-top': Print('┌' + '─' * (width - 2) + '┐'),
    '-mid': Print('├' + '─' * (width - 2) + '┤'),
    '-bot': Print('└' + '─' * (width - 2) + '┘'),
}
