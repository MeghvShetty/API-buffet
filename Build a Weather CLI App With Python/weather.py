# weather 
import argparse
from random import sample
import ssl
import json
import sys
from configparser import ConfigParser
from urllib import  error, parse,request
from pprint import pp # print data structures in a readable, pretty way

#ssl._create_default_https_context = ssl._create_unverified_context # choose not to authenticate SSL certificate
BASE_WEATHER_API_URL ="https://api.openweathermap.org/data/2.5/weather"  # base API URL as it is the same for all the API calls maked in this program 

def _get_api_key():
    config = ConfigParser()
    config.read("secrets.ini")
    return config["openweather"]["api_key"]

def build_weather_query(city_input, imperial=False):
    api_key = _get_api_key()
    city_name = "".join(city_input)
    url_encoded_city_name = parse.quote_plus(city_name) # which encodes the string so that you can make a valid HTTP request to the API. Aside from converting certain characters through UTF-8 encoding, this function also converts whitespace characters to plus symbols (+), which is a form of URL encoding that’s necessary for proper calls to this API.
    units = "imperial" if imperial else "metric"

    url = (
        f"{BASE_WEATHER_API_URL}?q={url_encoded_city_name}"
        f"&units={units}&appid={api_key}"
    )
    return url

def read_user_cli_args():
    parser = argparse.ArgumentParser(   # create an instance of argparse.ArgumentParser
        description="get weather and temperature information for city"
    )

    parser.add_argument (
        "city", nargs="+", type=str, help="enter the city name"
    )

    parser.add_argument(
        "-i",
        "--imperial",
        action="store_true",
        help="display the temprature in imperial units",

    )
    return parser.parse_args()  # .parse_args(), which will eventually be the user-input values

def get_weather_data(query_url):
    try:
        response = request.urlopen(query_url)
    except error.HTTPError as http_error:
        if http_error.code == 401:  # 401 - Unauthorized
            sys.exit("Access denied. Check your API Key.")
        elif http_error.code == 404:  # 404 - Not Found
            sys.exit("can't find weather data for this city")
        else:
           sys.exit(f"something went wrong...({http_error.code})")
    
    data = response.read()
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        sys.exit("Couldn't read the server response.")

def display_weather_info(weather_data, imperial=False):
    city = weather_data ["name"]
    weather_description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"]

    print (f"{city}", end="")
    print(f"\t{weather_description.capitalize()}", end="")
    print(f"({temperature}°{'F' if imperial else 'C'})")
  

if __name__ == "__main__": # opens a conditional block after checking for Python’s "__main__" namespace, which allows you to define code that should run when you’re executing weather.py as a script
    user_args = read_user_cli_args()
    query_url = build_weather_query(user_args.city,user_args.imperial)
    weather_data = get_weather_data(query_url)
    display_weather_info(weather_data, user_args.imperial)
    #pp(weather_data)
    #print(
    #    f"{weather_data['name']}: "
    #    f"{weather_data['weather'][0]['description']}"
    #    f"({weather_data ['main']['temp']})"
    #)