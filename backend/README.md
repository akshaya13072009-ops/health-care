# Healthcare Backend API

A FastAPI-based backend for the Healthcare Management System.

## Setup

### 1. Create Virtual Environment
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
```bash
cp .env.example .env
# Edit .env with your configuration
```

### 4. Run the Application
```bash
python main.py
```

The API will be available at `http://localhost:8000`

## API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure
```
backend/
├── app/
│   ├── models/        # Database models
│   ├── routes/        # API routes
│   ├── schemas/       # Pydantic schemas
│   ├── config.py      # Configuration
│   └── database.py    # Database setup
├── main.py            # Application entry point
├── requirements.txt   # Dependencies
└── README.md          # This file
```
