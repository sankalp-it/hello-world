import re
from typing import List, Dict, Generator


class VehicleEmissionEntry:
    def __init__(self, year: str, make: str, model: str, model_rules: List[str],
                 model_year_rules: List[str], standards_map: Dict[str, str]):
        self.year = year
        self.make = make
        self.model = model
        self.model_rules = model_rules
        self.model_year_rules = model_year_rules
        self.standards_map = standards_map

    def as_dict(self):
        return {
            "year": self.year,
            "make": self.make,
            "model": self.model,
            "model_rules": self.model_rules,
            "model_year_rules": self.model_year_rules,
            "standards_map": self.standards_map
        }


class VehicleStandardsParser:
    def __init__(self, content: str):
        self.lines = content.strip().splitlines()
        self.states = []

    def parse(self) -> Generator[VehicleEmissionEntry, None, None]:
        for idx, line in enumerate(self.lines):
            parts = line.strip().split("~")

            if idx == 0:
                # Header line
                self.states = parts[3:]
                continue

            year, model_field, model_year_rule = parts[0], parts[1], parts[2]
            standards_raw = parts[3:]

            model_entries = [entry.strip() for entry in model_field.split(',')]
            standards_map = dict(zip(self.states, standards_raw))

            for model_entry in model_entries:
                model_name, model_rules = self._extract_model_and_rules(model_entry)
                yield VehicleEmissionEntry(
                    year=year,
                    make="",  # make is not in the file now, placeholder for later
                    model=model_name,
                    model_rules=model_rules,
                    model_year_rules=[model_year_rule] if model_year_rule else [],
                    standards_map=standards_map
                )

    def _extract_model_and_rules(self, entry: str):
        """
        Extract model name and rule indicators (e.g., *1, *2) from model string.
        "PRIUS PHV *1,*2" -> ("PRIUS PHV", ["*1", "*2"])
        """
        parts = entry.strip().split()
        model_parts = []
        rules = []

        for part in parts:
            if "," in part:
                subparts = [x.strip() for x in part.split(",")]
                for sp in subparts:
                    if re.match(r"\*\d+", sp):
                        rules.append(sp)
            elif re.match(r"\*\d+", part):
                rules.append(part)
            else:
                model_parts.append(part)

        model_name = " ".join(model_parts).strip(",")
        return model_name, list(set(rules))
