from fastapi import APIRouter, Query
from typing import List
from app.models import VehicleRepair, CoverageResponse
# from app.services.bedrock_coverage_provider import BedrockCoverageProvider
from app.services.dummy_provider import DummyCoverageProvider

router = APIRouter()
# provider = BedrockCoverageProvider()
provider = DummyCoverageProvider()

@router.get("/coverage", response_model=CoverageResponse)
async def get_coverage(
    year: int,
    make: str,
    model: str,
    trim: str,
    current_mileage: int,
    parts: List[str] = Query(...),
    initial_sale_date: str = "",
    has_vpp_coverage: bool = False,
):
    repair = VehicleRepair(
        year=year,
        make=make,
        model=model,
        trim=trim,
        current_mileage=current_mileage,
        parts=parts,
        initial_sale_date=initial_sale_date,
        has_vpp_coverage=has_vpp_coverage
    )
    return await provider.get_coverage(repair)
