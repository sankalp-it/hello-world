from app.models import VehicleRepair, CoverageResponse, CoverageReference
from app.services.coverage_interface import CoverageProvider

class DummyCoverageProvider(CoverageProvider):
    async def get_coverage(self, repair: VehicleRepair) -> CoverageResponse:
        return CoverageResponse(
            covered="yes",
            category="OEM",
            rules=["Exhaust Pipe Covered for 7 years"],
            references=[
                CoverageReference(name="Doc1", link="http://google.com")
            ]
        )
