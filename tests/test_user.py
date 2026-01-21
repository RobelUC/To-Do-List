import pytest
from src.model.user import Usuario

def test_usuario_guarda_password_seguro():
    """
    HU: Verificar que al crear un usuario, la contraseña no se guarde en texto plano.
    """
    email = "test@ejemplo.com"
    password_secreto = "123456"

    nuevo_usuario = Usuario(email, password_secreto)

    # Verificaciones
    assert nuevo_usuario.email == "test@ejemplo.com"
    assert nuevo_usuario.password_hash != password_secreto
    assert nuevo_usuario.verificar_password("123456") is True