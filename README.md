# FINO

Командный курсовой проект — система обработки заявок на заём для МФО. Делаем приложение, в котором менеджер сможет добавить клиента, оформить заявку и посмотреть результат скоринга.

## Что уже есть

- API для создания и просмотра клиентов и заявок.
- Вход по email и паролю с JWT-аутентификацией.
- Отдельный сервис принятия решения по вероятности и заданным порогам; подключение к обработке заявок ещё в разработке.
- Модели данных и миграции для PostgreSQL.

Расчёт скоринга и интерфейс ещё в разработке. Фронтенд инициализирован на React и TypeScript; установлены Ant Design и Tailwind CSS.

## Стек

**Фронтенд:** React, TypeScript, Ant Design, Tailwind CSS, Vite.

**Бэкенд:** Python, FastAPI, Pydantic, SQLAlchemy, PostgreSQL, Alembic, JWT.

## Запуск

Нужны Docker Compose, uv и Bun. Команды выполняются из корня проекта.

Скопируй `.env.example` в `.env`, задай пароль базы и подними PostgreSQL:

```sh
cp .env.example .env
docker compose up -d postgres
```

Создай `backend/.env`. Имя пользователя, пароль и имя базы должны совпадать с корневым `.env`:

```env
DATABASE_URL=postgresql+psycopg://mfo_app:your-database-password@localhost:5433/mfo_db
SECRET_KEY=replace-with-a-long-random-string
```

Запусти бэкенд:

```sh
cd backend
uv sync
mkdir -p static/images
uv run alembic upgrade head
uv run python run.py
```

В другом терминале из корня проекта запусти фронтенд:

```sh
cd frontend
bun install
bun run dev
```

Фронтенд — http://localhost:5173, документация API — http://localhost:8000/api/docs.

Для работы с API клиентов и заявок нужна авторизация. Вход выполняется через `POST /api/auth/login`. Создание первого пользователя пока не автоматизировано; регистрации через API нет.

Сценарии работы и схема данных лежат в [docs](docs).
