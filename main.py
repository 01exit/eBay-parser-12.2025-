from flask import Flask, render_template, request, redirect, url_for
from db.db import Base, engine, SessionLocal
from db.models import Product
from parser.ebay_playwright import parse_ebay

app = Flask(__name__)
Base.metadata.create_all(bind=engine)

@app.route('/', methods=['GET', 'POST'])
def index():
    db = SessionLocal()
    products = None
    try:
        action = request.form.get("action")
        if action == "parse":
            query = request.form.get('query')
            limit = int(request.form.get("limit", 5))
            if query:
                raw = parse_ebay(query, limit=limit)
                products = []
                for r in raw:
                    p = Product(name=r["name"], price=r["price"], url=r["url"])
                    db.add(p)
                    products.append(p)
                db.commit()
                return render_template('index.html', products=products)
        elif action == "show_db":
            products = db.query(Product).all()
        elif action == "clear_db":
            db.query(Product).delete()
            db.commit()
            return redirect(url_for('index'))
        return render_template('index.html',  products=products)
    finally:
        db.close()

if __name__ == "__main__":
    app.run(debug=True)