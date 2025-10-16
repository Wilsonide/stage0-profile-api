# 🐱 Hng Stage 0 – Profile API (FastAPI)

This is a simple **RESTful API** built with **FastAPI** that returns your profile information along with a **dynamic cat fact** fetched from the [Cat Facts API](https://catfact.ninja/fact).

It demonstrates:

- REST API design using **FastAPI**
- Integration with a third-party API
- Dynamic UTC timestamp generation

---

## 🚀 Features

✅ Returns your profile details (name, email, stack)  
✅ Fetches a **new random cat fact** on every request  
✅ Includes the **current UTC time** in ISO 8601 format (e.g. `2025-10-16T09:15:42.123Z`)  
✅ Handles network/API failures gracefully

---

## 🧩 API Endpoint

### `GET /me`

#### ✅ Example Successful Response

```json
{
  "status": "success",
  "user": {
    "email": "wilsonicheku@example.com",
    "name": "Wilson Icheku",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-16T09:15:42.123Z",
  "fact": "Cats can jump up to six times their length."
}
```

---

## 🧭 Setup Instructions and How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Wilsonide/stage0-profile-api.git
cd stage0-profile-api
```

### 2️⃣ install dependencies to your local

```bash
uv sync
```

make sure you have uv installed in your system.

### 3️⃣ Run the FastAPI server

```bash
python main.py
```

Your server will start at:
👉 http://localhost:8000
