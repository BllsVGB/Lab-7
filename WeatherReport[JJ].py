import requests

# Убедитесь, что API-ключ заключен в кавычки
API_KEY = '3ce734815c80183853938f8675804c74' 
CITY_NAME = 'Ceadîr-Lunga'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Параметры запроса
params = {
    'q': CITY_NAME,
    'appid': API_KEY,  # Передаем API-ключ
    'units': 'metric',  # Используем метрическую систему для температуры (градусы Цельсия)
    'lang': 'ru'
}

# Отправляем запрос к API
response = requests.get(BASE_URL, params=params)

# Проверяем статус ответа
if response.status_code == 200:
    # Парсим JSON ответ
    data = response.json()
    
    # Извлекаем нужные данные
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind_speed = data['wind']['speed']
    
    # Выводим информацию
    print(f"Погода в городе {CITY_NAME}:")
    print(f"Описание: {weather.capitalize()}")
    print(f"Температура: {temperature}°C")
    print(f"Влажность: {humidity}%")
    print(f"Давление: {pressure} hPa")
    print(f"Скорость ветра: {wind_speed} м/с")
else:
    print(f"Ошибка при запросе данных: {response.status_code}")
    print(f"Сообщение: {response.json().get('message', 'Нет дополнительной информации')}")