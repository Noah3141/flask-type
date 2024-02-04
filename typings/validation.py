from typing import TypeVar


T = TypeVar("T")
def z(val: T | None) -> T:
    if val is None: raise Exception(f"NonNullable value passed as None: {val=}")
    else: return val


