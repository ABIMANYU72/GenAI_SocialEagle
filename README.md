# LinkedIn Job Scraper 🚀

A Python-based LinkedIn Job Scraper that automatically searches and extracts job listings from LinkedIn based on your preferred **job role** and **location**, then saves the results into an Excel file.

## 📌 Features

- 🔍 Search LinkedIn jobs by role and location
- 🤖 Automated job scraping
- 📄 Export scraped jobs to Excel format
- 🌐 Simple frontend using Streamlit
- ⚡ Backend API support

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Playwright
- Pandas
- Flask (based on your backend)

---

## 📂 Project Structure

```bash
project/
│
├── backend/
│   └── api.py
│
├── frontend/
│   └── app.py
|
└── README.md
```

---

## 🚀 How to Run the Project

### Step 1: Login to LinkedIn

First, run the file save_linkedin_session.py and authenticate yourself into your LinkedIn account and save the session.

### Step 2: Run the Backend API

Navigate to the backend folder and start the API server.

```bash
cd backend
python api.py
```

---

### Step 3: Run the Frontend

Open another terminal and start the Streamlit frontend.

```bash
cd frontend
streamlit run app.py
```

---

## 🎯 How It Works

1. Enter your desired:
   - Job Role
   - Location

2. The application:
   - Scrapes LinkedIn job listings
   - Collects relevant job details
   - Saves the results into an Excel file

---

## 📊 Output

The scraped job data will be exported as an Excel file containing details like:

- Job Title
- Company Name
- Location
- Job Link
- Posted Date
- and more...

---

## ⚠️ Disclaimer

This project is for educational purposes only. Please use responsibly and follow LinkedIn’s terms of service.

---

## 👨‍💻 Author

Developed by Abimanyu
