from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def get_generi(self) -> list[str] | None:
        cnx = DBConnect.get_connection()
        if cnx is None:
            return None
        cursor = cnx.cursor()
        try:
            cursor.execute('SELECT DISTINCT genere FROM libro ORDER BY genere')
            righe = cursor.fetchall()
            return [riga[0] for riga in righe]
        finally:
            cursor.close()
            cnx.close()

    def get_libri_filtrati(self, biblioteca: str | None, genere: str | None) -> list[Libro] | None:
        cnx = DBConnect.get_connection()
        if cnx is None:
            return None
        cursor = cnx.cursor(dictionary=True)
        try:
            query = ''' SELECT l.*
                        FROM libro l, biblioteca b
                        WHERE l.id_biblioteca = b.id
                        AND b.nome = COALESCE(%s, b.nome)
                        AND l.genere = COALESCE(%s, l.genere)
                        ORDER BY l.id'''
            cursor.execute(query, (biblioteca, genere))
            righe = cursor.fetchall()
            return [Libro(**riga) for riga in righe]
        finally:
            cursor.close()
            cnx.close()
