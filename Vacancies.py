import requests
import json

# Базовый URL API hh.ru для поиска вакансий
BASE_URL = 'https://api.hh.ru/vacancies'

# Параметры запроса (например, поиск вакансий по ключевому слову "Python" в Москве)
params = {
    'text': 'Python',  # Ключевое слово для поиска
    'area': 1,         # Код региона (1 — Москва)
    'per_page': 5       # Количество вакансий на странице
}

# Отправляем GET-запрос к API
response = requests.get(BASE_URL, params=params)

# Проверяем статус ответа
if response.status_code == 200:
    # Парсим JSON ответ
    data = response.json()

    
    print("Результаты поиска вакансий:")
    for vacancy in data['items']:
        print(f"\nВакансия: {vacancy['name']}")
        print(f"Компания: {vacancy['employer']['name']}")
        print(f"Зарплата: {vacancy['salary']['from'] if vacancy['salary'] else 'не указана'} {vacancy['salary']['currency'] if vacancy['salary'] else ''}")
        print(f"Город: {vacancy['area']['name']}")
        print(f"Ссылка: {vacancy['alternate_url']}")
        print(f"Опубликована: {vacancy['published_at']}")
else:
    print(f"Ошибка при запросе данных: {response.status_code}")