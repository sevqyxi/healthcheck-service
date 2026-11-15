# Healthcheck Service

Лабораторна робота №1 з дисципліни «Технології розроблення серверних компонентів».

У роботі реалізовано невеликий вебсервіс на Python з використанням Flask. Він має два ендпоінти для перевірки стану сервера. Для запуску використовується Docker Compose, а для автоматичної перевірки коду — GitHub Actions.

## Використані технології

- Python 3.11, Flask
- Docker, Docker Compose
- GitHub Actions
- Ruff

## Основні ендпоінти

`GET /healthz/live` — перевіряє, чи працює застосунок. Повертає статус `alive` і поточний час UTC.

`GET /healthz/ready` — перевіряє готовність сервера до роботи. Повертає статус `ready`, поточний час і стан підключення до бази даних (`not_connected_yet`).

Обидва ендпоінти повертають HTTP 200 OK.

## Запуск проєкту

Для запуску потрібен встановлений Docker Desktop.

1. Клонувати репозиторій та перейти в папку проєкту:

   ```bash
   git clone <URL_репозиторію>
   cd healthcheck-service
   ```

2. Зібрати та запустити контейнер:

   ```bash
   docker compose up --build -d
   ```

3. Перевірити його стан:

   ```bash
   docker compose ps
   ```

4. Перевірити роботу ендпоінтів:

   ```bash
   curl -i http://localhost:8080/healthz/live
   curl -i http://localhost:8080/healthz/ready
   ```

5. Зупинити контейнер:

   ```bash
   docker compose down
   ```

## GitHub Actions

У проєкті налаштовано автоматичну перевірку при push або pull request у гілку `main`.

GitHub Actions виконує перевірку коду за допомогою Ruff, збірку Docker-образу та перевірку конфігурації Docker Compose.

Результати перевірок можна переглянути у вкладці Actions на GitHub.
