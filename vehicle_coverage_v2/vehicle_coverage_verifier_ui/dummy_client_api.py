class DummyAPIClient:
    def get_coverage(self, data: dict) -> dict:
        return {
            "covered": "yes",
            "category": "OEM",
            "rules": ["Exhaust Pipe Covered for 7 years"],
            "references": [{"name": "Doc1", "link": "http://google.com"}]
        }
