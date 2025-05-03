from fastapi import FastAPI
from pydantic import BaseModel
from dataclasses import dataclass
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware (
    CORSMiddleware, 
    allow_origins = ["http://127.0.0.1:8000"]
)

PeopleInTheBar_data = [
    {
"id": 1,
"name": "TeethFairy",
"skill": "",
"Type": 0
},

   {
"id": 1,
"name": "TeethFairy",
"skill": "",
"Type": 0
}
]

@dataclass
class Fairis:

    id: id
    type: str
    name: str

@dataclass
class FairisWithWings(Fairis):
    length: int

new_Fairy = Fairis (1,'predator','Rita')

print (new_Fairy)

class Gnomes:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Gnomes(name = {self.name})"

new_Gnome = Gnomes ('Kesha')
print (new_Gnome)

@app.get("/list")
def get_list():
    return PeopleInTheBar_data

