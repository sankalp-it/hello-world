from models.check_emission_coverage_response import CheckEmissionCoverageResponse, Citation
from models.check_emission_coverage_request import CheckEmissionCoverageRequest
from services.bedrock_client import get_coverage_from_bedrock
from services.lambda_client import enrich_with_lambda_data
import pytest
import asyncio
from datetime import date

@pytest.mark.asyncio
async def test_get_coverage_from_bedrock_mock(monkeypatch):
    async def mock_bedrock_client(request: CheckEmissionCoverageRequest) -> CheckEmissionCoverageResponse:
        return CheckEmissionCoverageResponse(
            warranty_standard="3yr/36k",
            part="Catalytic Converter",
            part_category="Emission",
            warranty_coverage="Partial",
            covered=True,
            citations=[Citation(document_name="TestDoc", page_no=1, link="http://example.com")],
            notes="Mocked Bedrock response"
        )
    monkeypatch.setattr("services.bedrock_client.get_coverage_from_bedrock", mock_bedrock_client)

    request = CheckEmissionCoverageRequest(
        year=2021,
        make="Honda",
        model="Civic",
        trim="EX",
        garage_state="CA",
        current_mileage=15000,
        parts=["Catalytic Converter"],
        initial_sale_date=date(2021, 1, 1),
        prompt_id="test123",
        prompt_version="v1"
    )

    response = await get_coverage_from_bedrock(request)
    assert response.part == "Catalytic Converter"
    assert response.covered is True
    assert "Mocked" in response.notes

@pytest.mark.asyncio
async def test_enrich_with_lambda_data_mock(monkeypatch):
    async def mock_lambda_client(resp: CheckEmissionCoverageResponse) -> CheckEmissionCoverageResponse:
        resp.notes += " | Enriched"
        return resp
    monkeypatch.setattr("services.lambda_client.enrich_with_lambda_data", mock_lambda_client)

    response = CheckEmissionCoverageResponse(
        warranty_standard="3yr/36k",
        part="Sensor",
        part_category="Emission",
        warranty_coverage="Full",
        covered=True,
        citations=[],
        notes="Original"
    )

    enriched = await enrich_with_lambda_data(response)
    assert "Enriched" in enriched.notes
