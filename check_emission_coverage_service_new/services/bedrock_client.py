import boto3
import json
from models.check_emission_coverage_request import CheckEmissionCoverageRequest
from models.check_emission_coverage_response import CheckEmissionCoverageResponse, Citation

async def get_coverage_from_bedrock(request: CheckEmissionCoverageRequest) -> CheckEmissionCoverageResponse:
    bedrock_agent = boto3.client("bedrock-agent-runtime")

    input_data = {
        "year": request.year,
        "make": request.make,
        "model": request.model,
        "trim": request.trim,
        "garage_state": request.garage_state,
        "current_mileage": request.current_mileage,
        "parts": request.parts,
        "initial_sale_date": request.initial_sale_date.isoformat(),
        "prompt_id": request.prompt_id,
        "prompt_version": request.prompt_version
    }

    response = bedrock_agent.retrieve_and_generate(
        input=json.dumps(input_data),
        knowledgeBaseId="YOUR_KNOWLEDGE_BASE_ID",
        retrievalConfiguration={"vectorSearchConfiguration": {"numberOfResults": 5}},
        generationConfiguration={"maxTokens": 300, "temperature": 0.7}
    )

    output = json.loads(response["output"])

    return CheckEmissionCoverageResponse(
        warranty_standard=output["warranty_standard"],
        part=output["part"],
        part_category=output["part_category"],
        warranty_coverage=output["warranty_coverage"],
        covered=output["covered"],
        citations=[Citation(**c) for c in output.get("citations", [])],
        notes=output["notes"]
    )
