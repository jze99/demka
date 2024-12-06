import flet as ft
from pages.main_page import Main_page

def ViewHandler(page:ft.Page):
    return{
        "/":Main_page(page=page)
    }