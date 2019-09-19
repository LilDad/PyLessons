import pyowm

city = input('Какой город Вас интересует? ')

owm = pyowm.OWM('5b91c21ff3f01790e9698c6234646496')  # You MUST provide a valid API key

observation = owm.weather_at_place(city)
t = observation.get_weather()
temperature = t.get_temperature('celsius')['temp']

print('В городе ' + 'сейчас температура: ' + str(temperature))

def det_status():
    status = t.get_detailed_status()
    if status == 'clear sky':
        return "ясное небо!))"

print("Также, в указанном городе " + det_status())