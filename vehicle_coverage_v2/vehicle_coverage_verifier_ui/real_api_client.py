import requests

class RealAPIClient:
    def __init__(self, base_url: str = "http://localhost:8000", endpoint_path: str = "/api/coverage"):
        self.base_url = base_url.rstrip("/")
        self.endpoint_path = endpoint_path.lstrip("/")

    def get_coverage(self, data: dict) -> dict:
        url = f"{self.base_url}/{self.endpoint_path}"
        try:
            response = requests.get(url, params=data, timeout=5)  # timeout to avoid hanging
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return {
                "error": "HTTPError",
                "message": f"Server returned an error: {http_err}",
                "status_code": response.status_code if response else "N/A"
            }
        except requests.exceptions.ConnectionError:
            return {
                "error": "ConnectionError",
                "message": f"Could not connect to {url}. Is the server running?"
            }
        except requests.exceptions.Timeout:
            return {
                "error": "TimeoutError",
                "message": f"Request to {url} timed out."
            }
        except requests.RequestException as e:
            return {
                "error": "RequestException",
                "message": str(e)
            }
