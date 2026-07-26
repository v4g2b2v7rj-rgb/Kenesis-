import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS environment_memory")

c.execute("""
CREATE TABLE environment_memory (
    object TEXT,
    action TEXT,
    time_state TEXT,
    Date TEXT,
    importance INTEGER
)
""")

conn.commit()
c.execute("""
CREATE TABLE IF NOT EXISTS user_memory (
    user_type TEXT,
    user_content TEXT,
    user_time TEXT,
    user_date TEXT
)
""")

conn.commit()
conn.close()
