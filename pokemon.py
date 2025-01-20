from dataclasses import dataclass
from enum import Enum, auto
from items import Item

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

class MoveEffect(Enum):
    ONE_KO = auto()

@dataclass
class Move:
    name: str
    mv_type: Type
    category: Category | None
    power: int | None
    accuracy: int | None
    pp: int
    effect_msg: str
    effect: MoveEffect | None
    probability: int | None

@dataclass
class Exp:
    current: int
    for_next_level: int

@dataclass
class Hp:
    base: int
    max: int
    current: int

@dataclass
class Stat:
    base: int
    current: int

@dataclass
class Stats:
    hp: int
    attack: int
    defence: int
    special_attack: int
    special_defence: int
    speed: int

@dataclass
class Pokemon:
    id: int
    name: str
    gender: Gender
    nature: Nature
    types: list[Type | None]
    level: int
    exp: Exp
    moves: list[Move | None]
    hp: Hp
    attack: Stat
    defence: Stat
    special_attack: Stat
    special_defence: Stat
    speed: Stat
    iv: Stats
    ev: Stats
    status: Status
    held_item: Item

