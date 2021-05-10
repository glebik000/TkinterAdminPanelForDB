from sqlite3 import Error
import sqlite3
dialogues   = str()
theory      = str()
questions   = str()
languages   = str()
correct     = str()
answers     = str()
tables  = [dialogues, theory, questions, languages, correct, answers]

tables[0]  =""" 
               CREATE TABLE IF NOT EXISTS dialogues (
                   dialogue_id INTEGER PRIMARY KEY, 
                   theory_id INTEGER PRIMARY KEY, 
                   dialogue_text TEXT
                   );
            """
tables[1]  ="""
                CREATE TABLE IF NOT EXISTS theory (
                   theory_id INTEGER PRIMARY KEY,
                   theory_text TEXT
                   );
            """
tables[2]  ="""
                CREATE TABLE IF NOT EXISTS questions (
                   language_id INTEGER PRIMARY KEY,
                   question_id ITEGER PRIMARY KEY,
                   theory_id ITEGER PRIMARY KEY,
                   question_text TEXT
                   );
            """
tables[3]  ="""
                CREATE TABLE IF NOT EXISTS languages (
                   language_id INTEGER PRIMARY KEY,
                   language_name TEXT
                   );
            """
tables[4]  ="""
                CREATE TABLE IF NOT EXISTS correct (
                   question_id INTEGER PRIMARY KEY,
                   answer_id INTEGER PRIMARY KEY,
                   correct BOOLEAN
                   );
            """
tables[5]  ="""
                CREATE TABLE IF NOT EXISTS answers (
                   answer_id INTEGER PRIMARY KEY,
                   answer_text TEXT
                   );
            """

def create_connection(): 
    """ Create a database connection in current directory"""
    return sqlite3.connect("data.db")

def create_table(conn):
    """ Create a table """
    with conn:
        for table in tables:
            conn.execute(table)

