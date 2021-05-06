import tkinter as ui

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def insertTheData():
    print("Query should be here!")

class mainWindow:
    window = ui.Tk()
    window.columnconfigure(5, weight=1, minsize=25, pad=10) # should be fixed
    window.rowconfigure([0, 5], weight=1, minsize=10, pad=10) # should be fixed
    insertButton = ui.Button(text = "Insert", command=insertTheData)
    insertButton.grid(row=1, column=4)
    window.mainloop()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    adminWindow = mainWindow()
    print_hi('PyCharm')
