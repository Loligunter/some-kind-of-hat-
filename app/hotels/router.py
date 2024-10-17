from fastapi import APIRouter,Request,Depends
from app.bookings.dao import BookingDAO
from app.bookings.shemas import SBooking
from app.exceptions import RoomCannotBeBooked
from app.users.dependencies import get_current_user
from app.users.models import Users
from datetime import date
from app.dao.base import BaseDAO


router =APIRouter(
    prefix="/hotels",
    tags=["Отели и комнаты"]
)

@router.get("/hotels")
async def get_booking(location: str, date_from: date,date_to: date) -> list:
    return await BaseDAO.find_by_location()
