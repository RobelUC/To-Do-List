import pytest
from src.model.user import Usuario

def test_usuario_guarda_password_seguro():
    """
    HU: Verificar que al crear un usuario completo, la contraseña se encripte.
    """
    email = "test_unitario@ejemplo.com"
    password_secreto = "123456"
    
    # ACTUALIZADO: Ahora pasamos los 6 datos que pide tu código nuevo
    nuevo_usuario = Usuario(
        email, 
        password_secreto, 
        "NombreTest", 
        "ApellidoTest", 
        "01/01/2000", 
        "Masculino"
    )

    # Verificaciones
    assert nuevo_usuario.email == email
    assert nuevo_usuario.password_hash != password_secreto
    assert nuevo_usuario.verificar_password(password_secreto) is True