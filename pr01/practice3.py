from pydantic import Field, BaseModel
from typing_extensions import Optional


# class ClassName(Parent Class Name):
#     field_name: type = Field(..., min_length, max_length, etc)

class User(BaseModel):
    id: int
    name: str
    age: int
    email: str

class Product(BaseModel):
    name: str = Field(..., min_length=4, max_length=10)
    # gt: price > 10.0 조건을 만족해야 함
    # le: price <= 100 조건을 만족해야 함
    price: float = Field(..., gt = 10.0, le = 100)
    stock: Optional[int] = 10

# User 클래스를 상속받음
class Admin(User):
    role: str = 'admin'

if __name__ == '__main__':
    # Class 생성할 때 int 형이라고 명시하면
    # 생성시 str 형을 넣어도 int 형으로 저장됨
    user1 = User(id=1, name="Gaeun", age=18, email="24")
    user2 = User(id="2", name="Gaeun", age="18", email="24")
    print(user1)
    print(user2)
    print(type(user1.id))
    print(type(user2.id))

    # stock: Optional[int] = 10 으로 하면
    # 생성시 stock 값을 안넣으면 10으로, 넣으면 그 값으로 설정
    p1 = Product(name="Sample1", price=13.0)
    p2 = Product(name="Sample2", price=10.2, stock=20)
    # print(p1)
    print(p2)

    # role 값이 자동으로 admin
    user3 = Admin(id=1, name="Gaeun", age=18, email="24")
    print(user3)