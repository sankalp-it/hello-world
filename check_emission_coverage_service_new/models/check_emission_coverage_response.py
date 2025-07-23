from pydantic import BaseModel
from typing import List

class Citation(BaseModel):
    document_name: str
    page_no: int
    link: str

class CheckEmissionCoverageResponse(BaseModel):
    warranty_standard: str
    part: str
    part_category: str
    warranty_coverage: str
    covered: bool
    citations: List[Citation]
    notes: str
