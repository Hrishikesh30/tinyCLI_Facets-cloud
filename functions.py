from database import DB_NAME
import sqlite3
import time

def ingest(file_path):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    start_time = time.perf_counter()
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                timestamp, user_id, event_type, payload = [x.strip() for x in line.split('|', 3)]
                cursor.execute("INSERT INTO events (timestamp, user_id, event_type, payload) VALUES (?, ?, ?, ?)",
                               (timestamp, int(user_id), event_type, payload))
    
    end_time = time.perf_counter()
    print(f"Ingestion completed in {end_time - start_time:.4f} seconds.")
    return conn

def query_events(user_id, event_type=None, time_from=None, time_to=None):
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    start_time = time.perf_counter()
    sql = "SELECT timestamp, user_id, event_type, payload FROM events WHERE user_id = ?"
    params = [user_id]

    if event_type:
        sql += " AND event_type = ?"
        params.append(event_type)

    if time_from:
        sql += " AND timestamp >= ?"
        params.append(time_from)

    if time_to:
        sql += " AND timestamp <= ?"
        params.append(time_to)

    sql += " ORDER BY timestamp ASC"
    
    cursor.execute(sql, tuple(params))
    count = 0
    end_time = time.perf_counter()

    count = 0
    while True:
        rows = cursor.fetchmany(1000)
        if not rows:
            break
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
            count += 1
    conn.close()

    print("total count return:",count)
    #print(f"Start time: {start_time} and End time: {end_time}")
    print(f"Elapsed time: {(end_time - start_time) * 1_000_000:.0f} microseconds")