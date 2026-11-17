# PICS Official Website - MySQL Database

## 1. Database Information

Database Name: pics_database
Database Type: MySQL
Character Set: utf8mb4
Collation: utf8mb4_unicode_ci

## 2. Database Modules

The database supports the following modules:

1. Events
2. Participants
3. Registrations
4. Accounts
5. Payments

## 3. Database Creation

Open MySQL Workbench or MySQL Command Line.

Run:

SOURCE path/to/mysql_schema.sql;

Or execute the SQL statements manually.

## 4. Django Database Integration

Django connects to MySQL using the database
configuration in config/pics_settings.py.

Database credentials are stored in the .env file.

## 5. Database Tables

Django migrations will create the tables
based on the application models.

## 6. Migration Commands

Run these commands from the backend folder:

python manage.py makemigrations
python manage.py migrate

## 7. Database Connection Test

Run:

python manage.py shell

Then:

from database.mysql_connection import check_database_connection

check_database_connection()

## 8. Security

- Never upload .env to GitHub.
- Never store plain-text passwords.
- Never store card numbers or CVV.
- Store payment gateway transaction references.
- Use Django migrations to manage database tables.