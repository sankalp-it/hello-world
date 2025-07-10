from fastapi import APIRouter, HTTPException
from app.models.prompt_model import PromptRequest, PromptResponse
from app.services.dynamo_client import save_prompt, get_prompt
import uuid

router = APIRouter()

@router.post("/prompt", response_model=PromptResponse)
def create_prompt(request: PromptRequest):
    prompt_id = str(uuid.uuid4())
    save_prompt(prompt_id, request.prompt_text)
    return PromptResponse(prompt_id=prompt_id, prompt_text=request.prompt_text)

@router.get("/prompt/{prompt_id}", response_model=PromptResponse)
def read_prompt(prompt_id: str):
    item = get_prompt(prompt_id)
    if not item:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return PromptResponse(**item)
