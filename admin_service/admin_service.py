import sqlite3
from sqlite3 import Error
import mysql.connector

def create_connection(db_file):
    mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE mydatabase")


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


