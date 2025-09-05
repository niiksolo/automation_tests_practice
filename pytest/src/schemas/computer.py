from pydantic import BaseModel, HttpUrl, UUID4, EmailStr
from pydantic.types import  PastDate, FutureDate , PaymentCardNumber
from pydantic.networks import IPv4Address, IPv6Address
from pydantic.color import Color
from typing import List
#from examples import computer
from src.enums.user_enums import Statuses

class Physical(BaseModel):
    color: Color
    photo: HttpUrl
    uuid: UUID4

class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr

class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]


class Computer(BaseModel):
    status: Statuses
    activated_at:  PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo

comp = Computer.model_validate(computer)
print(comp)