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
                   dialogue_id  INTEGER    PRIMARY KEY AUTOINCREMENT, 
                   theory_id    integer,
                   dialogue_text TEXT,
                   FOREIGN KEY (theory_id) REFERENCES theory(theory_id)
                   );
            """
tables[1]  ="""
                CREATE TABLE IF NOT EXISTS theory (
                   theory_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   theory_text TEXT
                   );
            """
tables[2]  ="""
                CREATE TABLE IF NOT EXISTS questions (
                   question_id  INTEGER    PRIMARY KEY AUTOINCREMENT,
                   language_id  INT ,
                   theory_id    INT ,  
                   question_text TEXT,
                   FOREIGN KEY (language_id)   REFERENCES languages(language_id),
                   FOREIGN KEY (theory_id)     REFERENCES theory   (theory_id)
                   );
            """
tables[3]  ="""
                CREATE TABLE IF NOT EXISTS languages (
                   language_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   language_name VARCHAR(10)
                   );
            """
tables[4]  ="""
                CREATE TABLE IF NOT EXISTS correct (
                   correct_id   INTEGER  PRIMARY KEY AUTOINCREMENT,
                   answer_id    INT, 
                   question_id  INT,
                   correct BOOLEAN,
                   FOREIGN KEY (answer_id)    REFERENCES answers(answer_id),
                   FOREIGN KEY (question_id)  REFERENCES questions(question_id)
                   );
            """
tables[5]  ="""
                CREATE TABLE IF NOT EXISTS answers (
                   answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   answer_text VARCHAR(100)
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

