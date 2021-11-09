from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%(title)s, %(genre)s, %(artist_id)s) RETURNING *"
    values = {'title': album.title, 'genre': album.genre, 'artist_id': album.artist.id}
    result = run_sql(sql, values)
    id = result[0]["id"]
    album.id = id

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def select(id):
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = artist_repository.select(result["artist_id"])
        album = Album(result["title"], result["genre"], artist, id)
    return album

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for result in results:
        artist = artist_repository.select(result["artist_id"])
        album = Album(result["title"], result["genre"], artist, result["id"])
        albums.append(album)
    return albums

def update(album):
    sql = "UPDATE albums SET (title, genre, artist_id) = (%(title)s, %(genre)s, %(artist_id)s) WHERE id = %(id)s"
    values = {'title': album.title, 'genre': album.genre, 'artist_id': album.artist.id, 'id': album.id}
    run_sql(sql, values)

def delete(album):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [album.id]
    run_sql(sql, values)