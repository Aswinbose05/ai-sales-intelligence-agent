"""
Signal Database
Stores all extracted buying intent signals.
"""

import sqlite3
from src.config import DATABASE_PATH


class SignalDatabase:

    def __init__(self):

        self.conn = sqlite3.connect(DATABASE_PATH)

        self.cursor = self.conn.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS signals(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            company TEXT,

            signal_type TEXT,

            evidence TEXT,

            confidence REAL,

            reason TEXT,

            query_type TEXT,

            page_type TEXT,

            title TEXT,

            url TEXT

        )
        """)

        self.conn.commit()

    def insert(self, signal):

        self.cursor.execute("""
        INSERT INTO signals(

            company,
            signal_type,
            evidence,
            confidence,
            reason,
            query_type,
            page_type,
            title,
            url

        )

        VALUES(?,?,?,?,?,?,?,?,?)

        """, (

            signal.get("company", ""),
            signal.get("signal_type", ""),
            signal.get("evidence", ""),
            signal.get("confidence", 0),
            signal.get("reason", ""),
            signal.get("query_type", ""),
            signal.get("page_type", ""),
            signal.get("title", ""),
            signal.get("url", "")

        ))

        self.conn.commit()

    def get_all(self):

        self.cursor.execute("""
        SELECT *
        FROM signals
        """)

        return self.cursor.fetchall()

    def get_company(self, company):

        self.cursor.execute("""
        SELECT *
        FROM signals
        WHERE company=?
        """, (company,))

        return self.cursor.fetchall()

    def delete_all(self):

        self.cursor.execute("""
        DELETE FROM signals
        """)

        self.conn.commit()

    def count(self):

        self.cursor.execute("""
        SELECT COUNT(*)
        FROM signals
        """)

        return self.cursor.fetchone()[0]

    def close(self):

        self.conn.close()


if __name__ == "__main__":

    db = SignalDatabase()

    print("Rows :", db.count())

    db.close()