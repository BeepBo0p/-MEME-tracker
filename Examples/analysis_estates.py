from core.query import Query
from datetime import datetime
import pandas as pd
import json
import requests
import time

class NordvikEkstraAnalysis(Query):

    def __init__(self):
        super().__init__('Reading All and NE estates', '...')

    def execute(self):

        # returns JSON object as a Dataframe
        all_estates_df = pd.read_json('queries/nordvikekstra/data/all_estates.json', orient='records')
        ne_estates_df = pd.read_json('queries/nordvikekstra/data/ne_estates.json', orient='records')

        ne_estates_filtered_df = pd.DataFrame(all_estates_df[all_estates_df['assignmentNum'].isin(ne_estates_df['Oppdrag'])])
        not_ne_estates_filtered_df = pd.DataFrame(all_estates_df[~all_estates_df['assignmentNum'].isin(ne_estates_df['Oppdrag'])])

        # print(all_estates_df['estateId'].count())
        # print(ne_estates_filtered_df['estateId'].count())
        # print(ne_estates_df['Oppdrag'].count())
        # print(not_ne_estates_filtered_df['estateId'].count())
        

        # Calling the API
        base_url = 'https://hub.megler.vitec.net/MSNOP'
        username = 'inceptech'
        password = 'uLHhdVxl3lw3kZJ9UxMdSmNQvtTNYffWzLEYtEsh3CcLZFvvxT'
        # estateId = 'D4115C4E-ADD7-47AA-A4E7-72D1AB0C6ACC'

        count_ne_viewing = 0
        count_ne_interested = 0
        count_ne_estates = ne_estates_filtered_df['estateId'].count()

        count_not_ne_viewing = 0
        count_not_ne_interested = 0
        count_not_ne_estates = not_ne_estates_filtered_df['estateId'].count()


        # NE estates
        for estateId in ne_estates_filtered_df['estateId']: 
            url = base_url + '/Estates/' + estateId + '/ContactRelations'
            
            response_viewing = requests.get(url, auth=(username, password), params={'relationType': 0})
            response_interested = requests.get(url, auth=(username, password), params={'relationType': 1})

            print(response_viewing.json()['contacts'])
            print(response_interested.json()['contacts'])
            print()

        #     count_ne_viewing += len(response_viewing.json()['contacts'])
        #     count_ne_interested += len(response_interested.json()['contacts'])
            
        
        # # Not NE estates
        # for estateId in not_ne_estates_filtered_df['estateId']: 
        #     url = base_url + '/Estates/' + estateId + '/ContactRelations'
            
        #     response_viewing = requests.get(url, auth=(username, password), params={'relationType': 0})
        #     response_interested = requests.get(url, auth=(username, password), params={'relationType': 1})

        #     count_not_ne_viewing += len(response_viewing.json()['contacts'])
        #     count_not_ne_interested += len(response_interested.json()['contacts'])

        # average_ne_viewing = count_ne_viewing / count_ne_estates
        # average_ne_interested = count_ne_interested / count_ne_estates

        # average_not_ne_viewing = count_not_ne_viewing / count_not_ne_estates
        # average_not_ne_interested = count_not_ne_interested / count_not_ne_estates

        # print()
        # print('Antall visningsdeltakere med NE: ' + count_ne_viewing)
        # print('Antall interessenter med NE: ' + count_ne_interested)
        # print('Antall boliger med NE: ' + count_ne_estates)
        # print()
        # print('Antall visningsdeltakere med NE: ' + count_not_ne_viewing)
        # print('Antall interessenter med NE: ' + count_not_ne_interested)
        # print('Antall boliger med NE: ' + count_not_ne_estates)
        # print()
        # print()
        # print('Average antall visningsdeltakere med NE: ' + average_ne_viewing)
        # print('Average antall visningsdeltakere uten NE: ' + average_not_ne_viewing)
        # print()
        # print('Average antall interessenter med NE: ' + average_ne_interested)
        # print('Average antall interessenter uten NE: ' + average_not_ne_interested)
        # print()


        # # contacts1 = response1.json()['contacts']
        # # contacts2 = response2.json()['contacts']
        # # contacts3 = response3.json()['contacts']

        # # # print(response.status_code)
        # # print(len(contacts1))
        # # print(len(contacts2))
        # # print(len(contacts3))

        # return True















# Matching estates
# All estates: assignmentNum
# NE estates: Oppdrag