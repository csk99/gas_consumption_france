# GAS Consumption prediction in France




## Introduction
In this project, we aim to predict Gas consumption using machine learning and Gas  data from 2008 (or 2009,2010,customizable) to 2023 available [here](https://github.com/rvm-courses/GasPrices) across many stations in France.
We will also exploit amazing spark capabilities to run machine learning workloads under different harware conditions. Firstly on a local node spark environment where master and slave processes are colocated and also on a cluster in the cloud using Google Cloud Platform.

### Technologies / Frameworks used 
* ![Static Badge](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
* ![Static Badge](https://img.shields.io/badge/Apache_Spark-FFFFFF?style=for-the-badge&logo=apachespark&logoColor=#E35A16)
* ![Static Badge](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)

## Project Description
*Work in progress*


## Working principle
*Work in progress*

## Running time
*Work in progress*





## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).

2. Create a virtual env in the project folder (for help see this [tutorial](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/))

3. Run the following command to load tha data (in the project folder)
* For linux users:
```
python3 download_data.py -c config.yaml
```
* For windows users:
```
python download_data.py -c config.yaml
```    


4. Run the following command to unzip the files (in the project folder)
* For linux users:
```
chmod +x unzip_files.sh
```
```
./unzip_files.sh data
```
*It's a linux shell script*


5. Open the report.ipynb notebook and run the cells.<br> 
*Please choose the python virtual environment you created previously*<br> 
This notebook contains our Exploritory data analysis and model training.


