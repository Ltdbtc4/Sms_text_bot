# TODO add:
#   google calendar API integration into main.py, dependency files DONE
#   openweathermap API integration into main.py DONE
#   emoji integration framework into main.py DONE
#   bored API integration into main.py DONE
#   dynamic SMS formatting function framework into main.py DONE
#   run function into main.py DONE
#   handle time in separate file DONE

# imports

import json
import time
import requests
from twilio.rest import Client
from Time import DateTime
from Emojis import Emoji
from get_events import Event

date_time = DateTime()
Emojis = Emoji()
event = Event(0)
weather_history = []

# keys

openweathermap_apikey = "27b8703e6c4838fb3a948bbd0848de9c"
account_sid = 'AC9762d2e763dfd76349286f4a601cc40e'
auth_token = '038ffb81f3fcefffd80495d5c6651e39'


# returns current weather
def return_weather(status_code):
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={51.5072}&lon={0.1276}&appid={openweathermap_apikey}")
    # prints response status if applicable
    if status_code == 1:
        print("openweathermap status:", response.status_code)
    # loads response.text into json format
    response_json = json.loads(response.text)
    # returns current weather status
    return response_json["weather"][0]["main"]


# returns a randomized activity
def return_activity(status_code):
    response = requests.get(f"https://www.boredapi.com/api/activity?participants=1")
    # prints response status
    if status_code == 1:
        print("bored_api status:", response.status_code)
    # loads response.text into json file format
    response_json = json.loads(response.text)
    # returns activity
    return response_json["activity"]


# sends SMS
def send_sms(Type, *args):
    assert Type == "weather_update" or Type == "morning" or Type == "night" or Type == "afternoon", "Invalid SMS formatting type"
    # initializes Client from twilio.rest.Client
    client = Client(account_sid, auth_token)
    # checks message type
    if Type == "weather_update":
        # sends message
        client.messages.create(from_='+15075754121',
                               to='+447368442188',
                               body=f"Weather update: "
                                    f"{weather_history[0], Emojis.return_weather_emoji(weather_history[0])} "
                                    f"has been changed to {args[0], Emojis.return_weather_emoji(args[0])}")
    elif Type == "morning":
        # sends message
        client.messages.create(from_='+15075754121',
                               to='+447368442188',
                               body=f"\n {Emojis.wave} Good morning \nThe Current Time is "
                                    f"{date_time.return_current_time('normal')} "
                                    f"and "
                                    f"the date is {date_time.return_current_date('normal')}. "
                                    f"The weather is {return_weather(status_code=1)}{Emojis.return_weather_emoji(weather_history[0])}. "
                                    f"{event.next_event()}")
    elif Type == "night":
        # sends message
        client.messages.create(from_='+15075754121',
                               to='+447368442188',
                               body=f"\n {Emojis.wave} Good night \nThe Current Time is "
                                    f"{date_time.return_current_time('normal')} "
                                    f"and "
                                    f"the date is {date_time.return_current_date('normal')}. "
                                    f"The weather is {return_weather(status_code=1)}{Emojis.return_weather_emoji(weather_history[0])}. "
                                    f"{event.tomorrows_event()}")
    elif Type == "afternoon":
        # sends message
        client.messages.create(from_='+15075754121',
                               to='+447368442188',
                               body=f"\n {Emojis.wave} Good afternoon \nThe Current Time is "
                                    f"{date_time.return_current_time('normal')} "
                                    f"and "
                                    f"the date is {date_time.return_current_date('normal')}. "
                                    f"The weather is {return_weather(status_code=1)}{Emojis.return_weather_emoji(weather_history[0])}. "
                                    f"{event.next_event()}")
    # print line for aesthetics
    # print line for aesthetics
    print("SMS status: 200")


# handles program functions
def run():
    i = 0
    current_weather = return_weather(0)
    # creates list for weather history
    weather_history.append(current_weather)
    while True:
        # sleeps between while loop as to moderate API pings
        time.sleep(0.7)
        # returns the current time in the validation format
        current_time = date_time.return_current_time("validation")
        # checks whether to send sms
        if current_time == "07:00:00":
            send_sms("morning")
        if current_time == "15:04:00":
            send_sms("afternoon")
        if current_time == "22:05:00":
            send_sms("night")
        # checks if variable(i) is a multiple of 3 this is a further method to reduce the amount of API pings (pings
        # it every 3 loops)
        if i % 5 == 0:
            if current_weather != return_weather(status_code=0):
                current_weather = return_weather(status_code=0)
                weather_history.insert(0, current_weather)
                send_sms("weather_update", current_weather)
                break
        # increments variable(i)
        i += 1


# runs program
if __name__ == "__main__":
    print("running status: 200")
    run()
