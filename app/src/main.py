import flet as ft
from views import ViewHandler


def main(page: ft.Page):

    def PageLoader(route):
        page.views.clear()
        page.views.append(ViewHandler(page=page)[page.route])
        page.update()
        print(page.route)
    page.on_route_change = PageLoader
    page.go("/")

ft.app(main,assets_dir="assets", view=ft.AppView.WEB_BROWSER,port=80)
