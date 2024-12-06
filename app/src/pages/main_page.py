import flet as ft
import designer as des

class Main_page(ft.View):
    def __init__(self, page):
        super().__init__(
            route="/",
            bgcolor=des.colors[3],
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Column(
                    controls=[
                        ft.Row( # Шапка
                            alignment=ft.MainAxisAlignment.CENTER,
                            expand=True,
                            controls=[
                                ft.Container(
                                    expand=True,
                                    content=des.Text(value="Промитей",size=45),
                                    alignment=ft.alignment.center_left
                                ),
                                ft.Container(
                                    image=ft.DecorationImage(src="logo.png"),
                                    expand=True,
                                    alignment=ft.alignment.center_right,
                                    height=145,
                                )
                            ]
                        ),
                        ft.Row(
                            controls=[
                                
                            ]
                        )
                    ]
                )
            ]
        )