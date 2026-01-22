import sqlite3

class Usuario:
    def __init__(self, email, password, nombre, apellido, fecha_nacimiento, genero):
        self.email = email
        self.password = password
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero

    def guardar(self):
        conexion = sqlite3.connect("todo_app.db")
        cursor = conexion.cursor()
        
        # Crear tabla si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                email TEXT PRIMARY KEY,
                password TEXT,
                nombre TEXT,
                apellido TEXT,
                fecha_nacimiento TEXT,
                genero TEXT
            )
        """)
        
        try:
            cursor.execute("INSERT INTO usuarios VALUES (?, ?, ?, ?, ?, ?)", 
                           (self.email, self.password, self.nombre, self.apellido, self.fecha_nacimiento, self.genero))
            conexion.commit()
            return True
        except sqlite3.IntegrityError:
            return False # El correo ya existe
        finally:
            conexion.close()

    @staticmethod
    def login(email, password):
        conexion = sqlite3.connect("todo_app.db")
        cursor = conexion.cursor()
        
        # Asegurarnos de que la tabla exista para evitar errores
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                email TEXT PRIMARY KEY,
                password TEXT,
                nombre TEXT,
                apellido TEXT,
                fecha_nacimiento TEXT,
                genero TEXT
            )
        """)

        # --- EL CAMBIO ESTÁ AQUÍ ---
        # Seleccionamos todos los datos para crear el objeto Usuario
        cursor.execute("SELECT * FROM usuarios WHERE email = ? AND password = ?", (email, password))
        row = cursor.fetchone()
        conexion.close()

        if row:
            # row tiene: (email, password, nombre, apellido, nacimiento, genero)
            # Devolvemos un OBJETO Usuario con esos datos
            return Usuario(row[0], row[1], row[2], row[3], row[4], row[5])
        else:
            return None