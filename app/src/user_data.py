import flet as ft
import designer as des
import requests

select_row1=[]
select_row2 = []
page_user:ft.Page

def check_positive_integer(v):
    try:
        # Пробуем преобразовать строку в целое число
        number = int(v)
        print(f"{number}")
        # Проверяем, что число больше 0
        if number <= 0:
            page_user.open(des.loger(value="Число должно быть больше 0."))
        else:
            return number  # Возвращаем преобразованное число
    except ValueError:
        page_user.open(des.loger(value="Должно быть число "))

def open_delite_customer(e):
    from pages.delite_row import Delete
    data=[]
    for row in select_row1:
        data.append(
            {
                "id":row.id,
                "name":row.name_customer,
                "contact_info":row.contact_info,
                "address":row.address
            }
        )
    Delete.data = data
    page_user.go("/delete")
    
    
def open_add_customer(e):
    from pages.custumer_row import Customer_row
    Customer_row.id = 0
    Customer_row.name = ""
    Customer_row.contact = ""
    Customer_row.address=""
    page_user.go("/add_row")
    
def open_update_customer(e):
    from pages.custumer_row import Customer_row
    
    Customer_row.id = select_row1[0].id
    Customer_row.name = select_row1[0].name_customer
    Customer_row.contact = select_row1[0].contact_info
    Customer_row.address = select_row1[0].address
    page_user.go("/update_row")
    
button_chec1=[
    des.Button_select_row1(text="добавить",selected_rows=1,on_clic=open_add_customer),
    des.Button_select_row1(text="изменить", selected_rows=2,disabled=True,on_clic=open_update_customer),
    des.Button_select_row1(text="удалить",selected_rows=3,disabled=True,on_clic=open_delite_customer)
]

def open_add_order(e):
    from pages.order_row import Order_row
    Order_row.id = 0
    Order_row.order_data = ""
    Order_row.customer = ""
    Order_row.total_amount=""
    page_user.go("/add_row2")
    
def open_update_order(e):
    from pages.order_row import Order_row

    Order_row.id = select_row2[0].id
    Order_row.order_data = select_row2[0].order_data
    Order_row.customer = select_row2[0].customer
    Order_row.total_amount = select_row2[0].total_amount
    page_user.go("/update_row2")

def open_delite_orders(e):
    from pages.delite_row import Delete
    data=[]

    for row in select_row2:
        data.append(
            {
                "id":row.id,
                "order_data":str(row.order_data),
                "customer":row.customer,
                "total_amount":check_positive_integer(v=row.total_amount)
            }
        )
    print(f"{data=}")
    Delete.data = data
    page_user.go("/delete_order")

button_chec2=[
    des.Button_select_row2(text="добавить",selected_rows=1,on_clic=open_add_order),
    des.Button_select_row2(text="изменить", selected_rows=2,disabled=True,on_clic=open_update_order),
    des.Button_select_row2(text="удалить",selected_rows=3,disabled=True,on_clic=open_delite_orders)
]

