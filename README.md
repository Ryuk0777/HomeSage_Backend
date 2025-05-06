# 🧠 HomeSage Backend

Welcome to the backend of **HomeSage** — a machine learning-powered API for predicting house prices in 🇮🇳 **India**, 🇲🇾 **Malaysia**, and 🇺🇸 **America**.

This API is built with **FastAPI** and integrates trained models to provide fast and reliable real estate price estimations.

🔗 **Frontend Repo:** [HomeSage Frontend](https://github.com/yourusername/HomeSage)  
🌐 **Live App:** [https://homesage.onrender.com](https://homesage.onrender.com)

---

## 🚀 Features

- 🌍 Predicts house prices for **India**, **Malaysia**, and **America**
- ⚡ Asynchronous & fast with **FastAPI**
- 🧠 Integrates ML models for accurate pricing
- 💡 JSON input → prediction output
- 🧪 Easy to test via Swagger, Postman, or cURL

---

## 📓 Model Training Notebooks

See how each country's model was trained using the links below:

- 🇮🇳 **India:** [Colab Notebook](https://colab.research.google.com/drive/1SVXLcjfpyN0StQq5xFW7aVFrS6SyLfnb?usp=sharing)
- 🇲🇾 **Malaysia:** [Colab Notebook](https://colab.research.google.com/drive/1TkAepg1201hif3nC4uKddHEGWL3KZh3R?usp=sharing)
- 🇺🇸 **America:** [Colab Notebook](https://colab.research.google.com/drive/1Afn9kzbwAQtHskk0XfB1OCM8L4THe4cG?usp=sharing)

---

## 🛠️ Tech Stack

- 🐍 **Python 3**
- ⚙️ **FastAPI** – Web framework
- 📦 **Pydantic** – Input validation
- 🧠 **Scikit-learn** – ML models
- 🔁 **Joblib / Pickle** – For saving/loading trained models
- 🚀 **Uvicorn** – ASGI server

---

## 📦 Installation

### 1. Clone the Repo

```bash
git clone https://github.com/Ryuk0777/HomeSage_Backend.git
cd HomeSage_Backend
```

### 2. Create a Virtual Environment

**💻 On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**🐧 On Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Requirements

**💻 On Windows:**

```bash
pip install -r requirements.txt
```

**🐧 On Linux/macOS:**

```bash
pip3 install -r requirements.txt
```

### ▶️ Run the API Server

```bash
uvicorn main:app --reload
```

### 🌐 Local Development URLs

- 📍 **Base URL:** [http://127.0.0.1:8000](http://127.0.0.1:8000)  
- 🔧 **Swagger UI (API Docs):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


