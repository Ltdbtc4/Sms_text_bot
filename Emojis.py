class Emoji:
    def __init__(self):
        self.clear_sky = "\U0001F325"
        self.few_clouds = "\U0001F324"
        self.scattered_clouds = "\U0001F32C"
        self.broken_clouds = "\U0001F32C"
        self.shower_rain = "\U0001F328"
        self.rain = "\U0001F4A7"
        self.thunder = "\U0001F32A"
        self.snow = "\U0001F32B"
        self.mist = "\U0001F32B"
        self.arrow = "\U0002F32B"
        self.wave = "\U0001F44B "

    # searches for emoji based on weather
    def return_weather_emoji(self, weather):
        if weather == "01d" or "01n":
            return self.clear_sky
        elif weather == "02d" or "02n":
            return self.few_clouds
        elif weather == "03d" or "03n":
            return self.scattered_clouds
        elif weather == "04d" or "04n":
            return self.broken_clouds
        elif weather == "09d" or "09n":
            return self.shower_rain
        elif weather == "10d" or "10n":
            return self.rain
        elif weather == "11d" or "11n":
            return self.thunder
        elif weather == "13d" or "13n":
            return self.snow
        elif weather == "50d" or "50n":
            return self.mist
        else:
            return self.clear_sky
