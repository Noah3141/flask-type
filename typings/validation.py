from typing import TypeVar


T = TypeVar("T")
def some(val: T | None) -> T:
    if val is None: raise Exception(f"NonNullable value passed as None: {val=}")
    else: return val


def ss(*arg: str | None) -> str:
    "Some string validation: converts a `str | None -> str`, erroring if None"
    if arg[0] is None: raise Exception("")
    else: return arg[0]


def si(*arg: int | None) -> int:
    if arg[0] is None: raise Exception("")
    else: return arg[0]
