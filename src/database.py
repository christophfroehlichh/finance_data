import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")

def connect_db():
    try:
        connect = psycopg2.connect(database_url)
        print("Erfolgreich mit der Datenbank verbunden")
        connect.close()
        print("Und wieder getrennt")
    except Exception as e:
        print(e)
        print("Datenbank Verbindung ist fehlgeschlagen")


if __name__ == "__main__":
    connect_db()

