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
        - 'first_year_gas' (int): The starting year for gas data.
        - 'last_year_gas' (int): The last year for gas data.
        - 'year_station_file' (int): The year for station file.
        - 'year_service_file' (int): The year for service file.

    Returns:
    - list: A list of file names to be downloaded.
    e.g [prix2019.csv.gz,prix2020.csv.gz,...]
    """

    #generate a list of gas files following the pattern
    #Prix2008,Prix2009,...., 
    #2008 is starting year and can be changed in the yaml configuration file

    files = list(map(lambda i: f'Prix{i}.csv.gz',
                     list(range(
                         configurations['first_year_gas'],
                         configurations['last_year_gas']+1))))
    
    #add the station file to be downloaded based on the year provided
    files.append(f'Stations{configurations["year_station_file"]}.csv.gz')

    #add the Services file to be downloaded based on the year provided
    files.append(f'Services{configurations["year_service_file"]}.csv.gz')

    #handle the Prix2022 exception since it doesn't exist on Github
    files.remove('Prix2022.csv.gz')
    #add its 2 versions manually
    files.append('Prix2022S2.csv.gz')
    files.append('Prix2022S1.csv.gz')
    return files



def download_file(file):
    """
    Downloads a file from a specified URL and saves it to a designated location.

    Args:
    - file (str): The name of the file to be downloaded.

    Returns:
    - None

    Raises:
    - Exception: If the download fails, an exception is raised.

    Note:
    Ensure that the 'requests' library is installed to use this function for making HTTP requests.
    """

    #get the base url from the config file 
    base_url = configurations['base_url']

    #get the data destination path from the config file
    destination_path = configurations['base_data_location']

    #create the file url based on both the base_url and the file name
    url = base_url + file
    try:    
            #make a request to download the file
            response = requests.get(url)
            #if requests is successful
            if response.status_code == 200:
                #save the file to the destination path
                with open(destination_path + file, 'wb') as f:
                    f.write(response.content)
                    print(f'Successfully downloaded {file}')
    except Exception:
            print(f'Failed to download {file}')


#create arguments for our python script
#especially the config file that is needed
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


#download the files using parrelization
with ThreadPoolExecutor(max_workers=os.cpu_count() - 1) as executor:
    result = executor.map(download_file, files_to_download)
        

print("All files downloaded successfully")