#PancakeSafari
#Adam Abbas, Terry Guan, Irene Lam, Shannon Lau (PM)
#SoftDev pd7
#P01 -- ArRESTed Development

global db

import sqlite3  # enable control of an sqlite database
#opens a database
def open_db():
    global db
    f = "data/database.db"
    db = sqlite3.connect(f, check_same_thread=False)  # open if f exists, otherwise create
    return

# Closes the database
def close():
    global db
    db.commit()  # save changes
    db.close()  # close database
    return

# For testing and debugging purposes
def db_count():
    global db
    open_db()
    c = db.cursor()
    num = -2
    try:
        c.execute("SELECT count(*) FROM threads")
        num = c.fetchall()
    except:
        print("Unable to get count")
    close()
    return num[0][0] + 1

# Sets up initial database
def db_setup():
    global db
    open_db()
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS threads (
        id TEXT PRIMARY KEY,
        time DEFAULT CURRENT_TIMESTAMP NOT NULL,
        message_log TEXT NOT NULL,
        gif_url TEXT NOT NULL)''')
    close()
    return

# Creates a new row (thread) within the database
def create_thread(id, input_log, input_url):
    global db
    try:
        open_db()
        c = db.cursor()
        command = '''INSERT INTO threads
            VALUES (?, date('now'), ?, ?)'''
        # print command
        c.execute(command, (id, input_log, input_url,))      # input_log and input_url are from user/db
        close()
    except Exception as e:
        print e
        print "Error creating thread"
        return False
    return True

# Gets a specific thread given a index
def get_thread(index):
    global db
    try:
        open_db()
        c = db.cursor()
        c.execute("SELECT message_log FROM threads WHERE id=?", (index,))      # input_log and input_url are from user/db
        rows = c.fetchall()

        # for i in rows:
        #     print i

        close()
    except:
        print "Error getting thread"

    return rows[0][0]

# Appends a message to a specific thread given the ID and new message
def update_thread(index, new_message):
    global db
    try:
        curr_message = get_thread(index) # receives old thread
        #print "im here"
        # using , as delimiter
        mess = curr_message + "<br>" + new_message # new thread trimmed and appended accordingly
        print mess
        open_db()
        c = db.cursor()
        c.execute("UPDATE threads SET message_log = ? WHERE id = ?", (mess, index,))
        close()

    except:
        print "Error updating thread"
        return False
    return True

# Updates the image url in the database, given the ID of the thread and the url updates
def update_image(index, gif_url):
    global db
    try:
        open_db()
        c = db.cursor()
        c.execute("UPDATE threads SET gif_url = ? WHERE id = ?", (gif_url, index,))
        close()
        print "update image successful"
    except:
        print "Error updating image"
        return False
    return True

# Returns all threads within the database
def get_all_threads():
    global db
    try:
        open_db()
        c = db.cursor()
        c.execute("SELECT * FROM threads")
        rows = c.fetchall()
        close()
    except:
        print "Error getting all threads"

    return rows

# db_setup()

# Test cases
# create_thread(1, '"text":"Hi"',
#               "https://i.pinimg.com/736x/de/c5/d1/dec5d1d75fa4333d771e6fed6c97c958--dessin-ghibli-ghibli-watercolor.jpg")
# create_thread(2, '"text":"Welcome"',
#               "https://i.pinimg.com/736x/de/c5/d1/dec5d1d75fa4333d771e6fed6c97c958--dessin-ghibli-ghibli-watercolor.jpg")
# create_thread(3, '"text":"Totoro"',
#               "https://i.pinimg.com/736x/de/c5/d1/dec5d1d75fa4333d771e6fed6c97c958--dessin-ghibli-ghibli-watercolor.jpg")
# get_thread(1)
# update_thread(1,'"text":"New Updates"')
# get_thread(1)
# get_thread(3)
