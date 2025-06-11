from fastapi import APIRouter

router = APIRouter(prefix="/products")

@router.get("")
def f():
    return "products"