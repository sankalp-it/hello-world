import boto3
import json

class BedrockKnowledgeBaseClient:
    def __init__(self):
        self.client = boto3.client("bedrock-agent-runtime", region_name="us-east-1")
        self.kb_id = "your-knowledge-base-id"

    def query_knowledge_base(self, prompt: str):
        response = self.client.retrieve_and_generate(
            input={"text": prompt},
            retrieveAndGenerateConfiguration={
                "type": "KNOWLEDGE_BASE",
                "knowledgeBaseConfiguration": {
                    "knowledgeBaseId": self.kb_id,
                    "modelArn": "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-sonnet"
                }
            }
        )
        output_text = response["output"]["text"]
        return json.loads(output_text)
