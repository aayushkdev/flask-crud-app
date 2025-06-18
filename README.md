# Flask MongoDB User CRUD APP

## Requirements

- Docker
- Docker Compose

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/aayushkdev/flask-crud-app.git
cd flask-crud-app
```

### 2. Create a .env file

```bash
FLASK_DEBUG=false
SECRET_KEY=change-me
MONGO_URI=mongodb://mongo:27017/your_db_name
```

### 3. Run the app using docker compose

```bash
docker-compose up --build
```

### 4. test out the api

Use the url `http://localhost:5000/users` to test out the api