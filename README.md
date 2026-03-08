# Learn Elasticsearch

Local practice: create MySQL tables → migrate data to Elasticsearch.

## Project structure

- **mysql/createTable.py**  
  Uses PyMySQL to create the database `movies_db`, table `movies` (imdb_id, title, director, year, rating, actors, description, poster_url, created_at, updated_at), and inserts 5 sample movie rows.

- **es_migration/migrate_movies.py**  
  Reads the `movies` table from MySQL, converts each row to an ES document (datetime → ISO string), and bulk-indexes into the `movies` index via `elasticsearch.helpers.bulk`. Document `_id` is set to `imdb_id`; re-running overwrites existing docs (idempotent).

## Requirements

- Python 3, dependencies: `pymysql`, `elasticsearch`
- MySQL running locally (e.g. `brew services start mysql`), root with empty password
- Elasticsearch running locally (e.g. Docker: `docker run -d --name elasticsearch -p 9200:9200 -e "discovery.type=single-node" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:8.11.0`)

## Run order

1. Start MySQL, then run: `python mysql/createTable.py`
2. Start Elasticsearch (e.g. the Docker command above)
3. Run migration: `python es_migration/migrate_movies.py`
4. Verify: `curl "http://localhost:9200/movies/_search?pretty"`

## Notes

- If your Python `elasticsearch` client is newer (default `compatible-with=9`), create the client with the header `Accept: application/vnd.elasticsearch+json; compatible-with=8` so it works with an ES 8 server.
