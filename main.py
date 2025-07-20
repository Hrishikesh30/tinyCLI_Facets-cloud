import click
from functions import ingest, query_events
from database import init_db, setup_indexes

@click.group()
def cli():
    init_db()

@cli.command("record")
@click.argument('file_path')
def record(file_path):
    conn=ingest(file_path) #ingest text file to database
    cursor=conn.cursor()
    setup_indexes(cursor) #create index after ingesting data to the db
    conn.commit()
    conn.close()

@cli.command("query")
@click.argument('user_id', type=int)
@click.option('--type', 'event_type', default=None, help='Event type to filter.')
@click.option('--from', 'from_time', default=None, help='Start ISO8601 timestamp.')
@click.option('--to', 'to_time', default=None, help='End ISO8601 timestamp.')
def query(user_id, event_type, from_time, to_time):
    query_events(user_id, event_type, from_time, to_time) #query events from database

if __name__ == '__main__':
    cli()
