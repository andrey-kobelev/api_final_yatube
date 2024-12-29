# API Yatube  
### Автор
[Kobelev Andrey](https://github.com/andrey-kobelev)
  
## Краткое описание

**Yatube** — это платформа для блогов. 

**Возможности Yatube:**
- Зарегистрироваться;
- Создать, отредактировать или удалить собственный пост;
- Прокомментировать пост другого автора и подписаться на него.


> Доработал проект на Django, - добавил недостающие модели, и написал REST API (DRF) с нуля в соответствие с документацией в формате Redoc. Разработал систему аутентификации используя JWT-токены при помощи библиотеки Djoser. 

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/andrey-kobelev/api_yatube.git
```

```
cd api_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Документация для API Yatube

Когда вы запустите проект, будет доступна [документация](http://127.0.0.1:8000/redoc/) для API **Yatube**.  Документация представлена в формате **Redoc**.

## Примеры запроса и ответа

### Получение публикаций
Получить список всех публикаций. При указании параметров `limit` и `offset` выдача должна работать с пагинацией.

Сделайте GET-запрос на адрес:

http://127.0.0.1:8000/api/v1/posts/

Вывод будет таким:

```json
[
    {    
	    "id": 0,
	    "author": "string",
	    "text": "string",
	    "pub_date": "2021-10-14T20:41:29.648Z",
	    "image": "string",
	    "group": 0
    }
]

```

## Технологии
- [Python 3.9](https://www.python.org/downloads/release/python-390/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
