import requests

def current_weather():
    api_key= "67da29cb91129f1a68c1c06c1be92daa"
    city="Macae"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

    request = requests.get(url)
    json = request.json()
    #print(json)
    #print(json['main'])
    vdescription = json['weather'][0]['description']
    temp_max = json['main']['temp_max']
    temp_min = json['main']['temp_min']
    print(vdescription)
    print("The max temper is " + str(temp_max))
    print("The min temper is " + str(temp_min))