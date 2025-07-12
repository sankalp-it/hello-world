from parser import VehicleStandardsParser
import os


class TestVehicleStandardsParser:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def run(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        parser = VehicleStandardsParser(content)
        results = []

        for record in parser.parse():
            result = record.as_dict()
            results.append(result)
            print("Parsed Record:")
            print(result)

        return results


if __name__ == "__main__":
    file_path = os.path.join("testdata", "sample_vehicle_data.txt")
    tester = TestVehicleStandardsParser(file_path)
    tester.run()
