from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class CheckEmissionCoverageRequest(BaseModel):
    year: int
    make: str
    model: str
    trim: Optional[str]
    garage_state: str
    current_mileage: int
    parts: List[str]
    initial_sale_date: date
    prompt_id: str
    prompt_version: str
