# This is super mega temp script. Will be removed and merged later

import os
import requests
import csv

import pandas as pd

from tqdm import tqdm
from io import StringIO
from os import getcwd
from input import getTickerInput
from dotenv import load_dotenv
from randomdate import randome_range
from datetime import datetime, timedelta

# Load env variables
load_dotenv()

# Get the api key and url
API_KEY = os.getenv('API_KEY')
URL = os.getenv('URL')

name = input("Model / ticker name:")

path = getcwd() + "\\workspace\\dat\\"
if not os.path.exists(path):
    os.makedirs(path)

for i in tqdm(range(0, 1)):
    date = datetime.now()
    querystring = {"format":'csv',"api_key":API_KEY, "start_date": date - timedelta(days=6), "end_date": date -  timedelta(hours=1),'interval': 'hourly', 'period': '1', 'currency': name}

    response = requests.get(URL + '/timeseries', params=querystring)
    #print(response.text)

    if response.ok == True:
        df = pd.read_csv(StringIO(response.text), sep=",")

        ## Write API Results to CSV
        df.to_csv(path + "dat_" + name + ".csv", index=False, sep=',', encoding='utf-8')

        pass
    else:
        break

# Display error to be sure
if response.ok == False:
    print("Cannot retrieve data [" + str(response.status_code) + "]. Exiting.")
    print(response.text)
    exit()