import requests
import boto3
import json
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from models.check_emission_coverage_response import CheckEmissionCoverageResponse

async def enrich_with_lambda_data(response: CheckEmissionCoverageResponse) -> CheckEmissionCoverageResponse:
    session = boto3.session.Session()
    credentials = session.get_credentials()
    region = session.region_name
    lambda_url = "https://your-lambda-function-id.lambda-url.region.on.aws/"

    req = AWSRequest(
        method="POST",
        url=lambda_url,
        data=json.dumps(response.dict()),
        headers={"Content-Type": "application/json"}
    )

    SigV4Auth(credentials, "lambda", region).add_auth(req)
    signed_headers = dict(req.headers)

    result = requests.post(lambda_url, headers=signed_headers, data=req.body)

    if result.status_code == 200:
        enriched_data = result.json()
        return CheckEmissionCoverageResponse(**enriched_data)
    else:
        raise Exception(f"Lambda call failed: {result.status_code} {result.text}")
