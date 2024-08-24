from fastapi import APIRouter


router = APIRouter(prefix="/user")

@router.get("/get_info")
async def get_user(user_id: int):
    return {"user_id": user_id}