import sqlite3

class Database:
    _instance = None

    def __new__(cls):
        # Patrón Singleton: Para usar siempre la misma conexión
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.inicializar()
        return cls._instance

    def inicializar(self):
        # Conecta a la BD (crea el archivo si no existe)
        self.connection = sqlite3.connect("tareas.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        # Tabla Usuarios
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                email TEXT PRIMARY KEY,
                password_hash TEXT NOT NULL,
                nombre TEXT
            )
        ''')
        # Tabla Tareas
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT,
                estado TEXT DEFAULT 'pendiente',
                usuario_email TEXT,
                FOREIGN KEY(usuario_email) REFERENCES usuarios(email)
            )
        ''')
        self.connection.commit()