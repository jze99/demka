from data_base.models import main_models as mm
from data_base.data_base import Base,sync_engine,async_engine, sync_sassion
from sqlalchemy import select

class QeryDataBase():
    @classmethod
    def select_table(cls, table):
        with sync_sassion() as session:
            return session.execute(select(table)).all()
    
    @classmethod
    def create_table(cls, data=None):
        with sync_sassion() as session:
            Base.metadata.drop_all(sync_engine)
            Base.metadata.create_all(sync_engine)
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