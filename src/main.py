import requests  
from bs4 import BeautifulSoup
from state_finder import location_finder


city = input("enter city name :")

state = location_finder(city)
if state == None:
    raise ValueError(f"'{city}' is not a valid Indian city.")
    exit()

url = f"https://www.aqi.in/weather/in/india/{state.lower()}/{city.lower()}"

try:
    resp = requests.get(url) #requesting from site
    resp.raise_for_status() 
except Exception as e :
    print(e)
    exit()


soup = BeautifulSoup(resp.text,"html.parser") #parsing using BS
parsed = soup.find("meta", attrs={"name":"description"}) #getting the exact tag
if parsed:
    content = parsed["content"]
else: 
    print("error in parsing ")

slices = content.split(",") #splitting the string for further parsing

temperature = slices[0].split("temperature (")[1].replace(")","")
humidity = slices[1].replace("humidity ","")
wind = slices[2].replace("wind ","")
pressure = slices[3].replace("pressure ","").replace("(", "").replace(")", "")

weather = {
    "state":state,
    "temperature": temperature,
    "humidity": humidity,
    "wind": wind,
    "pressure": pressure,
}

print(
    f"State : {weather['state']}\n"
    f"Temperature : {weather['temperature']}\n"
    f"Humidity : {weather['humidity']}\n"
    f"Wind : {weather['wind']}\n"
    f"Pressure : {weather['pressure']}"
)