import requests

city = 'Орехово-Зуево'

url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
coud_url = requests.get(url)
test_url =requests.get(url).json()


if str(coud_url) != "<Response [200]>":
    print("Ощибка получения данных")
else:
    whater_date = requests.get(url).json()

    temperature = round(whater_date['main']['temp'])
    temperature_feels = round(whater_date['main']['feels_like'])
    speed = round((whater_date['wind']['speed']))


    print("сейчас в городе", city , str(temperature), "C")
    print('Ощущается как', str(temperature_feels) , 'С')
    print('Скорость ветра', str(speed), "километры")