import sqlite3

class Database:
    _instance = None

    def __new__(cls):
        # Patrón Singleton: Asegura que solo haya una conexión a la base de datos
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.inicializar()
        return cls._instance

    def inicializar(self):
        # Crea la conexión y las tablas si no existen
        self.connection = sqlite3.connect("tareas.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        # Tabla de Usuarios
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                email TEXT PRIMARY KEY,
                password_hash TEXT NOT NULL,
                nombre TEXT
            )
        ''')
        # Tabla de Tareas (la usaremos más adelante)
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

    def cerrar(self):
        self.connection.close()