

from typing import Any
from utils.prints import LINE, width

def print_rules(rules: Any) -> None:
    print("\n\n\n")
    print("ROUTES")
    print(f"{LINE['=']}")
    stem = ""

    for i, route in enumerate(rules):  
        try:
            url_stem = route.endpoint.split(".")[-2]
        except: url_stem = "base"

        if stem != url_stem:
            if i != 0: print(LINE['-bot'])
            print("\n", url_stem)
            print(LINE['-top'])
            stem = url_stem
        else: print(LINE['-mid'])
        print(f"│",  f">> {f'({route.endpoint})':15} {route.methods:}   {route.rule} "  )
    print(LINE['-bot'])
    print(f"{LINE['=']}")
