"""
Download Cincinnati Police Department data from the city's open data portal.
"""

import json
from os import path

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

# Download 2010 crime data and convert to DataFrame
# API endpoint:
# https://data.cincinnati-oh.gov/resource/4qzi-nepn.json
CRIMES = pd.DataFrame(CLIENT.get(
    '4qzi-nepn',
    where='occurredon between "2010-01-01T00:00:00" and "2010-12-31T23:59:59"',
    order='occurredon ASC',
    # Manually upping limit so data isn't truncated
    limit='50000'
))
CLIENT.close()

# Write to file
CRIMES.to_csv(path.join(DIR, 'crimes_raw.csv'), index=False)
