import os
import requests
from zipfile import ZipFile
from io import BytesIO

GTFS_URL = "http://www.sdmts.com/google_transit_files/google_transit.zip"
DEST_DIR = "data/raw"


def download_gtfs_data():
    os.makedirs(DEST_DIR, exist_ok=True)
    zip_path = os.path.join(DEST_DIR, "google_transit.zip")
    
    if not os.path.exists(zip_path):
        print("Downloading GTFS data...")
        response = requests.get(GTFS_URL)
        if response.status_code == 200:
            with open(zip_path, 'wb') as f:
                f.write(response.content)
            print("GTFS data has been downloaded.")
            
            with ZipFile(BytesIO(response.content)) as zip_ref:
                zip_ref.extractall(DEST_DIR)
            print("Extracted to", DEST_DIR)
        else:
            print("Failed to download. Status code:", response.status_code)
    else:
        print("GTFS zip already exists.")

if __name__ == "__main__":
    download_gtfs_data()