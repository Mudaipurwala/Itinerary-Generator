#!/usr/bin/env
"""
Genearates and Formats Data from API's
Produces CSV Files based on Config Inputs
"""
import os
import logging

import yaml
import requests
import coloredlogs
import pandas as pd

logging.basicConfig(level=logging.INFO)
coloredlogs.install()


class CreateItinerary:

    def __init__(self, url, headers, params):
        self.url = url
        self.headers = headers
        self.params = params
        self.path = os.path.dirname(os.path.realpath(__file__))

    def data_generator(self):
        """Generates a response from API based on Attributes

        Args:
            url (str): url of the specified API
            headers (dict): headers for the specified API

        Returns:
            [json]: API Response
        """
        try:
            logging.info("Requesting Data from API...")
            response = requests.get(
                self.url,
                headers=self.headers,
                params=self.params
            )
            response_result = response.json()
        except Exception as e:
            logging.error(
                "Error processing your API request: {}".format(e)
            )
        else:
            return response_result

    def data_formatter(self, response, records, columns, names):
        """Normalizes semi-structured JSON data into a flat table
        and formats data based on arguments

        Args:
            response (str): JSON response
            records (str): JSON API Primary Key in config file
            columns (dict): API response keys in config file
            names (dict): API column names in config file

        Returns:
            [Dataframe]: Returns a cleaned version of the Dataframe
        """

        data = pd.json_normalize(response[str(records)])
        data = data.reindex(columns=columns)
        data.rename(
            columns=names,
            inplace=True
        )
        logging.info(
            "Generating Data from API..."
        )

        return data

    def file_generator(self, data_list):
        """Generates CSV files from Config inputs

        Args:
            data_list (list): Input sub of Config File

        Returns:
            [csv file]: Returns a CSV file for each list input
        """

        for item in data_list:

            response = self.data_generator()

            if item == 'LOCATION':

                loc_id = response["location_suggestions"][0]["id"]
                data['API_PARAMS']['FOOD']['entity_id'] = str(loc_id)

                with open('config.yaml', 'w') as f:
                    yaml.dump(data, f)
                    break

            results = self.data_formatter(
                response=response,
                records=data['API_HOLDER'][item],
                columns=data['API_FIELDS'][item],
                names=data['API_COL_NAMES'][item]
            )

            logging.info(
                "CSV file has been generated for: {}".format(item)
            )

            return results.to_csv(
                self.path+'/{}.csv'.format(item),
                index=None,
                header=True
            )


if __name__ == '__main__':

    location = input("Please enter the name of a city: ")

    with open('config.yaml', "r") as file_decriptor:
        data = yaml.safe_load(file_decriptor)

    data['API_PARAMS']['POI']['location_id'] = location
    data['API_PARAMS']['LOCATION']['q'] = location
    data['API_PARAMS']['WEATHER']['q'] = location

    with open('config.yaml', 'w') as f:
        yaml.dump(data, f)

    itinerary_info = [
        'POI',
        'LOCATION',
        'FOOD',
        'WEATHER'
    ]

    for info in itinerary_info:

        CreateItinerary(
                url=data['API_URLS'][info],
                headers=data['API_HEADERS'][info],
                params=data['API_PARAMS'][info],
            ).file_generator([info])
