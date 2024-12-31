from collections.abc import Callable
from enum import Enum, auto
from typing import Annotated
from annotated_types import Le
from pydantic import BaseModel

class Gender(Enum):
    MALE = auto()
    FEMALE = auto()
    UNKNOW = auto()

    def __str__(self) -> str:
        match self.name:
            case "MALE":
                return "♂"
            case "FEMALE":
                return "♀"
            case "UNKNOW":
                return ""

class Nature(Enum):
    HARDY = auto()
    LONELY = auto()
    BRAVE = auto()
    ADAMANT = auto()
    NAUGHTY = auto()
    BOLD = auto()
    DOCILE = auto()
    RELAXED = auto()
    IMPISH = auto()
    LAX = auto()
    TIMID = auto()
    HASTY = auto()
    SERIOUS = auto()
    JOLLY = auto()
    NAIVE = auto()
    MODEST = auto()
    MILD = auto()
    QUIET = auto()
    BASHFUL = auto()
    RASH = auto()
    CALM = auto()
    GENTLE = auto()
    SASSY = auto()
    CAREFUL = auto()
    QUIRKY = auto()

    def __str__(self) -> str:
        return self.name.title()

class Status(Enum):
    NORMAL = auto()
    BURN = auto()
    FREEZE = auto()
    PARALYSIS = auto()
    POISON = auto()
    SLEEP = auto()

    def __str__(self) -> str:
        match self.name:
            case "NORMAL":
                return ""
            case "BURN":
                return "BRN"
            case "FREEZE":
                return "FRZ"
            case "PARALYSIS":
                return "PAR"
            case "POISON":
                return "PSN"
            case "SLEEP":
                return "SLP"

class Type(Enum):
    NORMAL = auto()
    FIGHTING = auto()
    FLYING = auto()
    POISON = auto()
    GROUND = auto()
    ROCK = auto()
    BUG = auto()
    GHOST = auto()
    STEEL = auto()
    FIRE = auto()
    WATER = auto()
    GRASS = auto()
    ELECTRIC = auto()
    PSYCHIC = auto()
    ICE = auto()
    DRAGON = auto()
    DARK = auto()
    FAIRY = auto()

    def __str__(self) -> str:
        return self.name.title()

class Category(Enum):
    PHYSICAL = auto()
    SPECIAL = auto()
    STATUS = auto()

    def __str__(self) -> str:
        return self.name.title()

class Move(BaseModel):
    name: str
    mv_type: Type
    category: Category | None
    power: int | None
    accuracy: int | None
    pp: int
    effect_msg: str
    effect: Callable | None
    probability: int | None

class Pokemon(BaseModel):
    id: int
    name: str
    gender: Gender
    nature: Nature
    types: Annotated[list[Type | None], Le(2)]
    level: int
    current_exp: int
    exp_for_next_level: int
    moves: Annotated[list[Move | None], Le(4)]
    hp_max: int
    hp_current: int
    attack: int
    defence: int
    special_attack: int
    special_defence: int
    speed: int
    iv: Annotated[list[int], Le(6)]
    ev: Annotated[list[int], Le(6)]
    status: Status
    held_item: Item

