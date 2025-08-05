# Code Challenge Generator

**Code Challenge Generator** is a full-stack web application for generating, solving, and reviewing AI-powered coding multiple-choice challenges.

---

## 🛠️ Technologies

- **Frontend:** React, React Router, Clerk (authentication), Vite
- **Backend:** FastAPI, SQLAlchemy, OpenAI API, Clerk Backend API, SQLite, Python 3.12
- **Other:** Svix (webhooks), `dotenv`, [`uv`](https://github.com/astral-sh/uv) (Python package manager)

---

## 📁 Folder Structure

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

## ⚙️ Setup Instructions

### 1. Prerequisites

Make sure you have the following installed:

- Python 3.12+
- Node.js 18+
- [`uv`](https://github.com/astral-sh/uv) (Python package manager)
- [ngrok](https://ngrok.com/) (for Clerk webhooks)
- OpenAI API key
- Clerk account: [https://clerk.com/](https://clerk.com/)

---

### 2. Clone the Repository

```sh
git clone https://github.com/JohanMunozMendez/code-challenge-generator.git
cd code-challenge-generator
```

---

### 3. Backend Setup

```sh
cd backend
cp .env.example .env
# Fill in the required environment variables in .env
uv venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r pyproject.toml
```

#### Required `.env` Variables:

- `OPENAI_API_KEY`: Get it from [OpenAI Dashboard](https://platform.openai.com/)
- `CLERK_SECRET_KEY`: Clerk secret key (private)
- `JWT_KEY`: Clerk JWT verification key (starts with `pk_...`)
- `CLERK_WEBHOOK_SECRET`: Webhook secret for verifying `user.created` events

#### Run Backend:

```sh
uv run server.py
```

> The FastAPI server will run at [http://localhost:8000](http://localhost:8000)

#### Clerk Webhooks (ngrok)

To receive Clerk webhooks locally, you need to expose your backend using ngrok:

```sh
ngrok http 8000
```

Copy the generated HTTPS URL and set it as your webhook endpoint in the Clerk dashboard.  
**Example:** If ngrok gives you `https://abc123.ngrok-free.app`, set your webhook URL as:

```
https://abc123.ngrok-free.app/webhooks/clerk
```

---

### 4. Frontend Setup

```sh
cd ../frontend
cp .env.example .env
# Add your VITE_CLERK_PUBLISHABLE_KEY
npm install
```

#### Required `.env` Variable:

- `VITE_CLERK_PUBLISHABLE_KEY`: Found in Clerk dashboard under **Developers > API Keys**

#### Run Frontend:

```sh
cd src
npm run dev
```

> The app will run at [http://localhost:5173](http://localhost:5173)

---

## 🔗 API Configuration

The frontend communicates with the backend through:

```
http://localhost:8000/api/
```

If needed, you can modify this in [`frontend/src/utils/api.js`](frontend/src/utils/api.js)

---

## 🚀 Usage Instructions

1. **Start the Backend:**

   ```sh
   cd backend && uv run server.py
   ```

2. **Start the Frontend:**

   ```sh
   cd frontend && npm run dev
   ```

3. **Open in Browser:**  
   [http://localhost:5173](http://localhost:5173)

4. **Authenticate:**  
   Sign up or log in using Clerk authentication.

5. **Generate a Challenge:**

   - Select difficulty and generate a coding challenge.
   - Choose your answer from multiple-choice options.
   - See explanations and your progress in the history section.

6. **Daily Quota System:**  
   Each user has a limited number of challenges per day. The quota resets every 24 hours.
