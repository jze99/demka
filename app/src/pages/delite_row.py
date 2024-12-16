import flet as ft
import designer as des
import requests
import flet.core.types as core


class Delete(ft.View):
    data =[]
    def __init__(self,route:str,page:ft.Page,on_clic:core.OptionalControlEventCallable=None):
        self.page = page
        super().__init__(
            route=route,
            controls={ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    des.Text(value="Удалить?")
                                ]
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    des.Button(text="Нет", on_clic=self.go_to_exit),
                                    ft.Container(height=1,width=70),
                                    des.Button(text="Да",on_clic=on_clic)
                                ]
                            )
                        ]
                    )
                )
            }
        )
    def go_to_exit(self,e):
        self.page.go("/")
    