# Backend API (FastAPI)

## Описание

Backend‑часть приложения, реализованная на **FastAPI** с использованием **SQLAlchemy** и JWT‑аутентификации.

API предоставляет:

* регистрацию и логин пользователей
* JWT‑авторизацию
* работу с сущностями (favorites и др.)
* Swagger‑документацию

Проект ориентирован на работу с фронтендом (React / Web / Mobile) по REST API.

---

## Стек

* Python 3.10+
* FastAPI
* SQLAlchemy
* SQLite (по умолчанию)
* JWT (access token)
* Pydantic

---

## Структура проекта

```
admin/
core/           # конфигурация, security, зависимости
models/         # SQLAlchemy модели
repositories/   # работа с БД
routers/        # API роуты
schemas/        # Pydantic схемы
services/       # бизнес‑логика
main.py         # точка входа
```

---

## Установка и запуск

### 1. Клонирование проекта

```bash
git clone <repo_url>
cd <project_name>
```

### 2. Виртуальное окружение

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\\Scripts\\activate     # Windows
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Запуск приложения

```bash
uvicorn main:app --reload
```

Приложение будет доступно по адресу:

```
http://127.0.0.1:8000
```

---

## Документация API (Swagger)

Swagger UI:

```
http://127.0.0.1:8000/docs
```

OpenAPI JSON:

```
http://127.0.0.1:8000/openapi.json
```

---

## Аутентификация

Используется JWT (Bearer token).

### Логин

`POST /login`

Пример запроса:

```json
{
  "email": "user@example.com",
  "password": "password"
}
```

Ответ:

```json
{
  "access_token": "jwt_token"
}
```

---

### Использование токена

Для защищённых эндпоинтов необходимо передавать заголовок:

```
Authorization: Bearer <access_token>
```

В Swagger:

1. Нажать **Authorize**
2. Вставить:

   ```
   Bearer <access_token>
   ```

---

## Работа с фронтендом

Фронтенд взаимодействует с backend через HTTP‑запросы.

Пример:

```text
fetch → JSON → render
```

Backend возвращает **JSON‑объекты или массивы объектов**, которые фронтенд может напрямую использовать для отображения.

Пример ответа:

```json
[
  {
    "id": 1,
    "title": "Item",
    "is_favorite": true
  }
]
```

---

## База данных

По умолчанию используется **SQLite** (`database.db`).

Важно:

* файл базы **НЕ хранится в репозитории**
* база создаётся локально при запуске

Для production рекомендуется PostgreSQL.

---

## Переменные окружения (пример)

Создай `.env` на основе `.env.example`:

```env
SECRET_KEY=supersecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## Статус проекта

Проект находится в активной разработке.

---

## Контакты

Backend разработка — API для фронтенда.
