from fastapi import APIRouter
from ..controllers import users as userController
router = APIRouter()

@router.get("/users", tags=['users'])
async def get_users():
  user = await userController.getUsers()
  return user