from werkzeug.security import generate_password_hash, check_password_hash
from src.model.database import Database

class Usuario:
    # Agregamos los nuevos argumentos al constructor
    def __init__(self, email, password, nombre, apellido, nacimiento, genero):
        self.email = email
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
        self.genero = genero
        self.password_hash = generate_password_hash(password)
        self.db = Database()

    def guardar(self):
        try:
            # Insertamos las 6 columnas
            self.db.cursor.execute(
                """INSERT INTO usuarios 
                   (email, password_hash, nombre, apellido, nacimiento, genero) 
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (self.email, self.password_hash, self.nombre, self.apellido, self.nacimiento, self.genero)
            )
            self.db.connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def verificar_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def login(email, password):
        # El login sigue igual, solo necesitamos email y pass para entrar
        db = Database()
        cursor = db.cursor
        cursor.execute("SELECT password_hash, nombre FROM usuarios WHERE email = ?", (email,))
        resultado = cursor.fetchone()
        
        if resultado:
            hash_guardado = resultado[0]
            if check_password_hash(hash_guardado, password):
                return True 
        return False