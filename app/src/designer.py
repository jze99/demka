import flet as ft

colors=[
    "#ff5f1f",
    "#103173",
    "#f2f2f2",
    "#0d0d0d"
]

class Text(ft.Text):
    def __init__(self,value:str="",size:int=24):
        super().__init__(
            value=value,
            color=colors[2],
            size=size
        )

class CardProduct(ft.Card):
    def __init__(self,name_customer:str="",contact_info:str="",address:str=""):
        super().__init__(
            content=ft.Container(
                color=colors[1],
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                Text(value=name_customer),Text(value=contact_info)
                            ]
                        ),
                        ft.Row(
                            controls=[
                                Text(value=address)
                            ]
                        )
                    ]
                )
            )
        )