import argparse
import yaml
import requests
import os
import tqdm
from concurrent.futures import ThreadPoolExecutor


#some useful functions
def build_files_to_download(configurations):
    """
    Constructs a list of files to be downloaded based on the provided configurations.

    Args:
    - configurations (dict): A dictionary containing configuration parameters:
        - 'first_year_gas' (str): The starting year for gas data.
        - 'last_year_gas' (str): The last year for gas data.
        - 'year_station_file' (str): The year for station file.
        - 'year_service_file' (str): The year for service file.

    Returns:
    - list: A list of file names to be downloaded.
    """

    
    files = list(map(lambda i: f'Prix{i}.csv.gz',
                     list(range(
                         configurations['first_year_gas'],
                         configurations['last_year_gas']+1))))
    files.append(f'Stations{configurations["year_station_file"]}.csv.gz')
    files.append(f'Services{configurations["year_service_file"]}.csv.gz')
    files.remove('Prix2022.csv.gz')
    files.append('Prix2022S2.csv.gz')
    files.append('Prix2022S1.csv.gz')
    return files



def download_file(file):
    """
    Downloads a file from a specified URL and saves it to a designated location.

    Args:
    - file (str): The name of the file to be downloaded.
    - configurations (dict): A dictionary containing configuration parameters:
        - 'base_url' (str): The base URL for the file download.
        - 'base_data_location' (str): The base location to save downloaded files.

    Returns:
    - None

    Raises:
    - Exception: If the download fails, an exception is raised.

    Note:
    Ensure that the 'requests' library is installed to use this function for making HTTP requests.
    """

    # Hint: Consider how the function constructs the URL and destination path using the provided configurations.
    # Look for the usage of 'base_url' and 'base_data_location' to form the complete URL and file path.
    # Pay attention to the 'requests' library usage to make an HTTP request and save the downloaded content.
    base_url = configurations['base_url']
    destination_path = configurations['base_data_location']
    url = base_url + file
    try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(destination_path + file, 'wb') as f:
                    f.write(response.content)
                    print(f'Successfully downloaded {file}')
    except Exception:
            print(f'Failed to download {file}')



argparser = argparse.ArgumentParser(
prog="This program donwloads the required data for the project from a github repository"
)

#added a the config file as a required argument
argparser.add_argument("-c", "--config", required=True, type=str, help="The path to the config file")

args = argparser.parse_args()

#read the config file
with open(args.config,'r') as f:
    configurations = yaml.safe_load(f)


#apply the download function to the list of files to be downloaded 
#by leveraging parrelization (multi threads)

#create a list of files to be downloaded
files_to_download = build_files_to_download(configurations)
print("Downloading...")

with ThreadPoolExecutor(max_workers=os.cpu_count() - 1) as executor:
    result = executor.map(download_file, files_to_download)
        

print("All files downloaded successfully")