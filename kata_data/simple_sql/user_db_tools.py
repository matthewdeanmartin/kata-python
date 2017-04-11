# coding=utf-8
# coding=utf-8
"""
Just the SQL code.
"""

# coding=utf-8
import json
import sqlite3
from datetime import datetime


class FriendFetcherDb(object):
    def __init__(self):
        self.conn = None
        self.transaction_count = 0

    def __enter__(self):
        self.conn = sqlite3.connect('../output/friends.db')

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn is not None:
            try:
                self.conn.commit()
            except:
                pass

            self.conn.close()


    def ad_hoc(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()

    def fetch_user_infos(self):
        cursor = self.conn.cursor()
        results = cursor.execute("""
                        SELECT * FROM user_infos
                    """)
        results = results.fetchall()
        return results


    def time_to_commit(self):
        self.transaction_count += 1
        if self.transaction_count % 100:
            self.conn.commit()


    def setup_db(self):
        try:
            self.conn.execute("""
    CREATE TABLE users (
      screen_name TEXT,
      twitter_id INT,
      location TEXT,
      city TEXT,
      state TEXT,
      country TEXT)""")
        except sqlite3.OperationalError:
            pass


        try:
            self.conn.execute("""
        CREATE TABLE locations (
         location TEXT,
         normal_location TEXT)
           """)
        except sqlite3.OperationalError:
            pass

