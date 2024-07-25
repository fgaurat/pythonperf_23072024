from dataclasses import dataclass

@dataclass
class Customer:
    id:int=0
    firstName:str=""
    lastName:str=""
    email:str=""
    gender:str=""
    ipAddress:str=""