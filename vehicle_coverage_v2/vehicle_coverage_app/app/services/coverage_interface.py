from abc import ABC, abstractmethod
from app.models import VehicleRepair, CoverageResponse

class CoverageProvider(ABC):
    @abstractmethod
    async def get_coverage(self, repair: VehicleRepair) -> CoverageResponse:
        pass
