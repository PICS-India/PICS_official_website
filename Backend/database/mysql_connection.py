from django.db import connection


def check_database_connection():

    try:
        connection.ensure_connection()

        print("MySQL Database Connected Successfully!")

        return True

    except Exception as error:

        print("MySQL Database Connection Failed!")
        print(error)

        return False


def get_database_info():

    try:
        with connection.cursor() as cursor:

            cursor.execute("SELECT DATABASE()")

            database_name = cursor.fetchone()

            print("Connected Database:", database_name[0])

    except Exception as error:

        print("Unable to fetch database information.")
        print(error)