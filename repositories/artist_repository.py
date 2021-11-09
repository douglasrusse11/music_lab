from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    result = run_sql(sql, values)
    id = result[0]["id"]
    artist.id = id 


def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def select(id):
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(result["name"], id)
    return artist

def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for result in results:
        artist = Artist(result["name"], result["id"])
        artists.append(artist)
    return artists

def albums(artist):
    albums = []
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)
    for result in results:
        album = Album(result["title"], result["genre"], artist, result["id"])
        albums.append(album)
    return albums

def update(artist):
    sql = "UPDATE artists SET name = %(name)s WHERE id = %(id)s"
    values = {'name': artist.name, 'id': artist.id}
    run_sql(sql, values)

def delete(artist):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [artist.id]
    run_sql(sql, values)