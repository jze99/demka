import flet as ft
import designer as des
import user_data as ud
from pages.main_page import Main_page
from pages.custumer_row import Customer_row
from pages.delite_row import Delete
from pages.orders_opage import Orders
from pages.order_row import Order_row
import requests

def ViewHandler(page:ft.Page):
    def add_row(e):
        Customer_row.id = 0
        Customer_row.name = ""
        Customer_row.contact = ""
        Customer_row.address=""
        data = {
            "id":0,
            "name":add_row_customer.name.value,
            "contact_info":add_row_customer.contact.value,
            "address":add_row_customer.address.value
        }
        url = "http://api:8000/api-demka/add"
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Данные успешно отправлены.")
            page.open(des.loger(value=("Ответ от сервера:", response.json())))
            page.go("/")
    
    def update_row(e):
        import user_data
        
        data = {
            "id":Customer_row.id,
            "name":update_row_customer.name.value,
            "contact_info":update_row_customer.contact.value,
            "address":update_row_customer.address.value
        }
        url = "http://api:8000/api-demka/update"
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Данные успешно отправлены.")
            page.open(des.loger(value=("Ответ от сервера:", response.json())))
            page.go("/")

    def delite_customer(e):
        import user_data
        
        url = "http://api:8000/api-demka/delete"
        response = requests.post(url, json=Delete.data)
        if response.status_code == 200:
            print("Данные успешно отправлены.")
            page.open(des.loger(value=("Ответ от сервера:", response.json())))
            user_data.select_row1.clear()
            user_data.page_user.go("/")
        Delete.data=[]
    
    ####orders
    
    def add_row_order(e):
        Order_row.id = 0
        Order_row.name = ""
        Order_row.contact = ""
        Order_row.address=""
        data = {
            "id":0,
            "order_data":str(add_order_row.order_data.value),
            "customer":add_order_row.customer.value,
            "total_amount":ud.check_positive_integer(v=add_order_row.total_amount.value)
        }
        url = "http://api:8000/api-demka/add1"
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Данные успешно отправлены.")
            page.open(des.loger(value=("Ответ от сервера:", response.json())))
            page.go("/orders_table")
    
    def update_row_order(e):
        import user_data
        data = {
            "id":Order_row.id,
            "order_data":str(update_order_row.order_data.value),
            "customer":update_order_row.customer.value,
            "total_amount":ud.check_positive_integer(v=update_order_row.total_amount.value)
        }
        url = "http://api:8000/api-demka/update1"
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Данные успешно отправлены.")
            page.open(des.loger(value=("Ответ от сервера:", response.json())))
            page.go("/orders_table")
    
    def delite_order(e):
        import user_data
        
        url = "http://api:8000/api-demka/delete1"
        response = requests.post(url, json=Delete.data)
        if response.status_code == 200:
            print("Данные успешно отправлены.")
            page.open(des.loger(value=("Ответ от сервера:", response.json())))
            user_data.select_row2.clear()
            user_data.page_user.go("/orders_table")
        Delete.data=[]
    
    add_row_customer = Customer_row(route="/add_row",ok=add_row, page=page)
    update_row_customer = Customer_row(route="/update_row",ok=update_row, page=page)
    delete = Delete(page=page,route="/delete",on_clic=delite_customer)
    orders_table = Orders(route="/orders_table",page=page)
    add_order_row = Order_row(page=page,route="/add_row2",ok=add_row_order)
    update_order_row = Order_row(page=page,route="/add_row2",ok=update_row_order)
    delete_order = Delete(page=page,route="/delete_order",on_clic=delite_order)
    return{
        "/":Main_page(page=page),
        "/add_row":add_row_customer,
        "/update_row":update_row_customer,
        "/delete":delete,
        "/orders_table":orders_table,
        "/add_row2":add_order_row,
        "/update_row2":update_order_row,
        "/delete_order":delete_order
    }