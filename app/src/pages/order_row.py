import flet as ft
import designer as des
import flet.core.types as core

class Order_row(ft.View):
    id:int=0
    order_data:str=""
    customer:str=""
    total_amount:str=""
    def __init__(self,page:ft.Page, route,ok:core.OptionalControlEventCallable=None):
        self.order_data=des.TextFieldData(page=page,value=Order_row.order_data,lable="дата продажи")
        self.customer=des.TextField(value=Order_row.customer,lable="покупатель")
        self.total_amount=des.TextField(value=Order_row.total_amount,lable="сумма продажи")
        super().__init__(
            route=route,
            bgcolor=des.colors[3],
            controls=[
                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        self.order_data,
                        self.customer,
                        self.total_amount,
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