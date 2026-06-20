import sqlite3

DB_NAME = "packetsentry.db"

def create_table():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS alerts (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            attacker_ip TEXT,

            scanned_ports INTEGER,

            severity TEXT,

            timestamp TEXT
        )

    """)

    conn.commit()

    conn.close()


def insert_alert(attacker_ip, scanned_ports, severity, timestamp):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO alerts (
            attacker_ip,
            scanned_ports,
            severity,
            timestamp
        )

        VALUES (?, ?, ?, ?)

    """, (

        attacker_ip,
        scanned_ports,
        severity,
        timestamp

    ))

    conn.commit()

    conn.close()


def get_all_alerts():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM alerts
        ORDER BY id DESC

    """)

    alerts = cursor.fetchall()

    conn.close()

    return alerts
