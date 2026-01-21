import flet as ft
from src.model.user import Usuario

def main(page: ft.Page):
    page.title = "To-Do List TDD"
    page.window_width = 450  
    page.window_height = 750 
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER       
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def mostrar_registro(e=None):
        page.clean()
        
        titulo = ft.Text("Crear Cuenta", size=24, weight="bold", color="blue")
        
        
        nombre = ft.TextField(label="Nombres", width=350, border_radius=10)
        apellido = ft.TextField(label="Apellidos", width=350, border_radius=10)
        nacimiento = ft.TextField(label="Fecha de Nacimiento (DD/MM/AAAA)", width=350, border_radius=10)
        
        
        lbl_genero = ft.Text("Género:")
        
        genero = ft.RadioGroup(content=ft.Row(
            [
                ft.Radio(value="Masculino", label="Varón"),
                ft.Radio(value="Femenino", label="Mujer")
            ],
            alignment=ft.MainAxisAlignment.CENTER  
        ))

        email = ft.TextField(label="Correo Electrónico", width=350, border_radius=10)
        password = ft.TextField(label="Contraseña", password=True, width=350, border_radius=10)
        
        lbl_error = ft.Text("", color="red")

        def accion_registrar(e):
          
            if not email.value or not password.value or not nombre.value or not apellido.value or not genero.value:
                lbl_error.value = "¡Faltan datos obligatorios!"
                page.update()
                return

            nuevo_usuario = Usuario(
                email.value, 
                password.value, 
                nombre.value,
                apellido.value,
                nacimiento.value,
                genero.value
            )
            
            if nuevo_usuario.guardar():
                page.snack_bar = ft.SnackBar(ft.Text("¡Cuenta creada con éxito!"))
                page.snack_bar.open = True
                mostrar_login()
            else:
                lbl_error.value = "Error: El correo ya existe."
                page.update()

        btn_crear = ft.ElevatedButton("REGISTRARME", width=350, on_click=accion_registrar)
        btn_volver = ft.TextButton("Volver al Login", on_click=mostrar_login)

        page.add(
            ft.Column(
                [titulo, nombre, apellido, nacimiento, lbl_genero, genero, email, password, btn_crear, lbl_error, btn_volver],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO 
            )
        )
        page.update()

    # ---------------------------------------------------------
    # PANTALLA DE LOGIN
    # ---------------------------------------------------------
    def mostrar_login(e=None):
        page.clean()
        titulo = ft.Text("Iniciar Sesión", size=24, weight="bold")
        email = ft.TextField(label="Correo", width=300, border_radius=10)
        password = ft.TextField(label="Contraseña", password=True, width=300, border_radius=10)
        lbl_error = ft.Text("", color="red")

        def accion_login(e):
            if Usuario.login(email.value, password.value):
                page.clean()
                # Mensaje de bienvenida
                page.add(ft.Text(f"¡Bienvenido {email.value}!", size=30, color="green"))
            else:
                lbl_error.value = "Datos incorrectos"
                page.update()

        btn_entrar = ft.ElevatedButton("INGRESAR", width=300, on_click=accion_login)
        btn_ir_registro = ft.TextButton("Crear cuenta nueva", on_click=mostrar_registro)

        page.add(
            ft.Column(
                [titulo, email, password, btn_entrar, lbl_error, btn_ir_registro],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        page.update()

    mostrar_login()

if __name__ == "__main__":
    ft.app(target=main)