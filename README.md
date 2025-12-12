# eBay-parser-12.2025-
A price scraper for eBay built with **Python + Playwright** to bypass anti-bot protection and collect real-time product prices.

# 🛒 Price Parser (eBay Scraper)
---

## 🚀 Features

- ✅ eBay product scraping
- ✅ Cloudflare / anti-bot bypass via Playwright
- ✅ Web interface via **Flask** (previously CLI)
  - Search products directly from browser
  - Show stored database
  - Clear database
  - Select number of results (1–10)
- ✅ SQLite database storage
- ✅ Modular project architecture
- ✅ Dynamic page parsing

---

## 📁 Project Structure
```
├── main.py           # Flask web application + optional CLI
├── db/
│   ├── db.py        # Database session & engine
│   └── models.py    # SQLAlchemy models
├── parser/
│   └── ebay_playwright.py # eBay scraper
├── templates/
│   └── index.html   # Web interface
├── requirements.txt # Dependencies
└── products.db  # SQLite database
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository
bash 
`git clone https://github.com/01exit/eBay-parser-12.2025-.git cd eBay-parser-12.2025-`

2️⃣ Install dependencies
`pip install -r requirements.txt`

3️⃣ Install Playwright browsers
`playwright install`

▶️ Usage
`python main.py`
Open your browser and go to `http://127.0.0.1:5000/`
You can:
  Search products
  View saved products
  Clear database
  Select number of results (1–10)

