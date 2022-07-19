from core.query import Query
from datetime import datetime
import pandas as pd
import json
import time

class NordvikEkstraEstatesQuery(Query):

    def __init__(self, dateFrom):
        super().__init__('Reading NE estates', '...')
        self.dateFrom = dateFrom

    def execute(self):

        # start_date_mongo = self.dateFrom
        
        estates_df = pd.read_excel('queries/nordvikekstra/data/ne_data.xlsx', sheet_name='Oversikt Test')
        estates_df.to_json(r'queries/nordvikekstra/data/ne_estates.json', orient='records', default_handler=str)

        return True