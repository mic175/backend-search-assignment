# 🚀 High-Performance Search Engine API

A lightweight, read-heavy search API built with **Python (Flask)**. Designed to handle high-traffic queries with sub-100ms latency using in-memory caching.

**[👉 View Live Demo](https://backend-search-assignment.onrender.com/search?q=a)**

## 🛠 Tech Stack
* **Framework:** Flask
* **Server:** Gunicorn (Production)
* **Language:** Python 3.9+
* **Deployment:** Render

## ⚡ Features
* **<100ms Response Time:** Data is pre-fetched and cached in memory upon server start to eliminate external API bottlenecks during search.
* **Pagination:** Efficiently handles large datasets via `page` and `limit` parameters.
* **Case-Insensitive Search:** Flexible querying for better user experience.

## 🏃‍♂️ Quick Start

**1. Clone & Install**
```bash
git clone [https://github.com/mic175/backend-search-assignment.git](https://github.com/mic175/backend-search-assignment.git)
cd backend-search-assignment
python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt```

**2. Run Locally**
```bash

python app.py```

**3. Test the Endpoint Open your browser: http://127.0.0.1:5000/search?q=a&page=1&limit=5**
