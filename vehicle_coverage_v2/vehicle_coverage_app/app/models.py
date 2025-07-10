from pydantic import BaseModel
from typing import List

class VehicleRepair(BaseModel):
    year: int
    make: str
    model: str
    trim: str
    current_mileage: int
    parts: List[str]
    initial_sale_date: str
    has_vpp_coverage: bool

class CoverageReference(BaseModel):
    name: str
    link: str

class CoverageResponse(BaseModel):
    covered: str
    category: str
    rules: List[str]
    references: List[CoverageReference]
