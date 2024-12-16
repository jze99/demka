import flet as ft
import flet.core.types as core
import datetime
import requests
colors=[
    "#ff5f1f",
    "#103173",
    "#f2f2f2",
    "#0d0d0d",
    "#114DC3"
]        

class loger(ft.AlertDialog):
    def __init__(self,value:str=""):
        super().__init__(
            content=Text(value=value)
        )


class Row_customer(ft.AlertDialog):
    def __init__(self,page, name_customer:str="", contact_info:str="", addres_customer:str=""):
        self.page = page
        self.name_customer=TextField(lable="имя покупателя",value=name_customer)
        self.contact_info_customer=TextField(lable="контактная информация покупателя",value=contact_info)
        self.address_customer=TextField(lable="адрес покупателя",value=addres_customer)
        super().__init__(
            content=ft.Container(
                width=500,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,
                    controls=[
                        ft.Row(controls=[self.name_customer]),
                        ft.Row(controls=[self.contact_info_customer]),
                        ft.Row(controls=[self.address_customer]),
                        ft.Row(controls=[Button_select_row1(text="Добавить")],alignment=ft.MainAxisAlignment.END)
                    ]
                )
            )
        )
    
    def add_row(self):
        pass

class TextField(ft.TextField):
    def __init__(self,lable:str="", value:str=""):
        super().__init__(
            value=value,
            label=lable,
            border_color=colors[1],
            text_size=24,
            selection_color=colors[4],
            focused_border_color=colors[4]
        )

class Text(ft.Text):
    def __init__(self,value:str="",size:int=24):
        super().__init__(
            value=value,
            color=colors[2],
            size=size
        )

class Button(ft.TextButton):
    def __init__(self, text:str="", on_clic:core.OptionalControlEventCallable=None):
        super().__init__(
            text=text,
            on_click=on_clic,
            width=100,
            height=55,
            style=ft.ButtonStyle(
                bgcolor=colors[1],
                color=colors[2],
                surface_tint_color=colors[4]
            )
        )

class Button_select_row1(ft.TextButton):
    def __init__(self, text:str="",selected_rows:int=1,disabled:bool=False, on_clic:core.OptionalControlEventCallable=None):
        self.selected_rows = selected_rows
        super().__init__(
            text=text,
            disabled=disabled,
            on_click=on_clic,
            width=100,
            height=55,
            style=ft.ButtonStyle(
                bgcolor=colors[1],
                color=colors[2],
                surface_tint_color=colors[4]
            )
        )
    def test(self):
        import user_data
        iter_row = len(user_data.select_row1)
        if self.selected_rows == 1:
            self.disabled = False
            self.bgcolor = colors[4]
        elif self.selected_rows == 2 and iter_row == 1:
            self.disabled = False
            self.bgcolor = colors[4]
        elif self.selected_rows == 3 and iter_row > 0:
            self.disabled = False
            self.bgcolor = colors[4]
        else:
            self.disabled = True
            self.bgcolor = colors[1]
        
    def activ(self):
        import user_data
        iter_row = len(user_data.select_row1)
        if self.selected_rows == 1:
            self.disabled = False
            self.bgcolor = colors[4]
        elif self.selected_rows == 2 and iter_row == 1:
            self.disabled = False
            self.bgcolor = colors[4]
        elif self.selected_rows == 3 and iter_row > 0:
            self.disabled = False
            self.bgcolor = colors[4]
        else:
            self.disabled = True
            self.bgcolor = colors[1]
        self.update()
        
class Button_select_row2(ft.TextButton):
    def __init__(self, text:str="",selected_rows:int=1,disabled:bool=False, on_clic:core.OptionalControlEventCallable=None):
        self.selected_rows = selected_rows
        super().__init__(
            text=text,
            disabled=disabled,
            on_click=on_clic,
            width=100,
            height=55,
            style=ft.ButtonStyle(
                bgcolor=colors[1],
                color=colors[2],
                surface_tint_color=colors[4]
            )
        )
    def test(self):
        import user_data
        iter_row = len(user_data.select_row2)
        if self.selected_rows == 1:
            self.disabled = False
            self.bgcolor = colors[4]
        elif self.selected_rows == 2 and iter_row == 1:
            self.disabled = False
            self.bgcolor = colors[4]
        elif self.selected_rows == 3 and iter_row > 0:
            self.disabled = False
            self.bgcolor = colors[4]
        else:
            self.disabled = True
            self.bgcolor = colors[1]
        
    def activ(self):
        import user_data
        iter_row = len(user_data.select_row2)
        if self.selected_rows == 1:
            self.disabled = False
            self.bgcolor = colors[4]
        elif self.selected_rows == 2 and iter_row == 1:
            self.disabled = False
            self.bgcolor = colors[4]
        elif self.selected_rows == 3 and iter_row > 0:
            self.disabled = False
            self.bgcolor = colors[4]
        else:
            self.disabled = True
            self.bgcolor = colors[1]
        self.update()
        
class CardProduct(ft.Container):
    def __init__(self,page:ft.Page,id:int,name_customer:str="",contact_info:str="",address:str=""):
        self.id=id
        self.select:bool=False
        self.page = page
        
        self.name_customer = name_customer
        self.contact_info=contact_info
        self.address=address
        
        self.controls = ft.Container(
            bgcolor=colors[1],
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Row(
                        expand=True,
                        controls=[
                            Text(value=name_customer),Text(value=contact_info)
                        ]
                    ),
                    ft.Row(
                        expand=True,
                        controls=[
                            Text(value=address)
                        ]
                    )
                ]
            )
        )
        super().__init__(
            expand=True,
            on_click=self.on_clic,
            content=self.controls
        )
        
    def update_button(self):
        import user_data
        for b in user_data.button_chec1:
            b.activ()
        
    def on_clic(self,e):
        import user_data
        if self.select==False:
            user_data.select_row1.append(self)
            self.controls.bgcolor=colors[4]
        if self.select==True:
            user_data.select_row1.remove(self)
            self.controls.bgcolor=colors[1]
        self.update_button()
        self.update()
        self.select= not self.select
        return

class Row_Orders(ft.Container):
    def __init__(self,page:ft.Page,id:int,order_data:str="",customer:str="",total_amount:str="",):
        self.page = page
        
        self.id = id
        self.order_data=order_data
        self.customer = customer
        self.total_amount=total_amount
        
        self.select:bool=False
        
        self.controls = ft.Container(
            bgcolor=colors[1],
            expand=True,
            on_click=self.on_clic,
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Row(
                        expand=True,
                        controls=[
                            Text(value=self.order_data),
                            Text(value=self.customer),
                        ]
                    ),
                    ft.Row(
                        expand=True,
                        controls=[
                            Text(value=self.total_amount)
                        ]
                    )
                ]
            )
        )
        
        super().__init__(
            expand=True,
            on_click=self.on_clic,
            content=self.controls
        )
    def update_button(self):
        import user_data
        for b in user_data.button_chec2:
            b.activ()
        
    def on_clic(self,e):
        import user_data
        if self.select==False:
            user_data.select_row2.append(self)
            self.controls.bgcolor=colors[4]
        if self.select==True:
            user_data.select_row2.remove(self)
            self.controls.bgcolor=colors[1]
        self.update_button()
        self.update()
        self.select= not self.select
        return

class TextFieldData(ft.TextField):
    def __init__(self,value,lable, page:ft.Page):
        self.page=page
        
        super().__init__(
            value=value,
            label=lable,
            read_only=True,
            border_color=colors[1],
            text_size=24,
            selection_color=colors[4],
            on_click=self.on_clic,
        )
        
    def handle_change(self,e):
       self.value = e.control.value.strftime('%Y-%m-%d')
       self.update()
    
    def on_clic(self,e):
        self.page.open(ft.DatePicker(
            first_date=datetime.datetime(year=2022, month=10, day=1),
            last_date=datetime.datetime(year=2026, month=10, day=1),
            on_change=self.handle_change
        ))  