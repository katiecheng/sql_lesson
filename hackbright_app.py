import sqlite3

DB = None
CONN = None

# UNFINISHED:
# def create_table(table_name, *args):
#     fieldnames = tuple(args)
#     query = """CREATE TABLE table_name (?)"""
#     DB.execute(query, (,))

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])

def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values(?,?,?)"""
    DB.execute(query, (first_name, last_name, github)) #create new row
    CONN.commit() # commit to memory
    print "Successfully added student: %s %s" % (first_name, last_name)

def make_new_project(title, description, max_grade):
    query = """INSERT into Projects (title, description, max_grade) values(?,?,?)"""
    DB.execute(query, (title, description, max_grade))
    CONN.commit()
    print "Successfully added project: %s %s" % (title, description)

def make_new_grade(github, title, grade):
    query = """INSERT into Grades values (?,?,?)"""
    DB.execute(query, (github, title, grade))
    CONN.commit()
    print "Successfully added grade to %s" % github

def query_project_by_title(title): ###START HERE TOMORROW!!###
    query = """SELECT title, description FROM Projects WHERE title=?"""
    DB.execute(query, (title,))
    row = DB.fetchone()
    print """\
Title: %s
Description: %s""" % (row[0], row[1])

def query_grade_by_project(title):
    query = """SELECT"""

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor() # mechanism to interact with the database, to execute queries (similar to a file handle)

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split(',')
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "new_project":
            make_new_project(*args)
        elif command == "new_grade":
            make_new_grade(*args)
        elif command == "query_project_by_title":
            query_project_by_title(*args)
        # elif command == "new_table":
        #     create_table(*args)

    CONN.close()

if __name__ == "__main__":
    main()
