from typing import TYPE_CHECKING,Optional
from sqlalchemy import JSON, Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.bookings.models import Bookings
from app.database import Base
from app.hotels.rooms.models import Rooms



# Модель написана в соответствии с современным стилем Алхимии (версии 2.x)
class Hotels(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    location: Mapped[str]
    services: Mapped[list[str]] = mapped_column(JSON)
    rooms_quantity: Mapped[int]
    image_id: Mapped[int]
    
    rooms: Mapped[list["Rooms"]] = relationship(back_populates="hotel")

    def __str__(self):
        return f"Отель {self.name} {self.location[:30]}"


