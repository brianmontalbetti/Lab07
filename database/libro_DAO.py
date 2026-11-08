from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_tutti_generi(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT DISTINCT genere FROM libro"
        cursor.execute(query)

        risultato = []
        for row in cursor:
            risultato.append(row["genere"])
        cursor.close()
        cnx.close()
        return risultato

    def get_libri_filtrati(self, id_biblioteca, genere):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = ("""SELECT *
                 FROM Libro
                 WHERE id_biblioteca = COALESCE (%s, id_biblioteca)
                 AND genere = COALESCE (%s, genere)""")
        cursor.execute(query, (id_biblioteca, genere))

        risultato = []
        for row in cursor:
            l = Libro(
                id=row["id"],
                titolo=row["titolo"],
                autore=row["autore"],
                genere=row["genere"],
                anno_pubblicazione=row["anno_pubblicazione"],
                id_biblioteca=row["id_biblioteca"]
            )
            risultato.append(l)

        cursor.close()
        cnx.close()
        return risultato