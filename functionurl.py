import boto3
import requests
from requests_aws4auth import AWS4Auth

# Get current AWS session (uses your SSO or environment credentials)
session = boto3.Session()
credentials = session.get_credentials().get_frozen_credentials()

region = 'us-east-1'  # <-- replace with your region
service = 'lambda'
url = "https://abcd1234.lambda-url.us-east-1.on.aws/"  # <-- your function URL

auth = AWS4Auth(credentials.access_key,
                credentials.secret_key,
                region,
                service,
                session_token=credentials.token)

payload = {"message": "hello from federated user"}

response = requests.post(url, json=payload, auth=auth)
print("Status:", response.status_code)
print("Response:", response.text)
