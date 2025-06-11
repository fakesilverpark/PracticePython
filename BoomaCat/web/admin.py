from fastapi import APIRouter

router = APIRouter(prefix="/admin")

@router.get("")
def f():
    return "admin"