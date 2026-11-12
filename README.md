# GameTopUp KG

GameTopUp KG is a Flask-based gaming storefront for KGS currency with product catalog, user accounts, balance management, order flow, and admin panel.

## Features

- Premium gaming storefront UI
- Catalog with games and products
- Cart and checkout flow
- Manual payment proof handling
- SQLite database with SQLAlchemy
- Admin dashboard and role checks
- Account balance and transaction history
- Reviews and support page

## Local setup on Windows 11

1. Clone or open the project folder.
2. Create a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and update values.
5. Run the app:
   ```powershell
   python run.py
   ```
6. Open `http://127.0.0.1:5000`.

## Environment configuration

Create `.env` using:

```env
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///database/app.db
ADMIN_EMAIL=admin@gametopup.kg
```

## First admin user

The app seeds a default admin account automatically on first startup:

- Username: `admin`
- Email: `admin@gametopup.kg`
- Password: `Admin123!`

After logging in, change the password in the settings section.

## Production notes

- This project uses SQLite for local development and can be switched to PostgreSQL by updating the connection string.
- All balance mutations are protected server-side and are not editable from browser JavaScript.
- Payment uploads are restricted to safe image file types and limited to 16 MB.
