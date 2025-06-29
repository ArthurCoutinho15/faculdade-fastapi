from pydantic import BaseModel as SCBaseModel
from typing import Optional

class CursoSchema(SCBaseModel):
    id: Optional[int]
    titulo: str
    aulas: int 
    horas: int
    
    class Config:
        orm_mode = True
    
    
    