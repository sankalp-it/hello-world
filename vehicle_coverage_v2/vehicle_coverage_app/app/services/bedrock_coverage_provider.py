from app.models import VehicleRepair, CoverageResponse
from app.services.coverage_interface import CoverageProvider
from app.services.bedrock_client import BedrockKnowledgeBaseClient

class BedrockCoverageProvider(CoverageProvider):
    def __init__(self):
        self.client = BedrockKnowledgeBaseClient()

    async def get_coverage(self, repair: VehicleRepair) -> CoverageResponse:
        prompt = f"""
        Given the following vehicle repair request, provide whether it's covered,
        the category, rules that apply, and documentation references.

        Input JSON:
        {repair.json()}

        Output format:
        {{
          "covered": "yes/no",
          "category": "OEM/Aftermarket",
          "rules": ["Rule text..."],
          "references": [{{"name": "Doc1", "link": "http://..."}}]
        }}
        """
        response_json = self.client.query_knowledge_base(prompt)
        return CoverageResponse(**response_json)
