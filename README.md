# DevOps-WS – Fullstack Boilerplate with FastAPI, PostgreSQL, Vite + React & NGINX

This project is designed primarily to **learn Docker fundamentals** by integrating a simple FastAPI backend, PostgreSQL database, and a Vite-powered React frontend. The focus is on Docker Compose orchestration, service communication, volume usage, and container health checks.

This is a full-stack starter project using:
- FastAPI (async backend)
- PostgreSQL (as the database)
- Vite + React (frontend)
- NGINX (reverse proxy)
- Docker Compose (container orchestration)

---

## Project Structure

```
devops-ws/
├── backend/           # FastAPI backend & PostgreSQL DB
│   ├── ...
├── frontend/          # Vite + React frontend
│   ├── ...
├── nginx/
│   └── ...
├── .env (should be added by user)
├── docker-compose.yml
└── README.md
```

---

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/berzankocdag/devops-ws.git
cd devops-ws
```

### 2. Set environment variables
Create a `.env` file:
```env
POSTGRES_USER=postgresdb
POSTGRES_PASSWORD=postgresdb
POSTGRES_DB=mypostgres
```

Also in `frontend/.env`:
```env
VITE_API_BASE_URL=http://localhost/api
```

### 3. Run Docker Compose
```bash
docker-compose up --build
```

---

## 📦 API Endpoints

- `GET /users/` – List users  
- `POST /users/` – Create user  
- `GET /users/{id}` – Get user by ID  
- `GET /items/` – List items  
- `POST /items/` – Create item  

---

## 💡 Why This Setup?

### FastAPI
- Modern async Python backend
- Pydantic + OpenAPI docs included

### PostgreSQL
- Reliable, production-grade relational DB

### Vite + React
- Fast frontend build & hot-reload dev environment

### NGINX
- Reverse proxy to serve frontend and proxy `/api/*` to backend

### Docker Compose
- Multi-service orchestration made easy for local and deployment

---
