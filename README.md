# Tiny Event Stream CLI

A tiny Python CLI to record and query an event stream using SQLite for fast, persistent storage.

## Features

- Ingests events from a text file 
- Stores events in a local SQLite database
- Query events by user, event type, and time window
- Fast queries with proper indexing
- Simple CLI interface using `click`

## Requirements

- Python 3.7+
- Python libraries and `click` (installable via pip)

## Setup

1. **Clone the repository**:

2. **Install dependencies:**
   ```sh
   pip install click
   ```

## Usage

### 1. Record events from a file

The input (.txt) file should have one event per line in the format:

```
<ISO-8601 timestamp> | <user-id> | <event-type> | <payload>
```

Example:

```
2023-08-14T12:34:56Z | 42 | login | {"ip":"10.0.0.1"}
2023-08-14T12:35:10Z | 42 | purchase | {"item":"A123","price":9.99}
2023-08-14T12:36:00Z | 7  | login  | {"ip":"192.168.1.5"}
```

To ingest events:

```sh
python main.py record <file_path>
```

### 2. Query events

Query all events for a user, optionally filtered by event type and time window:

```sh
python main.py query <user-id> [--type=<event-type>] [--from=<ISO8601>] [--to=<ISO8601>]
```

#### Examples

- All events for user 42:
  ```sh
  python main.py query 42
  ```
- All 'login' events for user 42:
  ```sh
  python main.py query 42 --type=login
  ```
- All events for user 42 from a specific time:
  ```sh
  python main.py query 42 --from=2023-08-14T12:00:00Z
  ```
- All events for user 42 in a time window:
  ```sh
  python main.py query 42 --from=2023-08-14T12:00:00Z --to=2023-08-14T13:00:00Z
  ```

## Performance

- Designed to handle 1M+ events efficiently (query in ≤ 1s on typical hardware)
- Uses SQLite indexes for fast lookups
- Optimized ingestion using batch inserts and deferred index creation to improve overall performance.
## Testing

- You can use the provided `f1.txt` or create your own event file for testing.
- Example:
  ```sh
  python main.py record f1.txt
  python main.py query 42
  python main.py query 17 --type=logout --from=2023-08-15T00:00:00Z --to=2023-08-15T12:00:00Z
  python main.py query 42 --type=login --from=2023-08-15T00:00:00Z --to=2023-08-15T12:00:00Z
  ```

## Notes

- The database is stored in `events.db` in the project directory.
- Re-running `record` will append new events to the database.
- Timestamps are stored in ISO-8601 format.


