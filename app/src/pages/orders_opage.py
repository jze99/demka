import flet as ft
import designer as des
import user_data

class Orders(ft.View):
    def __init__(self,route:str,page:ft.Page):
        self.page = page
        super().__init__(
            route=route,
            scroll=True,
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
                                    expand=True,
                                    alignment=ft.alignment.center,
                                    content=des.Text(value="Продажи")
                                ),
                                des.Button(text="Клиенты",on_clic=self.go_to_custumers),
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
                                    controls=user_data.button_chec2
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        
    def go_to_custumers(self,e):
        self.page.go('/')
        
    def load_table(self):
        import requests
        user_data.select_row2.clear()
        self.page.update()
        for b in user_data.button_chec2:
            b.test()
        user_data.page_user = self.page
        url="http://api:8000/api-demka/select1"
        try:
            response = requests.post(url) 
            response.raise_for_status() 
            data = response.json() 
            temp_data=[]
            for d in data:
                print(f"{d=}")
                temp_data.append(des.Row_Orders(
                    page=self.page,
                    id=d['id'],
                    order_data=d['order_data'],
                    customer=d['customer'],
                    total_amount=d['total_amount']
                ))
            return temp_data
        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка: {e}")
            return []