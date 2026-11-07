Name: Francis Earl S. Brigoli
Section: G1

## Run the project

1. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Apply database migrations and start the development server:
   ```powershell
   python manage.py migrate
   python manage.py runserver
   ```
4. Open http://127.0.0.1:8000/ in your browser.