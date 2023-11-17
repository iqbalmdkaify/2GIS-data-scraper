# 2GIS Map data scraper

### Project description and working

For database building and personal data-science projects, this is an automated script written in Python (.ipynb) file that scrapes and parses the **2GIS map data** received in the User Interface (UI) of browser. Many websites, such as Google Maps, 2GIS, and others, do not use a free open API call to retrieve map data, which could cause issues for data scientists doing data mining on websites where map data is the main source of information. Various data scraping libraries and methods are available in Python including BeautifulSoup, Selenium, htmllib3, etc. In order for these libraries to scrape web material, a few prerequisites must be met, one of which is that the user interface (UI) must have stale, non-dynamic data (HTML page). Data scientists may encounter difficulties in obtaining the necessary data for their projects because the majority of geo and dynamic data involves online API calls that result in dynamic web pages and content and are not free of cost. I mixed the power of Selenium *web driver* with BeautifulSoup for scraping dynamic Geo data with better accuracy. Basically, the Selenium web driver acts as an automated host client, searching and navigating the data in real time while dynamically modifying the user interface to produce HTML text data snapshots for BeautifulSoup that can be parsed at a later time. The associated website's *CAPTCHA verification* and *API calls limitation* are **circumvented** by the web driver's automated human matched search and navigation timing, resulting in the generation of *balanced and precised data*. The output data is saved in the CSV (.csv) format, which can subsequently be utilized for pre-processing or building databases for assignments and learning.

## Status

The present project is still in the planning stages, during which time more enhancements and modifications will be made to support various geo-navigation websites.

## Environments

It's best to use virtual environments. To successfully create the environment file and install dependencies and libraries, execute and follow each of the following code steps one at a time. 

1. **virtualenv** can be used to run the code after generating the environment file and installing the dependencies from the *requirements.txt* file. Other components which are **not a part** of the *requirements.txt* file such as web drivers are mentioned in the following sections.

```
pip install virtualenv
virtualenv your_env_name
source your_env_name/bin/activate
pip install -r requirements.txt
```

2. Or you can use **venv** to create a virtual environment.

```
python -m venv <path_to your_env>
cd <path_to your_env>/
source ./Scripts/activate
pip install -r requirements.txt
```

## Requirements

The items listed below are essential for properly executing the code. Please take note that I've specified a separate section with a step-by-step guide if you're having trouble installing and configuring the *Chrome web driver*.

- [Chrome browser](https://www.google.com/chrome/?brand=YTUH&gclid=CjwKCAiA9dGqBhAqEiwAmRpTC5tpn7r1ZsmaprDlSZnRaMTgMAlk3hIVAhXEvt-nOnOJo-IlgFab9hoCPugQAvD_BwE&gclsrc=aw.ds)
- [Chrome web driver](https://chromedriver.chromium.org/downloads)
- [Python](https://www.python.org/downloads/) 
- [Jupyter Notebook](https://jupyter.org/install) 

## How to use and run the file

Kindly adhere to the instructions for setting up and executing the script.

##### Cloning Repo and creating environment

​	1. Clone the [repo](https://github.com/iqbalmdkaify/2GIS-data-scrapper.git) from GitHub to your destination folder and navigate to that cloned folder.

```
git clone <repo_origin> <dest_path>
cd <dest_path>/
```

​	2. Create Virtual environment inside the very same folder using **venv** and activate it.

```
python -m venv ./
source ./Scripts/activate
```
​	3. Install the dependencies from the <code>requirements.txt</code> file by running the following command.

```
pip install -r requirements. txt
```

##### Download Chrome web driver

1. Navigate to the following [link](https://chromedriver.chromium.org/downloads) and download the driver which matches your Google Chrome version.

2. Extract the downloaded folder. Copy the *chromedrive.exe* file to your chrome **path** folder <code>C:/Users/<username>/chrome driver/</code> 

##### Set the constants in the <code>main.ipynb</code> file

Five **constant variables** must be set in total in the *main.ipynb file*. Verify that the following files are in the same directory or folder: <code>main.ipynb, markup_file, csv_data_file</code>. If they are located in different directories, the **full path** to these files must be included in the code. An example file for the output CSV file(_data.csv_) is provided in the repo, feel free to see the file structure in order to modify the <code>headers</code> variable in the _main_ script.

You can run the script in [Jupyter Notebook](https://jupyter.org/install) after configuring the variables listed below.

1. Set <code>HEADERS</code> for the csv file in the <code>main.ipynb</code> file. Default *headers* <code>['title', 'type', 'address', 'rating']</code> are already written which can be changed according to your needs.

2. Set <code>MARKUP_FILENAME</code> to the name of the file where the script will store the UI HTML data snapshots temporarily, **e.g.** <code>your_filename.txt</code> 

3. Set <code>CSV_DATA_FILENAME</code> to the name of the file where you will store your final output data.

4. Set the <code>SEARCH</code> to your 2GIS *query_text* which you want to search in the map.

5. Set the <code>CITY_NAME</code> to the *city_name* where you want to search your query.

##### Run the script from the <code>main.ipynb</code> file

##### Run the last code block for removing potential duplicates if it exists

## Chrome web driver configuration

Should you want to utilize the project without a virtual environment, you will need to install the necessary libraries manually that the script uses. You can get further information about Chrome Web Driver for Python from this [source](https://reflect.run/articles/installing-chromedriver-and-python-selenium/).

1. Using the following command, install *Chrome webDriver Manager* first:

```
pip install webdriver-manager # or pip3 install webdriver-manager
```

It is important to import these. Kindly don't change them.

![Screenshot_imports](https://github.com/iqbalmdkaify/2GIS-data-scrapper/blob/main/images/capture_20231115154824785.bmp)

Furthermore, these code blocks are mandatory.

![Screenshot_code_block](https://github.com/iqbalmdkaify/2GIS-data-scrapper/blob/main/images/capture_20231115154838058.bmp)

2. Install Selenium

```
pip install selenium
```

3. Install Pandas

```
pip install pandas
```

4. Install BeautifulSoup

```
pip install beautifulsoup4
```

## License Information

[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/#) 
