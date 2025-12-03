# High-Performance Search Engine API

A lightweight, read-heavy search API built with **Python (Flask)**. Designed to handle high-traffic queries with sub-100ms latency using in-memory caching.

**[View Live Demo](https://backend-search-assignment.onrender.com/search?q=a)**

## 🛠 Tech Stack
* **Framework:** Flask
* **Server:** Gunicorn (Production)
* **Language:** Python 3.9+
* **Deployment:** Render

## Features
* **<100ms Response Time:** Data is pre-fetched and cached in memory upon server start to eliminate external API bottlenecks during search.
* **Pagination:** Efficiently handles large datasets via `page` and `limit` parameters.
* **Case-Insensitive Search:** Flexible querying for better user experience.

## Quick Start

**1. Clone & Install**
```bash
git clone [https://github.com/mic175/backend-search-assignment.git](https://github.com/mic175/backend-search-assignment.git)
cd backend-search-assignment
python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
```

**2. Run Locally**
```bash
python app.py
```

**3. Test the Endpoint Open your browser:** 
```bash
http://127.0.0.1:5000/search?q=a&page=1&limit=5
```

---

## Engineering Decisions (Bonus)

### 1. Design Notes: Alternative Approaches
I considered three architectures for this search engine:
* **Live Fetching:** Fetching data from the source API on every request.
    * *Rejected because:* It introduces network latency (RTT), making the <100ms target impossible.
* **Database (PostgreSQL/SQLite):** Storing messages in a database.
    * *Rejected because:* Overkill for a small, static dataset. Database queries adds overhead compared to direct memory access.
* **In-Memory Caching (Selected):** Loading data into a global list on startup.
    * *Reasoning:* This offers **O(n)** search performance (or better) and zero network latency during searches, guaranteeing the fastest possible response time.

### 2. Latency Optimization: Reaching 30ms
To reduce latency from ~90ms to <30ms for a production-scale system, I would:
* **Use a Trie (Prefix Tree):** Instead of iterating through the entire list of messages (`O(n)`), I would index the words into a Trie structure. This allows lookup time proportional to the word length (`O(k)`), which is instant even with millions of records.
* **Edge Caching (CDN):** Place the API behind Cloudflare. Common searches (like "hello") would be served from a server close to the user's physical location, avoiding the round-trip to the main server entirely.
