from pydantic import BaseModel

class Prompt(BaseModel):
    prompt_id: str
    prompt_text: str

class PromptRequest(BaseModel):
    prompt_text: str

class PromptResponse(BaseModel):
    prompt_id: str
    prompt_text: str
