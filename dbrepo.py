import boto3
from typing import Dict


class MYEmissionWarrantyRuleRepository:
    def __init__(self, table_name: str):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)

    def _build_pk(self, standards_year: str, model_year: str, model: str) -> str:
      return f'MY{standards_year}#{model_year}#{model.upper()}'
      
  def insert_vehicle_entry(self, entry: dict):
      entry['PK'] = self._build_pk(entry['standards_year'],entry['model_year'], entry['model'])
      self.table.put_item(Item=entry)

  def get_emission_standard(self, standards_year: str, model_year: str, model: str) -> Dict:
      pk = self._build_pk(standards_year, model_year, model)
      response = self.table.get_item(Key={'PK': pk})
      return response.get('Item', {})






