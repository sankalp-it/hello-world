from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import boto3

app = FastAPI()
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VehicleStandards')

class EmissionRequest(BaseModel):
    year: str
    model: str
    state: str

class EmissionResponse(BaseModel):
    emission_standard: str
    vehicle_rules: list
    restriction: str

@app.post("/emission-info", response_model=EmissionResponse)
def get_emission_info(req: EmissionRequest):
    pk = f"VEHICLE#{req.year}#{req.model.upper()}"
    try:
        response = table.get_item(Key={'PK': pk, 'SK': 'STANDARD'})
        item = response.get('Item')
        if not item:
            raise HTTPException(status_code=404, detail="Vehicle not found")

        standards = item.get("standards", {})
        state_key = req.state.upper()
        if state_key not in standards:
            raise HTTPException(status_code=404, detail=f"No emission standard for state {state_key}")
        
        return EmissionResponse(
            emission_standard=standards[state_key],
            vehicle_rules=item.get("vehicle_rules", []),
            restriction=item.get("restriction", "")
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
