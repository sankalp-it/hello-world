from fastapi import APIRouter
from models.check_emission_coverage_request import CheckEmissionCoverageRequest
from models.check_emission_coverage_response import CheckEmissionCoverageResponse
from services.bedrock_client import get_coverage_from_bedrock
from services.lambda_client import enrich_with_lambda_data

router = APIRouter()

@router.post("/coverage", response_model=CheckEmissionCoverageResponse)
async def check_coverage(request: CheckEmissionCoverageRequest):
    bedrock_response = await get_coverage_from_bedrock(request)
    final_response = await enrich_with_lambda_data(bedrock_response)
    return final_response
