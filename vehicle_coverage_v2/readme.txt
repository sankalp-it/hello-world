Notes
✅ 1. Set Up AWS Credentials
Bedrock access uses standard AWS credentials via IAM.
Options:
* Environment variables (dev/local): bash CopyEdit   export AWS_ACCESS_KEY_ID=your_access_key
* export AWS_SECRET_ACCESS_KEY=your_secret_key
* export AWS_DEFAULT_REGION=us-east-1
*   
* AWS config file (~/.aws/credentials) ini CopyEdit   [default]
* aws_access_key_id = your_access_key
* aws_secret_access_key = your_secret_key
*   
* IAM Role (production/EC2/EKS): Use a role with bedrock:InvokeModel permission.

✅ 2. Install Required SDK
Bedrock uses Boto3 (or LangChain, BedrockAgent, etc.).
bash
CopyEdit
pip install boto3

✅ 3. Grant Required IAM Permissions
Attach a policy like:
json
CopyEdit
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:ListFoundationModels"
      ],
      "Resource": "*"
    }
  ]
}
Use a scoped resource ARN for production.

✅ 4. Example: FastAPI Client for Bedrock
python
CopyEdit
import boto3

class BedrockClient:
    def __init__(self, region="us-east-1", model_id="anthropic.claude-3-sonnet-20240229-v1:0"):
        self.client = boto3.client("bedrock-runtime", region_name=region)
        self.model_id = model_id

    def invoke(self, prompt: str) -> str:
        body = {
            "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
            "max_tokens_to_sample": 300,
            "temperature": 0.7,
        }

        response = self.client.invoke_model(
            body=bytes(str(body), encoding="utf-8"),
            modelId=self.model_id,
            contentType="application/json",
            accept="application/json",
        )
        result = response["body"].read().decode("utf-8")
        return result

✅ 5. Wire it in FastAPI
python
CopyEdit
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
bedrock_client = BedrockClient()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/bedrock/invoke")
def get_completion(req: PromptRequest):
    result = bedrock_client.invoke(req.prompt)
    return {"result": result}

✅ 6. Test
bash
CopyEdit
curl -X POST http://localhost:8000/bedrock/invoke \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is Bedrock in AWS?"}'

Would you like me to:
* Generate a bedrock_client.py file?
* Add it into your FastAPI backend project with a working endpoint?
* Create a zip or Docker setup for that too?
Let me know!



✅ 1. Grant AWS Credentials Inside the Container
🔹 Option A: Use Environment Variables (For Local Dev)
Update your docker-compose.yml for the backend service:
yaml
CopyEdit
version: "3.9"

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      AWS_ACCESS_KEY_ID: "${AWS_ACCESS_KEY_ID}"
      AWS_SECRET_ACCESS_KEY: "${AWS_SECRET_ACCESS_KEY}"
      AWS_DEFAULT_REGION: "us-east-1"
Then in your local .env file or shell:
bash
CopyEdit
export AWS_ACCESS_KEY_ID=your-access-key
export AWS_SECRET_ACCESS_KEY=your-secret-key
export AWS_DEFAULT_REGION=us-east-1
Or use a .env file and set env_file: .env in your docker-compose.yml.

🔹 Option B: Use Volume Mount for ~/.aws/credentials
If you want to pass your full AWS config into the container:
yaml
CopyEdit
volumes:
  - ~/.aws:/root/.aws:ro
Be careful with permissions — this is great for dev, but not ideal for production.

✅ 2. Minimal docker-compose.yml Example
yaml
CopyEdit
version: "3.9"

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      AWS_ACCESS_KEY_ID: "${AWS_ACCESS_KEY_ID}"
      AWS_SECRET_ACCESS_KEY: "${AWS_SECRET_ACCESS_KEY}"
      AWS_DEFAULT_REGION: "us-east-1"

  frontend:
    build: ./vehicle_coverage_verifier_ui
    ports:
      - "8501:8501"
    environment:
      BASE_URL: "http://backend:8000"
      ENDPOINT_PATH: "/api/coverage"
Now frontend talks to backend, and backend talks to AWS Bedrock.

✅ 3. Best Practices for Production
* Use IAM Roles for Service Accounts on EKS or ECS.
* Avoid hardcoding secrets — use AWS Secrets Manager or environment injection from CI/CD.
* Avoid mounting your local .aws directory in production.

Would you like me to:
* Generate the full docker-compose.yml for your frontend + backend + AWS Bedrock call?
* Add .env handling and .dockerignore?
