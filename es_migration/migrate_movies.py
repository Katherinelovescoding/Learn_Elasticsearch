import elasticsearch
from elasticsearch.helpers import bulk
import pymysql
from datetime import datetime

def row_to_doc(row):
    doc =  dict(row)
    for key in ("created_at", "updated_at"):
        if doc.get(key) is not None:
            doc[key] = doc[key].strftime("%Y-%m-%dT%H:%M:%S")
    return doc

def generate_actions():
    conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = "",
    charset = 'utf8mb4',
    database = 'movies_db',
    cursorclass = pymysql.cursors.DictCursor
    )
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM movies")
        for row in cursor:
            doc = row_to_doc(row)
            yield {
                "_index":"movies",
                "_id": row["imdb_id"],
                "_source": doc
            }
    conn.close()


if __name__ == "__main__":
    es = elasticsearch.Elasticsearch(['http://localhost:9200'])
    success, failed = bulk(es, generate_actions(), raise_on_error=False)
    print(f"Successfully indexed {success} movies")
    if failed:
        print(f"Failed to index {failed} movies")
        for error in failed:
            print(f"Error: {error}")