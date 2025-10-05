from sqlalchemy.orm import mapped_column, relationship, Mapped
from sqlalchemy import String, Boolean, Date, Integer, DateTime, UniqueConstraint, ForeignKey
from datetime import datetime
from app.db.session import Base

class Weather(Base):
    __tablename__ = "weather"

    id: Mapped[int] = mapped_column(primary_key = True)
    city: Mapped[str] = mapped_column(String, nullable = False)
    temperature: Mapped[int] = mapped_column(Integer, nullable = False)
    description: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, default = datetime.now)