# coding=utf-8
"""

"""

import sqlite3

class DbUtils(object):
    def __init__(self):
        self.conn = None
        self.transaction_count = 0

    def __enter__(self):
        self.conn = sqlite3.connect('../output/tweets.db')

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

    def setup_db(self):
        try:
            self.conn.execute("""
        CREATE TABLE users (
         screen_name TEXT,
         twitter_id INT,
         json_user_info TEXT,
         date_pulled TEXT)
           """)
        except sqlite3.OperationalError:
            pass

        try:
            self.conn.execute("""
    CREATE TABLE friends (
      screen_name TEXT,
      twitter_id INT,
      json_friends TEXT,
      date_pulled TEXT)""")
        except sqlite3.OperationalError:
            pass

        try:
            self.conn.execute("""
     CREATE TABLE tweets (
      screen_name TEXT,
      twitter_id INT,
      json_tweets TEXT,
      date_pulled TEXT)
        """)
        except sqlite3.OperationalError:
            pass

        try:
            self.conn.execute("""
        CREATE TABLE locations (
         location TEXT,
         normal_location TEXT,
         date_pulled TEXT)
           """)
        except sqlite3.OperationalError:
            pass

        try:
            self.conn.execute("""
        CREATE TABLE domains (
         domain TEXT,
         is_media_outlet TEXT)
           """)
        except sqlite3.OperationalError:
            pass
