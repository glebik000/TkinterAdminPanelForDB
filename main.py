from functools import partial
from buttons_for_tables import *
import tkinter as ui
from database import *

def handler(name, cur, conn):
    window = ui.Tk()
    window.rowconfigure(1, weight=1,minsize=5)
    my_frame = ui.Frame(master=window, 
            borderwidth=5)
    if name == "dialogues":
        entry = ui.Entry(master=my_frame,
               width=50)
        label = ui.Label(master=my_frame,
                text="dialogue text",
                width=10)
        button = ui.Button(master=my_frame,
                           text="INSERT",
                           width=15,
                           command=partial(handler_diag, cur, conn, entry)
                           )
        my_frame.grid(row=0, column=0)
        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        button.grid(row=1)
        window.mainloop()
    elif name == "theory":
        entry = ui.Entry(master=my_frame,
               width=50)
        label = ui.Label(master=my_frame,
                text="theory text",
                width=10)
        button = ui.Button(master=my_frame,
                           text="INSERT",
                           width=15,
                           command=partial(handler_thr, cur, conn, entry)
                           )
        my_frame.grid(row=0, column=0)
        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        button.grid(row=1)
        window.mainloop()
    elif name == "questions":
        entry = ui.Entry(master=my_frame,
               width=50)
        label = ui.Label(master=my_frame,
                text="question text",
                width=10)
        button = ui.Button(master=my_frame,
                           text="INSERT",
                           width=15,
                           command=partial(handler_qst, cur, conn, entry)
                           )
        my_frame.grid(row=0, column=0)
        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        button.grid(row=1)
        window.mainloop()
    elif name == "languages":
        entry = ui.Entry(master=my_frame,
               width=50)
        label = ui.Label(master=my_frame,
                text="language name",
                width=15)
        button = ui.Button(master=my_frame,
                           text="INSERT",
                           width=15,
                           command=partial(handler_lang, cur, conn, entry)
                           )
        my_frame.grid(row=0, column=0)
        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        button.grid(row=1)
        window.mainloop()
    elif name == "correct":
        entry = ui.Entry(master=my_frame,
               width=5)
        label = ui.Label(master=my_frame,
                text="is correct",
                width=10)
        label2 = ui.Label(master=my_frame,
                text="ID",
                width=5)
        entry2 = ui.Entry(master=my_frame,
               width=5)
        label3 = ui.Label(master=my_frame,
                text="Correct(1-YES, 0-NO)",
                width=15)
        entry3 = ui.Entry(master=my_frame,
               width=5)
        button = ui.Button(master=my_frame,
                           text="INSERT",
                           width=15,
                           command=partial(handler_cor, cur, conn, entry, entry2, entry3)
                           )
        my_frame.grid(row=0, column=0)
        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        label2.grid(row=1, column=0)
        entry2.grid(row=1, column=1)
        label3.grid(row=2, column=0)
        entry3.grid(row=2, column=1)
        button.grid(row=3)
        window.mainloop()
    elif name == "answers":
        entry = ui.Entry(master=my_frame,
               width=50)
        label = ui.Label(master=my_frame,
                text="answer text",
                width=10)
        button = ui.Button(master=my_frame,
                           text="INSERT",
                           width=15,
                           command=partial(handler_ans, cur, conn, entry)
                           )
        my_frame.grid(row=0, column=0)
        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        button.grid(row=1)
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
