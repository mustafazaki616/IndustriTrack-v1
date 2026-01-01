# IndustriTrack ERP

A comprehensive manufacturing ERP built with FastAPI and React.

## Project Structure
- `backend/`: FastAPI application
- `frontend/`: React + TypeScript frontend
- `infrastructure/`: Docker and orchestration files

## Setup
### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```
