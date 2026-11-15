# Healthcheck Service

Лабораторна робота №1 з дисципліни «Технології розроблення серверних компонентів».

Веб-сервіс на Python + Flask із двома системними ендпоінтами перевірки стану (Liveness / Readiness), контейнеризацією через Docker та CI на GitHub Actions.

## Стек

- Python 3.11, Flask, Gunicorn
- Docker, Docker Compose
- GitHub Actions, Ruff (лінтер)

## Структура проєкту

```
.
├── .github/
│   └── workflows/
│       └── ci.yml            # CI: лінтер + збірка Docker-образу
├── .dockerignore
├── .gitignore
├── app.py                    # Flask-застосунок з healthcheck-ендпоінтами
├── docker-compose.yaml
├── Dockerfile                # мультистадійна збірка
├── README.md
└── requirements.txt          # зафіксовані версії залежностей
```

## API

| Метод | Шлях            | Опис                                  | Статус |
|-------|-----------------|---------------------------------------|--------|
| GET   | `/healthz/live`  | Liveness probe — процес живий         | 200 OK |
| GET   | `/healthz/ready` | Readiness probe — сервіс готовий до трафіку | 200 OK |

Приклад відповіді `GET /healthz/live`:

```json
{
  "status": "alive",
  "timestamp": "2026-11-15T10:00:00.000000+00:00"
}
```

Приклад відповіді `GET /healthz/ready`:

```json
{
  "status": "ready",
  "database": "not_connected_yet",
  "timestamp": "2026-11-15T10:00:00.000000+00:00"
}
```

## Локальний запуск через Docker Compose

### Вимоги

- встановлений [Docker Desktop](https://www.docker.com/products/docker-desktop/) (або Docker Engine + плагін Docker Compose v2);
- вільний порт `8080`.

### Кроки

1. Клонувати репозиторій:

   ```bash
   git clone <URL_репозиторію>
   cd <назва_репозиторію>
   ```

2. Зібрати образ і запустити контейнер:

   ```bash
   docker compose up --build -d
   ```

3. Перевірити, що контейнер запущений (через ~30 с у колонці STATUS з'явиться `healthy`):

   ```bash
   docker compose ps
   ```

4. Перевірити ендпоінти:

   ```bash
   curl -i http://localhost:8080/healthz/live
   curl -i http://localhost:8080/healthz/ready
   ```

   Або відкрити ці адреси в браузері.

5. Переглянути логи:

   ```bash
   docker compose logs -f app
   ```

6. Зупинити та видалити контейнер:

   ```bash
   docker compose down
   ```

## Запуск без Docker (для розробки)

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Сервіс буде доступний на `http://localhost:8080`.

## Лінтер

```bash
pip install ruff==0.16.9
ruff check .
```

## CI (GitHub Actions)

Workflow `.github/workflows/ci.yml` запускається при кожному `push` та `pull_request` у гілки `main` / `master` і виконує:

1. статичний аналіз коду лінтером Ruff;
2. збірку Docker-образу;
3. валідацію конфігурації `docker-compose.yaml`.

Результати доступні на вкладці **Actions** репозиторію.
