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
    price: float = Field(..., gt = 10.0, le = 100)
    stock: Optional[int] = 10

if __name__ == '__main__':
    user1 = User(id=1, name="Gaeun", age=18, email="24")
    user2 = User(id=2, name="Gaeun", age=18, email="24")
    print(user1)
    print(user2)

    # stock: Optional[int] = 10 으로 하면
    # 생성시 stock 값을 안넣으면 10으로, 넣으면 그 값으로 설정
    p1 = Product(name="Toy1", price=10.0)
    p2 = Product(name="Toy2", price=10.2, stock=20)
    print(p1)
    print(p2)