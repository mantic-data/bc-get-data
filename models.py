"""Contain the ORM models"""

from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, backref, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Client(Base):
    __tablename__ = "client"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())
    description: Mapped[str] = mapped_column(String())
    addresses: Mapped[list["Address"]] = relationship(back_populates="client")
    factures: Mapped[list["Facture"]] = relationship(back_populates="client")

    def to_dict(self):
        return {"id": self.id, "name": self.name, "description": self.description}


class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    postal_code: Mapped[str] = mapped_column(String())
    first_line: Mapped[str] = mapped_column(String())
    city: Mapped[str] = mapped_column(String())
    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"))
    client: Mapped[Client] = relationship(back_populates="addresses")


class Service(Base):
    __tablename__ = "service"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())
    level: Mapped[int] = mapped_column(Integer())
    factures: Mapped[list["Facture"]] = relationship(back_populates="service")


class Facture(Base):
    __tablename__ = "facture"
    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column(Float())
    type: Mapped[str] = mapped_column(String())
    service_id: Mapped[int] = mapped_column(ForeignKey("service.id"))
    service: Mapped[Service] = relationship(back_populates="factures")
    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"))
    client: Mapped[Client] = relationship(back_populates="factures")
