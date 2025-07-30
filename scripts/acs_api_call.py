import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv() # Load .env file into environment variables

API_KEY = os.getenv("CENSUS_API_KEY")
BASE_URL = "https://api.census.gov/data/2023/acs/acs5"
PARAMS = {
    "get": "NAME, B01003_001E, B19013_001E, B08201_002E, B08006_001E, B08006_002E, B08006_008E", # total pop, med household income, num households w/ no vehicles
    "for": "tract:*",
    "in": "state:06 county:073",
    "key": API_KEY
}

response = requests.get(BASE_URL, params=PARAMS)
data = response.json()

df = pd.DataFrame(data[1:], columns=data[0])
df.to_csv("data/processed/census_acs_2023.csv", index=False)
print("Saved census data.")