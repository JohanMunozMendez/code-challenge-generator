# Code Challenge Generator

**Code Challenge Generator** is a full-stack web application for generating, solving, and reviewing AI-powered coding multiple-choice challenges. Authenticated users can practice, generate, and track their coding progress, with a daily quota system. This project is ideal for developers and educators seeking to practice or create programming questions.

---

## Technologies Used

- **Frontend:** React, React Router, Clerk (authentication), Vite
- **Backend:** FastAPI, SQLAlchemy, OpenAI API, Clerk Backend API, SQLite, Python 3.12
- **Other:** Svix (webhooks), dotenv, [uv](https://github.com/astral-sh/uv) (Python package manager)

---

## Folder Structure

```
.
├── backend/   # FastAPI backend (API, database, AI integration)
│   ├── src/
│   │   ├── ai_generator.py
│   │   ├── app.py
│   │   ├── utils.py
│   │   ├── database/
│   │   └── routes/
│   ├── database.db
│   ├── pyproject.toml
│   └── server.py
└── frontend/  # React frontend (UI, authentication)
    ├── src/
    │   ├── App.jsx
    │   ├── challenge/
    │   ├── history/
    │   ├── layout/
    │   ├── auth/
    │   └── utils/
    ├── index.html
    ├── package.json
    └── vite.config.js
```

---

## Setup Instructions

### Prerequisites

- Python 3.12+
- Node.js 18+
- [uv](https://github.com/astral-sh/uv) (for Python dependency management)
- [OpenAI API key](https://platform.openai.com/)
- [Clerk account](https://clerk.com/) for authentication

---

### 1. Clone the Repository

```sh
git clone https://github.com/JohanMunozMendez/code-challenge-generator.git
cd code-challenge-generator
```

---

### 2. Backend Setup

```sh
cd backend
cp .env.example .env
# Edit .env and fill in your CLERK_SECRET_KEY, JWT_KEY, OPENAI_API_KEY, CLERK_WEBHOOK_SECRET
uv venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r pyproject.toml
```

**Run the backend locally:**

```sh
python server.py
```

> The FastAPI server will start at [http://localhost:8000](http://localhost:8000).

---

### 3. Frontend Setup

```sh
cd ../frontend
cp .env.example .env
# Edit .env and set your VITE_CLERK_PUBLISHABLE_KEY from Clerk
npm install
```

**Run the frontend locally:**

```sh
npm run dev
```

> The React app will be available at [http://localhost:5173](http://localhost:5173).

---

## API Base URL

The frontend expects the backend API at:

```
http://localhost:8000/api/
```

You can change this in [`frontend/src/utils/api.js`](frontend/src/utils/api.js) if needed.

---

## Build & Deployment

### Frontend

To build the frontend for production:

```sh
npm run build
```

The output will be in the `frontend/dist` directory.

### Backend

The backend is ready for deployment with any ASGI server (e.g., Uvicorn, Gunicorn).  
For production, configure environment variables securely and use a production-ready database.

---

## Usage Instructions

1. **Start the backend:**  
   `cd backend && python server.py`

2. **Start the frontend:**  
   `cd frontend && npm run dev`

3. **Open your browser:**  
   Visit [http://localhost:5173](http://localhost:5173)

4. **Sign up or sign in** using Clerk authentication.

5. **Generate a challenge:**

   - Select a difficulty and click "Generate Challenge".
   - Answer the multiple-choice question.
   - View explanations and your challenge history.

6. **Quota:**  
   Each user has a daily quota of challenges. The quota resets every 24 hours.

---

## Environment Variables

### Backend

Copy the example file and fill in your secrets:

```sh
cp backend/.env.example backend/.env
```

Required variables:

- `CLERK_SECRET_KEY`
- `JWT_KEY`
- `OPENAI_API_KEY`
- `CLERK_WEBHOOK_SECRET`

### Frontend

Copy the example file and fill in your Clerk publishable key:

```sh
cp frontend/.env.example frontend/.env
```

Required variable:

- `VITE_CLERK_PUBLISHABLE_KEY`

## How to Get Environment Variables

You’ll need the following secrets:

### 🔑 OpenAI Project API Key

1. Go to [https://platform.openai.com/](https://platform.openai.com/)
2. Select or create a **project** under your organization
3. Navigate to **API Keys** within that project
4. Create a **Project API Key** (starts with `sk-`)
5. Paste it into your `backend/.env` file as:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 🧑‍💼 Clerk Credentials

Create a Clerk account at [https://clerk.com/](https://clerk.com/) and set up a application. Then gather the following:

#### For the Backend (`backend/.env`):

- `CLERK_SECRET_KEY`: Your Clerk secret API key (keep this private)
- `JWT_KEY`: This is your Clerk **JWT verification key** (starting with `pk_...`)
- `CLERK_WEBHOOK_SECRET`: The secret used to verify the **user.created** subscribed event

#### For the Frontend (`frontend/.env`):

- `VITE_CLERK_PUBLISHABLE_KEY`: The public key used on the frontend to connect to Clerk

You can find these values in your app's configure dashboard under **Developers** > **API Keys** or **Webhooks**.
