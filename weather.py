
from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Wroclaw"):
    request_url = f"http://api.openweathermap.org/data/2.5/weather?appid={os.getenv('OPEN_WEATHER_API_KEY')}&q={city}&units=metric"
    weather_data=requests.get(request_url).json()
    return weather_data

if __name__ == '__main__':
    print('get_current_weather conditions')
    city = input('Enter city name: ')
    if not bool(city.strip()):
        city = 'Wroclaw'
    # todo : fix internal server error for empty input
    weather_data = get_current_weather(city)
    print(weather_data)
