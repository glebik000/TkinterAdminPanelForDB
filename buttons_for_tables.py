from sqlite3 import Error
import sqlite3 

def handler_diag(cur, conn, entry):
    print("pressed diag")
    que =   """ INSERT INTO dialogues (dialogue_text)
                VALUES(?)
            """
    text = entry.get()
    stri = (text,)
    cur.execute(que, stri)
    conn.commit() 

def handler_thr(cur, conn, entry):
    print("pressed thr")
    que =   """ INSERT INTO theory (theory_text)
                VALUES(?)
            """
    text = entry.get()
    stri = (text,)
    cur.execute(que, stri)
    conn.commit() 

def handler_qst(cur, conn, entry):
    print("pressed qst")
    que =   """ INSERT INTO questions (question_text)
                VALUES(?)
            """
    text = entry.get()
    stri = (text,)
    cur.execute(que, stri)
    conn.commit() 

def handler_lang(cur, conn, entry):
    print("pressed lang")
    que =   """ INSERT INTO languages (language_name)
                VALUES(?)
            """
    text = entry.get()
    stri = (text,)
    cur.execute(que, stri)
    conn.commit() 

def handler_cor(cur, conn, entry, entry2, entry3):
    print("pressed cor")
    #que =   """ INSERT INTO correct (correct)
    #            VALUES(?)
    #        """
    #text = entry.get()
    #stri = (text,)
    #cur.execute(que, stri)
    #conn.commit() 

def handler_ans(cur, conn, entry):
    print("pressed ans")
    que =   """ INSERT INTO answers (answer_text)
                VALUES(?)
            """
    text = entry.get()
    stri = (text,)
    cur.execute(que, stri)
    conn.commit() 
