import requests
import sys
GoogleMapsAPIKey = "AIzaSyCFyytn6hOsL5j-D9vvKibMEq8MZTp9mjc"
OpenWeatherMapKey = "b00dc69092e7b4e6199a61b16874d897"
CityCHK = "haifa"
#CityCHK = input("Which city temperature you want to check? ")
RequestGoogleCoords = f"https://maps.googleapis.com/maps/api/geocode/json?&address={CityCHK}&key={GoogleMapsAPIKey}"
GoogleResp=requests.get(RequestGoogleCoords)
GoogleJsonResp = GoogleResp.json()
GoogleServicesStatus = GoogleJsonResp["status"]
#print(f"Google Services Status is {GoogleServicesStatus}")
if GoogleServicesStatus != "OK":
    print(f"Error accord while trying to get {CityCHK} coordinates using google maps api services")
    sys.exit("Error accord!")
else:
    address = GoogleJsonResp["results"][0]["geometry"]["location"]
    lat = address["lat"]
    lng = address["lng"]
    #print(lat,lng)
    RequestOpenWeatherMap = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&units=metric&APPID={OpenWeatherMapKey}"
    OpenWeatherMapResp = requests.get(RequestOpenWeatherMap)
    OpenWeatherMapJsonResp = OpenWeatherMapResp.json()
    openweatherservicestatus = OpenWeatherMapJsonResp["cod"]
    #print(OpenWeatherMapJsonResp)
if openweatherservicestatus != 200:
    errormessage = OpenWeatherMapJsonResp["message"]
    print(f"Error Code: {openweatherservicestatus} Message: {OpenWeatherMapJsonResp}")
else:
    citytemp = OpenWeatherMapJsonResp["main"]["temp"]
    print(f"Current Temperature in {CityCHK} is {citytemp} Celsios degree")
