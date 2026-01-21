from werkzeug.security import generate_password_hash, check_password_hash
from src.model.database import Database

class Usuario:
    def __init__(self, email, password, nombre="Usuario"):
        self.email = email
        self.nombre = nombre
        # AQUÍ CUMPLIMOS LA HU: Encriptamos la contraseña
        self.password_hash = generate_password_hash(password)
        self.db = Database()

    def guardar(self):
        """Guarda el usuario en la BD"""
        try:
            self.db.cursor.execute(
                "INSERT INTO usuarios (email, password_hash, nombre) VALUES (?, ?, ?)",
                (self.email, self.password_hash, self.nombre)
            )
            self.db.connection.commit()
            return True
        except Exception as e:
            # Si el usuario ya existe (email duplicado)
            return False

    def verificar_password(self, password):
        """Compara una contraseña plana con el hash guardado"""
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def login(email, password):
        """Busca usuario y valida contraseña (para la Interfaz)"""
        db = Database()
        cursor = db.cursor
        cursor.execute("SELECT password_hash, nombre FROM usuarios WHERE email = ?", (email,))
        row = cursor.fetchone()
        
        if row:
            hash_guardado = row[0]
            if check_password_hash(hash_guardado, password):
                return True # Login Correcto
        return False