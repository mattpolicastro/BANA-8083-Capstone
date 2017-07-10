"""
Download Cincinnati Police Department data from the city's open data portal.
"""

import json
from os import path
import sys

import pandas as pd
from sodapy import Socrata

# Import the config file
DIR = path.dirname(__file__)
CONFIG_FILE = open(path.join(DIR, 'socrata.json'))
CONFIG = json.load(CONFIG_FILE)
CONFIG_FILE.close()

# Start API client session
CLIENT = Socrata(
    'data.cincinnati-oh.gov',
    CONFIG['app_token'],
    CONFIG['username'],
    CONFIG['password']
)


YEAR = str(sys.argv[1])
DATE_RANGE = '"' + YEAR +'-01-01T00:00:00" and "' + YEAR + '-12-31T23:59:59"'

# Download 2010 crime data and convert to DataFrame
# API endpoint:
# https://data.cincinnati-oh.gov/resource/4qzi-nepn.json
CRIMES = pd.DataFrame(CLIENT.get(
    '4qzi-nepn',
    where='reportedon between ' + DATE_RANGE + ' AND occurredon between ' + DATE_RANGE,
    order='reportedon ASC',
    # Manually upping limit so data isn't truncated
    limit='50000'
))
CLIENT.close()

# Write to file
CRIMES.to_csv(path.join(DIR, 'raw', 'crimes_raw_' + YEAR + '.csv'), index=False)
