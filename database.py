import sqlite3

DB_NAME = "events.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            timestamp TEXT,
            user_id INTEGER,
            event_type TEXT,
            payload TEXT
        )
    ''')
    setup_indexes(cursor)
    conn.commit()
    conn.close()

def setup_indexes(cursor):
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_user_id ON events (user_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_user_type ON events (user_id, event_type)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_user_time ON events (user_id, timestamp)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_user_type_time ON events (user_id, event_type, timestamp)")
