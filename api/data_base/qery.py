from data_base.models import main_models as mm
from data_base.data_base import Base,engine,async_engine, sync_sassion
from sqlalchemy import delete, select

class QeryDataBase():
    @classmethod
    def select_table(cls, table):
        with sync_sassion() as session:
            return session.execute(select(table)).all()
    
    @classmethod
    def add_customer(cls, customer_data):
        with sync_sassion() as session: 
            print(customer_data)
            new_customer = mm.Customer(
                name=customer_data.name,
                contact_info=customer_data.contact_info,
                address=customer_data.address
            )
            session.add(new_customer)
            session.commit()
            return {"message": "Запись добавлена"}
    
    @classmethod
    def update_customer(cls, customer_id, updated_data):
        with sync_sassion() as session:
            customer = session.execute(select(mm.Customer).filter_by(id=customer_id)).scalar_one_or_none()
            
            if customer:
                # Update customer attributes
                customer.name = updated_data.name
                customer.contact_info = updated_data.contact_info
                customer.address = updated_data.address
                
                session.commit()
                return {"message": "Запись обновлена"}
            else:
                return {"message": "Пользователь не найден"}
    
    @classmethod
    def delete_customers(cls, customer_ids):
        with sync_sassion() as session:
            deleted_count = 0
            for customer_id in customer_ids:
                customer = session.execute(select(mm.Customer).filter_by(id=customer_id)).scalar_one_or_none()
                if customer:
                    session.execute(delete(mm.Customer).where(mm.Customer.id == customer_id))
                    deleted_count += 1
            session.commit()
            if deleted_count > 0:
                return {"message": f"Удалено записей: {deleted_count}"}
            else:
                return {"message": "Пользователи не найдены"}
    
    @classmethod
    def create_table(cls, data=None):
        with sync_sassion() as session:
            Base.metadata.drop_all(engine)
            Base.metadata.create_all(engine)
            for d in data:
                for dd in data[d]:
                    if d == "Customer":
                        temp_data=mm.Customer(
                            name=dd["name"],
                            contact_info=dd["contact_info"],
                            address=dd["address"]
                        )
                        session.add(temp_data)
                    if d == "Orders":
                        temp_data=mm.Orders(
                            order_data=dd["order_data"],
                            customer=dd["customer"],
                            total_amount=dd["total_amount"]
                        )
                        session.add(temp_data)
                    if d == "OrderDetalis":
                        temp_data=mm.OrderDetalis(
                            order_id=dd["order_id"],
                            product=dd["product"],
                            quantity=dd["quantity"],
                            price=dd["price"]
                        )
                        session.add(temp_data)
                    if d == "Products":
                        temp_data=mm.Products(
                            name=dd["name"],
                            type=dd["type"],
                            material=dd["material"],
                            price=dd["price"],
                            stocl_quantity=dd["stock_quantity"],
                        )
                        session.add(temp_data)
                    if d == "Suppliers":
                        temp_data = mm.Suppliers(
                            name=dd["name"],
                            contact_info=dd["contact_info"],
                            product_id=dd["product_id"],
                        )
                        session.add(temp_data)
            session.commit()

    @classmethod
    def add_order(cls, order):
        with sync_sassion() as session: 
            print(order)
            new_order = mm.Orders(
                order_data=order.order_data,
                customer= order.customer,
                total_amount = order.total_amount
            )
            session.add(new_order)
            session.commit()
            return {"message": "Запись добавлена"}
    
    @classmethod
    def update_order(cls, order_id, data_order):
        with sync_sassion() as session:
            order = session.execute(select(mm.Orders).filter_by(id=order_id)).scalar_one_or_none()
            
            if order:
                # Update customer attributes
                order.order_data = str(data_order.order_data)
                order.customer = data_order.customer
                order.total_amount = int(data_order.total_amount)
                
                session.commit()
                return {"message": "Запись обновлена"}
            else:
                return {"message": "Пользователь не найден"}
    
    @classmethod
    def delete_order(cls, order_ids):
        with sync_sassion() as session:
            deleted_count = 0
            for order_id in order_ids:
                customer = session.execute(select(mm.Orders).filter_by(id=order_id)).scalar_one_or_none()
                if customer:
                    session.execute(delete(mm.Orders).where(mm.Orders.id == order_id))
                    deleted_count += 1
            session.commit()
            if deleted_count > 0:
                return {"message": f"Удалено записей: {deleted_count}"}
            else:
                return {"message": "Пользователи не найдены"}
        

#async def login_user(auth_request):
#    async with async_session() as session:
#        stmt = select(users).where(
#            users.inn == auth_request.login,
#            users.password == auth_request.password
#        )
#        result = await session.execute(stmt)
#        user_exists = result.scalars().first() is not None
#    return user_exists
#
#async def add_user(name: str, age: int):
#    async with async_session() as session:
#        async with session.begin():
#            new_user = users(name=name, age=age)
#            session.add(new_user)
#        await session.commit()