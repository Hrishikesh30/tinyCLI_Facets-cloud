import sqlite3
import time

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
    #setup_indexes(cursor) #creating index after ingestion will improve the overall ingestion time
    conn.commit()
    conn.close()

def setup_indexes(cursor):
    start_time =time.perf_counter()
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_user_id ON events (user_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_user_type ON events (user_id, event_type)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_user_time ON events (user_id, timestamp)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_user_type_time ON events (user_id, event_type, timestamp)")
    end_time = time.perf_counter()
    print(f"index creation completed in {end_time - start_time:.4f} seconds.")