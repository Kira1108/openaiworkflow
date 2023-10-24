from sqlalchemy import TEXT, Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import func
from database import Base
from datetime import datetime


class Text(Base):
    
    __tablename__ = "text"
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(TEXT, nullable = False)
    parse_result: Mapped[str] = mapped_column(TEXT, nullable=True)
    is_parsed: Mapped[bool] = mapped_column(Boolean,default = False)
    key:Mapped[str] = mapped_column(TEXT, nullable = True)
    create_time: Mapped[datetime] = mapped_column(insert_default =func.now())
    update_time: Mapped[datetime] = mapped_column(nullable = True, onupdate =func.now)
    
    def __repr__(self) -> str:
        return f"<Text(id={self.id}, text={self.text})>"
    
