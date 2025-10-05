<p align="center"> <img src="https://img.shields.io/badge/FastAPI-109989?style=for-the-badge&logo=fastapi&logoColor=white" /> <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" /> <img src="https://img.shields.io/badge/SQLAlchemy-FF6600?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" /> <img src="https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white" /> <img src="https://img.shields.io/badge/Docker-0db7ed?style=for-the-badge&logo=docker&logoColor=white" /> <img src="https://img.shields.io/badge/Python_3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" /> </p>

---

# 🌤️ WeatherHub — Async Weather Data API

<img width="1510" height="875" alt="изображение" src="https://github.com/user-attachments/assets/abaf192c-2f4b-4aba-bc7c-a2a964c998b0" />


> **WeatherHub** is an asynchronous REST API built with **FastAPI**, **Celery**, and **Redis**.
> It provides up-to-date weather information for multiple cities and automatically updates data on a schedule.

---

## 🚀 Tech Stack

* **Python 3.11+**
* **FastAPI** — modern async web framework
* **SQLAlchemy + PostgreSQL** — ORM and database
* **Celery + Redis** — background task queue and periodic jobs
* **Docker & Docker Compose** — containerized environment
* **Pydantic** — data validation and serialization

---

## ⚙️ Setup & Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/weatherhub.git
cd weatherhub
```

### 2️⃣ Create an `.env` file

```bash
OPENWEATHER_API_KEY=your_api_key_here
DATABASE_URL=postgresql+psycopg2://user:password@db/weatherhub
REDIS_URL=redis://redis:6379/0
```

### 3️⃣ Start with Docker Compose

```bash
docker-compose up --build
```

API will be available at:
👉 `http://localhost:8000`

Celery and Celery Beat will automatically start and handle background tasks.

---

## 🌍 API Endpoints

| Method | Endpoint                      | Description                                  |
| :----: | :---------------------------- | :------------------------------------------- |
|  `GET` | `/weather/?city={city}`       | Get current weather data for a specific city |
|  `GET` | `/weather/all`                | Get all stored weather records               |
|  `GET` | `/weather/cities`             | List all tracked cities                      |
| `POST` | `/weather/update?city={city}` | Manually trigger weather update for a city   |

---

## 🕒 Periodic Tasks (Celery Beat)

WeatherHub automatically updates weather data every **N minutes** for all cities.
Configuration is defined in:

```
app/tasks/scheduler.py
```

You can adjust the update frequency via Celery Beat schedule settings.

---

## 🧪 Testing

Run tests using **pytest**:

```bash
pytest -v
```

---

## 📁 Project Structure

```
weatherhub/
├── app/
│   ├── api/
│   │   └── routes_weather.py
│   ├── core/
│   │   ├── celery_app.py
│   │   └── config.py
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   │   └── weather.py
│   ├── schemas/
│   │   └── weather.py
│   └── tasks/
│       ├── weather_tasks.py
│       └── scheduler.py
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

## 📦 Example API Response

```json
{
  "city": "Tokyo",
  "temperature": 22.5,
  "description": "clear sky",
  "created_at": "2025-10-05T15:30:00"
}
```

---

## 🧩 Future Improvements

* [ ] User authentication & roles
* [ ] Caching with Redis for faster responses
* [ ] Monitoring via Prometheus & Grafana
* [ ] Frontend dashboard for weather visualization

---

## 👨‍💻 Author

**(https://github.com/GrigoryZakharov)**
💬 Telegram: [@yourhandle](https://t.me/@ILoveTankiOnline)
📧 Email: [@email.com](mailto:zakharov9933@gmail.com)

---

## 🪪 License

This project is distributed under the **MIT License** — free to use, modify, and improve 🚀

---
