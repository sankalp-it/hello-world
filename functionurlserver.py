import json

def lambda_handler(event, context):
    print("Event:", event)

    body = event.get('body')
    if body:
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            return {"statusCode": 400, "body": "Invalid JSON"}

        model = data.get('model')
        make = data.get('make')
        model_year = data.get('model_year')

        print("Model:", model)
        print("Make:", make)

        return {
            "statusCode": 200,
            "body": json.dumps({"received_model": model})
        }

    return {
        "statusCode": 400,
        "body": "Missing request body"
    }
