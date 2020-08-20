# Itinerary Generator

Itinerary Generator is a project that generates destination information by gathering data from 3 different API's. 

This project will quickly generate the following information based on a city of your choosing:

- 20 Places to eat
- 5 Day Weather Forecast
- 20 Points of Interest

## Environment Variables

```
USER_KEY = {USER_KEY}
TRIPOSO_ACCOUNT_ID = {TRIPOSO_ACCOUNT_ID}
TRIPOSO_API_KEY = {TRIPOSO_API_KEY}
APPID = {APPID}
```

## Usage
1. Register and obtain API Credentials from sources listed in References section or use your own API's 
2. Edit the current Configuration file with your API credentials and other sections as necessary
3. Install Dependencies `pip3 install -r requirements.txt`
4. Running in Terminal `python3 itinerary.py`
5. Running in Docker: `docker build .` to build the container
6. Run: `docker run -it -v "$(pwd):/data" itinerary_container` (replace with the name of your env file and container name)
7. The following should appear in the interactive terminal: `"Please enter the name of a city: <ENTER CITY NAME>"`

Once completed 3 CSV files will be generated for you locally

* POI.csv
* FOOD.csv 
* WEATHER.csv

**Optional**

API's and parameters can be re-configured and others can also be added. Note that Columns, Names, and Holder sections in yaml file will require an update as API urls and parameters are added or changed. 

## References
The following API's were used in order to create this project: 
 
- https://developers.zomato.com/api
- https://www.triposo.com/api/
- https://openweathermap.org/api