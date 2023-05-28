from pydantic import BaseModel

class Modem(BaseModel):
    id: int
    brand: str
    capacity: str
    antenna: str
    cost: float