from typing import TypedDict

class person(TypedDict):

    name : str
    age : int

new_persin : person = {"name" : "Mayank", "age" : 21}

print(new_persin)