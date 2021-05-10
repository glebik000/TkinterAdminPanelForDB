from sqlite3 import Error
import sqlite3

def create_connection(db_file): 
    """ Create a database connection"""
    conn = None 
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ Create a table """
    try:
        crs = conn.cursor()
        crs.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database_folder = r"E:\Project\TkinterAdminPanelForDB\sqldb.db"

    sql_create_projects_table = """ 
                                    CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY, 
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                        );
                                """
    sql_create_tasks_table =    """
                                    CREATE TABLE IF NOT EXISTS tasks (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        priority integer,
                                        status_id integer NOT NULL,
                                        project_id integer NOT NULL,
                                        begin_date text NOT NULL,
                                        end_date text NOT NULL,
                                        FOREIGN KEY (project_id) REFERENCES projects (id)
                                        );
                                """
    conn = create_connection(database_folder)
    if conn is not None:
        create_table(conn, sql_create_projects_table)
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! Can't make a connection")

if __name__ == '__main__':
    main()
    print("Data base created")
