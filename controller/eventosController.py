from database.conexion import get_connection
from models.eventos import Eventos


class Eventos:
    def __init__(self):
        self.conn = get_connection()


def agregar_evento(self, nombreEvento,fecha_inicio,hora_inicio,fecha_publicacion):
    cursor = self.conn.cursor()
    cursor.execute('''
        INSERT INTO eventos (nombreEvento,fecha_inicio,hora_inicio,fecha_publicacion) 
        VALUES (?,?,?,?)
    ''', nombreEvento,fecha_inicio,hora_inicio,fecha_publicacion)
    self.conn.commit()

