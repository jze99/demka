import flet as ft
import designer as des
import flet.core.types as core

class Customer_row(ft.View):
    id:int=0
    name:str=""
    contact:str=""
    address:str=""
    def __init__(self,page:ft.Page, route,ok:core.OptionalControlEventCallable=None):
        self.name=des.TextField(value=Customer_row.name,lable="имя покупателя")
        self.contact=des.TextField(value=Customer_row.contact,lable="контактная информация покупателя")
        self.address=des.TextField(value=Customer_row.address,lable="адрес покупателя")
        super().__init__(
            route=route,
            bgcolor=des.colors[3],
            controls=[
                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        self.name,
                        self.contact,
                        self.address,
                        ft.Row(
                            controls=[
                                des.Button(text="назад",on_clic=self.go_to_exit),
                                ft.Container(height=1,width=90),
                                des.Button(text="ок",on_clic=ok)
                            ]
                        )
                    ]
                )
            ]
        )
    def go_to_exit(self,e):
        self.page.go("/")