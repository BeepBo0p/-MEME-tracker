from email.policy import default
from core.query import Query
from datetime import datetime
import pandas as pd
import json
import time

class AllEstatesQuery(Query):

    def __init__(self, dateFrom):
        super().__init__('Reading all estates', '...')
        self.dateFrom = dateFrom
        #self.dateTo = dateTo

    def execute(self):

        start_date_mongo = self.dateFrom
        #end_date_mongo = self.dateTo

        estates = self.mongodb_source.connection.estates.find(
                { "$or": [
                    { "soldDate": { "$gte": start_date_mongo }, "showings": { "$size": 0 } },
                    { "soldDate": { "$gte": start_date_mongo }, "showings": { "$size": 1 } }
                ] }
        )

        print(len(list(estates.clone())))

        estates_df = pd.DataFrame(estates.clone())
        estates_df.to_json(r'queries/nordvikekstra/data/all_estates.json', orient='records', default_handler=str)

        return True