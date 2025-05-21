from pydantic import BaseModel


class Character(BaseModel):
    personName: str
    endurance: int
    health: int
    armor: float
    gold_value: int
    strength: str
    agility: str
    intelligence: str
    sex: str
    race: str
    married: bool
    partner_id: str
    inventory: list
