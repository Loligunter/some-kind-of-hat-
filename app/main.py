from fastapi import FastAPI,Query,Depends
from datetime import date
from typing import Optional
from pydantic import BaseModel
import uvicorn

from app.bookings.router import router as router_bookings
from app.users.router import router_auth, router_users
from app.hotels.router import router as router_hotels

app = FastAPI()

app.include_router(router_users)
app.include_router(router_auth)
app.include_router(router_bookings)
app.include_router(router_hotels)


class SHotel(BaseModel):
    address: str
    name: str
    stars: int

class HotelSearchArgs:
    def __init__(self,
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool]=None,
        stars: Optional[int] = Query(None,ge=1,le=5)
):
        self.location=location
        self.date_from=date_from
        self.date_to=date_to
        self.has_spa=has_spa
        self.stars=stars

@app.get("/hotels")
def get_hotel(search_args: HotelSearchArgs=Depends()
    )-> list[SHotel]:
    hotel=[
        {
            'address': 'Красноврмейская',
            'name': 'Hotel',
            'stars': 5,
        }
    ] 
    return hotel

class SBookingPOST(BaseModel):
    room_id: int
    date_from: date
    date_to: date



#Не читай мой код, мне за него стыдно

@app.post("/booking")
async def add_booking(booking: SBookingPOST):
    pass