# PICS Official Website – Backend

## 1. Project Overview

The PICS Official Website Backend is developed using Django and Django REST Framework.

It manages events, participants, registrations, user accounts, and payments through REST APIs.

## 2. Technology Stack

- Python
- Django
- Django REST Framework
- MySQL
- JWT Authentication
- REST APIs

## 3. Backend Structure

```text
backend/
│
├── config/
│
├── apps/
│   ├── events/
│   ├── participants/
│   ├── registrations/
│   ├── accounts/
│   └── payments/
│
├── database/
│
├── common/
│
├── manage.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── README.md
```

## 4. Main Modules

### Events
- Create and manage events.
- View event details.
- Update event information.

### Participants
- Store participant information.
- Manage participant profiles.
- Maintain participant records.

### Registrations
- Register participants for events.
- Maintain registration records.
- Track registration status.

### Accounts
- User signup and login.
- Manage user profiles.
- Authentication and permissions.

### Payments
- Store payment records.
- Track payment status.
- Maintain transaction references.
- Payment gateway integration.

## 5. Database

Database: MySQL

Database Name: `pics_database`

Database configuration is managed through environment variables in `.env`.

## 6. Installation

Install the required Python packages:

```bash
python -m pip install -r requirements.txt
```

Create your `.env` file using `.env.example` as a template.

Configure your MySQL database and credentials.

## 7. Database Setup

Execute the SQL file:

`database/mysql_schema.sql`

Then run Django migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 8. Run Development Server

```bash
python manage.py runserver
```

Backend development server:

`http://127.0.0.1:8000/`

## 9. Important Commands

Check project configuration:

```bash
python manage.py check
```

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Create admin user:

```bash
python manage.py createsuperuser
```

Run tests:

```bash
python manage.py test
```

## 10. Security Guidelines

- Never upload `.env` to GitHub.
- Keep database credentials private.
- Never store plain-text passwords.
- Never store card CVV or full card details.
- Use environment variables for secret keys.
- Validate incoming API requests.

## 11. Development Status

Backend modules are being developed incrementally.

Payment gateway integration, email verification, and additional security features can be integrated in later development stages.

---

**Project:** PICS Official Website  
**Backend:** Django REST Framework  
**Database:** MySQL