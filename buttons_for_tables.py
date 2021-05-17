from sqlite3 import Error
import sqlite3 

def handler_diag(cur, conn, entry, entry2):
    print("pressed diag")
    que =   """ INSERT INTO dialogues (theory_id, dialogue_text)
                VALUES(?, ?)
            """
    text =  entry.get()
    text2 = entry2.get()
    stri = (text, text2, )
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

def handler_qst(cur, conn, entry, entry2, entry3):
    print("pressed qst")
    que =   """ INSERT INTO questions (language_id, theory_id, question_text)
                VALUES(?, ?, ?)
            """
    text  = entry.get()
    text2 = entry2.get()
    text3 = entry3.get()
    stri = (text, text2, text3, )
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
    que =   """ INSERT INTO correct (question_id, answer_id, correct)
                VALUES(?, ?, ?)
            """
    text = entry.get()
    text2 = entry2.get()
    text3 = entry3.get()
    stri = (text, text2, text3, )
    cur.execute(que, stri)
    conn.commit() 

def handler_ans(cur, conn, entry):
    print("pressed ans")
    que =   """ INSERT INTO answers (answer_text)
                VALUES(?)
            """
    text = entry.get()
    stri = (text,)
    cur.execute(que, stri)
    conn.commit() 
