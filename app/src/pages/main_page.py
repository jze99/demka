import flet as ft
import designer as des
import requests
import user_data

class Main_page(ft.View):
    def __init__(self, page):
        self.page=page
        page.update()
        super().__init__(
            route="/",
            bgcolor=des.colors[3],
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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
                                    expand=True,
                                    alignment=ft.alignment.center,
                                    content=des.Text(value="Клиенты")
                                ),
                                des.Button(text="Продажи", on_clic=self.go_to_orders),
                                ft.Container(
                                    image=ft.DecorationImage(src="logo.png"),
                                    expand=True,
                                    alignment=ft.alignment.center_right,
                                    height=145,
                                )
                            ]
                        ),
                        ft.Row(
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Column(
                                    expand=True,
                                    alignment=ft.MainAxisAlignment.START,
                                    horizontal_alignment=ft.CrossAxisAlignment.END,
                                    scroll=ft.ScrollMode.AUTO,
                                    controls=self.load_table()
                                ),
                                ft.Column(
                                    alignment=ft.MainAxisAlignment.START,
                                    horizontal_alignment=ft.CrossAxisAlignment.END,
                                    controls=user_data.button_chec1
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    def go_to_orders(self,e):
        self.page.go('/orders_table')
    
    def load_table(self):
        user_data.select_row1.clear()
        self.page.update()
        for b in user_data.button_chec1:
            b.test()
        user_data.page_user = self.page
        url="http://api:8000/api-demka/select"
        try:
            response = requests.post(url) 
            response.raise_for_status() 
            data = response.json() 
            temp_data=[]
            for d in data:
                print(f"{d=}")
                temp_data.append(des.CardProduct(
                    page=self.page,
                    id=d['id'],
                    name_customer=d['name'],
                    contact_info=d['contact_info'],
                    address=d['address']
                ))
            return temp_data
        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка: {e}")
            return []