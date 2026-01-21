import flet as ft

def main(page: ft.Page):
    # Configuración de la ventana
    page.title = "To-Do List (Flet)"
    page.window_width = 400
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # --- Elementos ---
    titulo = ft.Text("Iniciar Sesión", size=30, weight="bold")
    
    txt_email = ft.TextField(label="Correo Electrónico", width=300, border_radius=10)
    txt_pass = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300, border_radius=10)
    
    lbl_resultado = ft.Text("", color="red")

    def login_click(e):
        if txt_email.value == "admin" and txt_pass.value == "123":
            lbl_resultado.value = "¡Bienvenido de nuevo!"
            lbl_resultado.color = "green"
        else:
            lbl_resultado.value = "Datos incorrectos"
            lbl_resultado.color = "red"
        page.update()

    # --- CORRECCIÓN AQUÍ: Usamos content=ft.Text(...) ---
    btn_login = ft.ElevatedButton(
        content=ft.Text("INGRESAR"),  # <--- ESTO ES LO QUE CAMBIÓ
        width=300, 
        height=50, 
        on_click=login_click,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
    )

    # --- Agregar a pantalla ---
    page.add(
        ft.Column(
            [titulo, txt_email, txt_pass, btn_login, lbl_resultado],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)