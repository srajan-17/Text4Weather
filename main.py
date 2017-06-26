import json
import requests

def getWeather(zp):
    
    # This section generates the weather data for a location (The location is specified by a zip code).
    
    weather_key = "83badc33240c1f999e6c93790f0e3a03"

    base_url = "http://api.openweathermap.org/data/2.5/weather?zip="

    def gen_url(zip_code):
        return base_url + zip_code + ",us" + "&APPID=" + weather_key

    r = requests.get(gen_url(str(zp)))

    data = r.json()


    # This section takes the generated weather data and filters out the information that is needed.

    max_temp = data['main']['temp_max']
    pressure = data['main']['pressure']
    min_temp = data['main']['temp_min']
    temp = data['main']['temp']
    humid = data['main']['humidity']

    max_temp_fahrenheit = round(9/5 * (max_temp - 273) + 32, 2)
    min_temp_fahrenheit = round(9/5 * (min_temp - 273) + 32, 2)
    temp_fahrenheit = round(9/5 * (temp - 273) + 32, 2)


    # After filtering out and declaring the needed variables, the messages are created as strings.

    s1 = "The maximum temperature is " + str(max_temp_fahrenheit) + " ºF."
    s2 = "The pressure is " + str(pressure) + " hPa."
    s3 = "The minimum temperature is " + str(min_temp_fahrenheit) + " ºF."
    s4 = "The current temperature is " + str(temp_fahrenheit) + " ºF."
    s5 = "The humidity is " + str(humid) + "%." 
    s6 = s4 + "\n" +\
         s3 + "\n" +\
         s1 + "\n" +\
         s2 + "\n" +\
         s5 + "\n"

    return s6


# The complete message is printed.

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def response():
    #Respond to incoming texts with a simple text message.
    resp = MessagingResponse()
    strResp = request.form.get('Body')
    strfinal = strResp.lower()
    zipcode = request.form.get('FromZip')
    s7 = getWeather(zipcode) + "Zip Code: " + str(zipcode)
    print(strfinal, zipcode)
    if "weather" in strfinal:
        resp.message(s7)
    else:
        resp.message("If you want to know the weather, type weather.")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

