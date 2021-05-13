from functools import partial
import tkinter as ui
from database import *

def handler(name, cur, conn):
    window = ui.Tk()
    window.rowconfigure(1, weight=1,minsize=5)
    my_frame = ui.Frame(master=window, 
            borderwidth=5)
    entry = ui.Entry(master=my_frame,
           width=50)
    if name == "dialogues":
        label = ui.Label(master=my_frame,
                text="dialogue text",
                width=10)

        que =   """ INSERT INTO dialogues (dialogue_text)
                    VALUES(?)
                """
        stri = ('test text 1',)
        cur.execute(que, stri)
        conn.commit() 

    elif name == "theory":
        label = ui.Label(master=my_frame,
                text="theory text",
                width=10)

        que =   """ INSERT INTO theory (theory_text)
                    VALUES(?)
                """
        stri = ('just a test',)
        cur.execute(que, stri)
        conn.commit() 

    elif name == "questions":
        label = ui.Label(master=my_frame,
                text="question text",
                width=10)
    elif name == "languages":
        label = ui.Label(master=my_frame,
                text="language name",
                width=15)
    elif name == "correct":
        label = ui.Label(master=my_frame,
                text="is correct",
                width=10)
    elif name == "answers":
        label = ui.Label(master=my_frame,
                text="answer text",
                width=10)
    my_frame.grid(row=0, column=0)
    label.grid(row=0, column=0)
    entry.grid(row=0, column=1)
    window.mainloop()

class start_window:
    conn = create_connection()
    create_table(conn)
    table_names = ("dialogues", "theory", "questions", "languages", "correct", "answers")
    #print("checking conn: ", conn)
    cur = conn.cursor()
    window = ui.Tk()
    for i in range(6):
        window.rowconfigure(i, weight=1,minsize=5)
        my_frame = ui.Frame(master=window, 
                relief=ui.RAISED, 
                borderwidth=5)
        my_frame.grid(row=i)
        button = ui.Button(master=my_frame,
                text=f"{table_names[i]}", 
                width=25,
                command=partial(handler, table_names[i], cur, conn)
                )
        button.pack(padx=5, pady=5)
    window.mainloop()
    conn.close()


if __name__ == '__main__':

    app = start_window()
    print("Test app");
