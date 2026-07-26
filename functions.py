import random
import sqlite3
import time
import random
def env_format_memory(rows):
    return "\n".join(
        [f"- {obj} → {act} | {state} | {date} | {imp}"
         for obj, act, state, date, imp in rows]
    )
def format_user_memory(rows):
    return "\n".join(
        [f"- [{mem_type}] {content} ({time_state}, {date})"
         for mem_type, content, time_state, date in rows]
    )
from datetime import datetime
import random

def gen_object_action():
    things = ["box", "pencil", "UNKNOWN OBJECT", "macbook"]
    actions = ["Moving", "Galloping", "Dancing", "Disappeared"]

    obj = random.choice(things)
    act = random.choice(actions)

    time_state = "present"

    Date = datetime.now().strftime("%d %B %Y %H:%M:%S")

    importance = random.randint(1, 10)

    return obj, act, time_state, Date, importance
def insert_env_data(object,action,time_state,Date,importance):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    
    
    c.execute(
    "INSERT INTO environment_memory VALUES (?, ?, ?, ?, ?)",
    (object,action,time_state,Date,importance)
)

    conn.commit()
    c.execute("SELECT * FROM environment_memory")
    output = c.fetchall()
    c.close()
    return env_format_memory(output)

def insert_user_data(user_type,user_content,user_time,user_date):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    
    
    c.execute(
    "INSERT INTO user_memory VALUES (?, ?, ?, ?)",
    (user_type,user_content,user_time,user_date))


    conn.commit()
    c.execute("SELECT * FROM user_memory")
    output = c.fetchall()
    c.close()
    return format_user_memory(output)
def get_all_env():
    conn = sqlite3.connect("test.db")
    c = conn.cursor()

    c.execute("SELECT * FROM environment_memory")
    output_env = c.fetchall()

    conn.close()

    return output_env
def search_env_memory(thing):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()

    c.execute("SELECT * FROM environment_memory" \
    " WHERE object = (?)",
    (thing, ))
    env_get = c.fetchall()
    retrieve_env = env_format_memory(env_get)
    conn.close()
    return retrieve_env
