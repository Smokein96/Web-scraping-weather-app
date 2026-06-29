import requests  
from bs4 import BeautifulSoup
from state_finder import location_finder


city = input("enter city name :")

state = location_finder(city)
if state == None:
    print("no city found")
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

print(f"State : {state}\n Temperature : {temperature}\n Humidity :{humidity}\n Wind:{wind}\n Pressure :{pressure}")