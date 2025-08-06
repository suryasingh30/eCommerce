# 🛒 Django E-commerce Backend

A modular, RESTful e-commerce backend built with Django and Django REST Framework, featuring:

- 🔐 JWT authentication (Simple JWT)  
- 🧩 Modular apps: `users`, `products`, `cart`, `orders`, `wishlist`  
- 👥 Admin vs. Customer roles (`is_admin` flag)  
- 🔎 Products & Categories with slug‐based filtering, search, ordering, pagination  
- 📊 “Most sold” / “Least sold” reporting for admins  
- 🛒 Cart & Checkout flow  
- 🧾 Order history with total price calculation  
- ❤️ Wishlist management  
- 🐘 PostgreSQL deployment-ready (Render)

---

## ⚡ Quick Start

### 1. Clone the Repo
```bash
git clone https://github.com/suryasingh30/eCommerce.git
cd eCommerce/backend
2. Create & Activate Virtual Environment
bash
Copy
Edit
# Create virtual environment
python -m venv .venv

# Activate
# macOS/Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in backend/ with the following:

ini
Copy
Edit
DJANGO_SECRET_KEY=your-django-secret-key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,your-render-app.onrender.com
DATABASE_URL=postgres://username:password@host:port/dbname
5. Apply Migrations & Create Superuser
bash
Copy
Edit
python manage.py migrate
python manage.py createsuperuser
6. Run the Development Server
bash
Copy
Edit
python manage.py runserver
📁 Project Structure
bash
Copy
Edit
backend/
├── backend/           # Django project (settings, wsgi, urls)
├── users/             # Authentication & User model
├── products/          # Products & Categories + reporting
├── cart/              # Shopping cart & checkout
├── orders/            # Orders & order history
├── wishlist/          # Wishlist feature
├── manage.py
├── requirements.txt
├── Procfile           # Render deployment
└── .env               # Local env vars (not committed)
🚀 Deployment on Render
Set Project Root to backend/

Ensure requirements.txt & Procfile are inside backend/

Set Build Command:

bash
Copy
Edit
pip install -r requirements.txt
Set Start Command:

bash
Copy
Edit
gunicorn backend.wsgi
Add Environment Variables:

DJANGO_SECRET_KEY

DATABASE_URL

DEBUG=False

ALLOWED_HOSTS

🔗 API Endpoints
🔐 Authentication
POST /api/auth/register/ — Register user

POST /api/auth/login/ — Obtain JWT tokens

POST /api/auth/refresh/ — Refresh token

🛍️ Products & Categories
GET /api/products/ — List, search, filter, order products

POST /api/products/ — Create product (Admin only)

GET /api/products/{id}/ — Product detail

PUT/PATCH /api/products/{id}/ — Update product (Admin)

DELETE /api/products/{id}/ — Delete product (Admin)

Categories
GET /api/products/categories/ — List categories

POST /api/products/categories/ — Create category (Admin)

GET /api/products/categories/{id}/ — Category detail

PUT/PATCH /api/products/categories/{id}/ — Update (Admin)

DELETE /api/products/categories/{id}/ — Delete (Admin)

Reports
GET /api/products/reports/products/ — Sales report: most/least sold (Admin)

🛒 Cart & Checkout
POST /api/cart/add/ — Add/update cart item

GET /api/cart/ — View cart

POST /api/cart/checkout/ — Checkout & clear cart

📦 Orders
GET /api/orders/ — View user's order history (with total price)

❤️ Wishlist
GET /api/wishlist/ — View wishlist

POST /api/wishlist/ — Add to wishlist

DELETE /api/wishlist/ — Remove from wishlist

---

## 🔗 Documentation Link

For the latest version of this documentation, visit:  
[E-commerce API Documentation on Notion](https://www.notion.so/E-commerce-API-Documentation-2479ba7bca148060b165c618babb77ed?source=copy_link)
