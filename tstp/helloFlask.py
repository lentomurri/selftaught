import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.bbc.co.uk/weather/2650225")
soup = BeautifulSoup(page.content, "html.parser")
mydivs= soup.find_all(class_="wr-day-container")
result = mydivs[0].find(class_="wr-day-summary") 
day = result.find_all("span")
week = soup.find_all(class_="wr-day-temperature")
temperatureHigh =  week[0].find_all(class_="wr-value--temperature--c")
print(len(temperatureHigh))
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# for i in range(0,6):
#     forecast = day[i].get_text()
#     print(days[i] + ":\n" + forecast )