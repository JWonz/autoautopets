import json
import requests
from datetime import datetime
import os
import glob


def save_locally(data):
    # Get the current timestamp
    datestamp = datetime.now().strftime('%Y%m%d')

    # Construct the file name using the timestamp
    file_name = f"./data/sap_{datestamp}.json"

    # Open the file in write mode
    with open(file_name, 'w') as f:
        # Write the data to the file as JSON
        json.dump(data, f)


def read_most_recent_json(directory):
    # Get a list of all the files in the directory
    file_list = glob.glob(os.path.join(directory, '*.json'))

    # Sort the list of files by modification time
    file_list.sort(key=os.path.getmtime)

    # Get the most recent file
    most_recent_file = file_list[-1]

    # Open the most recent file in read mode
    with open(most_recent_file, 'r') as f:
        # Read the contents of the file
        contents = json.load(f)

    # Return the contents of the file
    return contents


def get_superautopet_com():
    response = requests.get('https://superauto.pet/api.json')

    if response.status_code == 200:
        # Load the JSON data from the response
        data = response.json()

        # Now you can access the data in the JSON file
        print(data)
        save_locally(data)


if __name__ == '__main__':
    get_superautopet_com()
