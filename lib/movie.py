from . import CONN
from . import CURSOR

class Movie:
    def __init__(self, title, year, id=None):
        self.id = id
        self.title = title
        self.year = year

    def __repr__(self):
        return f'Movie(id={self.id}, title={self.title}, year={self.year})'






    # --- CLASS METHODS --- #
    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT,
            year NUMBER
            ) 
        """
        CURSOR.execute(sql)



    @classmethod
    def get_all(cls):
        sql="SELECT * FROM movies"
        movies_tuples = CURSOR.execute(sql).fetchall()
        return [ Movie(title=movie[1], year=movie[2], id=movie[0]) for movie in movies_tuples]



    # BONUS: this will destroy a row based on a given id
    @classmethod
    def destroy_by_id(cls, id):
        sql="DELETE FROM movies where id = ?"
        CURSOR.execute(sql, [id])
        CONN.commit()






    # --- SQL INSTANCE METHODS --- #
    def create(self):
        sql = "INSERT INTO movies (title, year) VALUES(?,?)"
        CURSOR.execute(sql, {self.title, self.year})
        CONN.commit()

        sql = "SELECT id = last_insert_rowid() FROM movie"
        id = CURSOR.execute(sql).fetchone()
        self.id = id



    def update(self):
        sql="""UPDATE movies
        SET title = ?, year =?
        WHERE idf = ?
        """
        CURSOR.execute(sql, [self.title, self.year, self.id])
        CONN.commit()



    # BONUS: this will either create or update depending on if this instance exists in the db
    def save(self):
        if self.id == None:
            self.create()
        else:
            self.update()



    def destroy(self):
        sql = """DELETE FROM movies
        WHERE id = ?
        """
        CURSOR.execute(sql, [self.id])
        CONN.commit()
