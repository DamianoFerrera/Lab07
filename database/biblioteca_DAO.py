from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    def get_biblioteche(self) -> list[Biblioteca] | None:
        cnx = DBConnect.get_connection()
        if cnx is None:
            return None
        cursor = cnx.cursor(dictionary=True)
        try:
            cursor.execute('SELECT * FROM biblioteca ORDER BY nome')
            righe = cursor.fetchall()
            return [Biblioteca(**riga) for riga in righe]
        finally:
            cursor.close()
            cnx.close()
