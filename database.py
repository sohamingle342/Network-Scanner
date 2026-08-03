import sqlite3
from datetime import datetime


DATABASE_NAME = "scan_history.db"


# Create Database
def create_database():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scans (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        target_ip TEXT,

        status TEXT,

        operating_system TEXT,

        ports_found INTEGER,

        scan_duration TEXT,

        scan_date TEXT

    )
    """)


    connection.commit()

    connection.close()



# Save Scan Result
def save_scan(
        ip,
        status,
        os_name,
        port_count,
        scan_time
):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()


    cursor.execute("""

    INSERT INTO scans
    (
        target_ip,
        status,
        operating_system,
        ports_found,
        scan_duration,
        scan_date
    )

    VALUES (?, ?, ?, ?, ?, ?)

    """,

    (
        ip,
        status,
        os_name,
        port_count,
        f"{scan_time:.2f} seconds",
        datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    ))


    connection.commit()

    connection.close()



# View Scan History
def show_history():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()


    cursor.execute(
        "SELECT * FROM scans"
    )


    records = cursor.fetchall()


    print("\n========== SCAN HISTORY ==========\n")


    for row in records:

        print(
            f"ID: {row[0]}"
        )

        print(
            f"IP: {row[1]}"
        )

        print(
            f"Status: {row[2]}"
        )

        print(
            f"OS: {row[3]}"
        )

        print(
            f"Ports Found: {row[4]}"
        )

        print(
            f"Duration: {row[5]}"
        )

        print(
            f"Date: {row[6]}"
        )

        print("-"*40)


    connection.close()

create_database()
