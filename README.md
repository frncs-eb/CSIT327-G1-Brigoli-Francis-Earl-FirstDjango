# CampusConnect

## Project Information

- **Name:** Francis Earl S. Brigoli
- **Section:** G1

## Overview

**CampusConnect** is a Django web application for campus community members. It includes student and administrator roles, a dashboard, account registration, and a profile page where signed-in users can update their own details. The interface uses Bootstrap 5 from a CDN with custom styling.

### Key Features

1. **User accounts and profiles**
   - Register with a username, email, name, course, and password.
   - View and update your own profile at `/accounts/profile/`.
   - Profile updates are limited to the currently signed-in user.
2. **Dashboard**
   - A login-protected dashboard shows the account role, course, last login, and community member count.
3. **Role-based admin panel**
   - The admin panel at `/admin-panel/` is available only to accounts with the Administrator role.
   - User accounts and roles can be managed through Django Admin at `/admin/`.
4. **Feedback and security**
   - Successful registration displays a Django message on the login page.
   - Forms include CSRF protection, and Django's configured password validators apply during sign-up.
5. **Responsive interface**
   - Shared navigation and page templates are styled with Bootstrap 5 CSS and custom styles in `templates/base.html`.

---

## Project Structure

```text
brigoli-campusconnect/
├── manage.py
├── README.md
├── requirements.txt
├── .gitignore
├── accounts/                 # Custom user model, forms, and account views
├── campusconnect/            # Django settings and root URL configuration
├── dashboard/                # Dashboard and administrator panel
└── templates/
    ├── base.html
    ├── dashboard/
    │   ├── admin_panel.html
    │   └── home.html
    └── registration/
        ├── login.html
        ├── profile.html
        └── signup.html
```

---

## Steps to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/frncs-eb/CSIT327-G1-Brigoli-Francis-Earl-FirstDjango.git
cd CSIT327-G1-Brigoli-Francis-Earl-FirstDjango
```

### 2. Create and activate a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. (Optional) Create an administrator account

```bash
python manage.py createsuperuser
```

Creating a Django superuser grants access to Django Admin. To use the CampusConnect admin panel, sign in to Django Admin, open the account, and set its **Role** to **Administrator**.

### 6. Run the development server

```bash
python manage.py runserver
```

Open **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** in your browser.

---

## Testing the App

1. Open `/accounts/signup/`, register an account, and confirm the success message appears on the login page.
2. Log in at `/accounts/login/` and visit the dashboard.
3. Open **Profile**, update an account detail, and save your changes.
4. Log out and visit `/accounts/profile/`; you should be redirected to log in.
5. To try the administrator panel, create a superuser, set its role to **Administrator** in Django Admin, then visit `/admin-panel/`.

Run the automated tests with:

```bash
python manage.py test
```

---

## Tech Stack

- Python
- Django
- SQLite (development database)
- Bootstrap 5 CSS (CDN) and custom CSS

---