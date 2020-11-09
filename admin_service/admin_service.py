import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


class Admin:

    def __init__(self):
        self.email = "random@uchicago.edu"
        self.password = "123"
        self.adminID = "randomID"
    def login(self, email, password):
        pass
    def logout(self):
        pass
    def remove_user(self, user_id):
        pass
    def block_user(self, user_id):
        pass
    def unblock_user(self, user_id):
        pass
    def view_disputes(self, user_id):
        pass
    def process_refund_request(self, user_id, amount):
        pass
    def respond_user_email(self, user_email, emailID, subject, body):
        pass
    def view_flagged_items(self):
        pass
    def view_metrics(self):
        pass
    def add_category(self, category_name):
        pass
    def modify_category(self, old_category_name, new_category_name):
        pass
    def delete_category(self, category_name):
        pass


