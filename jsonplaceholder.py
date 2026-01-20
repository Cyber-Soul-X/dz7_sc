import requests

# URL API для получения постов
url = "https://jsonplaceholder.typicode.com/posts"


try:
    # Отправляем GET-запрос
    response = requests.get(url)
    
    # Проверяем, что запрос успешен (статус 200)
    if response.status_code == 200:
        # Парсим JSON-ответ
        posts = response.json()
        
        # Выводим заголовки и тела первых 5 постов
        print("Первые 5 постов:\n")
        for i, post in enumerate(posts[:5], start=1):
            print(f"Пост #{i}:")
            print(f"Заголовок: {post['title']}")
            print(f"Тело: {post['body']}")
            print("-" * 50)  # Разделитель между постами
    else:
        print(f"Ошибка: HTTP {response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"Ошибка при выполнении запроса: {e}")
