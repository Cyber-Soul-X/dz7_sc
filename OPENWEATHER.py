import requests
from decouple import config

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru'
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            print(f"\nПогода в {city_name}:")
            print(f"Температура: {temperature} °C")
            print(f"Описание: {description.capitalize()}")
        elif response.status_code == 404:
            print(f"Город '{city_name}' не найден. Проверьте написание.")
        elif response.status_code == 401:
            print("Ошибка авторизации: неверный API-ключ.")
        else:
            print(f"Ошибка API: статус {response.status_code}")
            print(f"Детали: {response.json().get('message', 'Неизвестно')}")
            
    except requests.exceptions.Timeout:
        print("Запрос превысил время ожидания (10 сек). Проверьте интернет-соединение.")
    except requests.exceptions.ConnectionError:
        print("Не удалось подключиться к API. Проверьте интернет или адрес сервера.")
    except requests.exceptions.RequestException as e:
        print(f"Неожиданная ошибка запроса: {e}")
    except KeyError as e:
        print(f"Ошибка обработки ответа: отсутствует поле {e}. Ответ API изменился.")

def main():
    try:
        API_KEY = config('OPENWEATHER_API_KEY')
    except Exception as e:
        print(f"Ошибка загрузки API-ключа: {e}")
        print("Проверьте файл .env и наличие переменной OPENWEATHER_API_KEY.")
        return

    city_name = input("Введите название города: ").strip()
    if not city_name:
        print("Название города не может быть пустым.")
        return
    
    get_weather(city_name, API_KEY)

if __name__ == "__main__":
    main()
