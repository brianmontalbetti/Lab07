from mysql.connector.cursor import CursorBase

from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_tutte_biblioteche(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM biblioteca"
        cursor.execute(query)
        risultato = []
        for row in cursor:
            b = Biblioteca(row["id"], row["nome"], row["indirizzo"])
            risultato.append(b)

        cursor.close()
        cnx.close()
        return risultato