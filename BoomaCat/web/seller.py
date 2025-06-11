from fastapi import APIRouter

router = APIRouter(prefix="/seller")

@router.get("")
def f():
    return "seller"