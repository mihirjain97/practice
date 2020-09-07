import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=36.3741&lon=-119.2702#.X0oR38gzZPY')

# mumbai = requests.get(
#     'http://3.214.164.90/manage-vendor')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')

week_items = week.find_all(class_='tombstone-container')

period_names = [item.find(class_='period-name').get_text()
                for item in week_items]
short_Desc = [item.find(class_='short-desc').get_text() for item in week_items]
temp_Data = [item.find(class_='temp').get_text() for item in week_items]
# print(period_names)
# print(short_Desc)
# print(temp_Data)

weather_stuff = pd.DataFrame(
    {
        'Period': period_names,
        'Short_Description': short_Desc,
        'Temperature': temp_Data,
    }
)
print(weather_stuff)

weather_stuff.to_csv('Weather1.csv')
