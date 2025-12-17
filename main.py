from flask import Flask, request
from sqlalchemy.orm import Session
from sqlalchemy.sql import select
from sqlalchemy import func
from db import engine
from models import Client, Address, Service, Facture

app = Flask(__name__)


@app.route("/health")
def healthcheck():
    return "ok"


@app.route("/clients", methods=["POST"])
def find_clients():
    clients_info = request.get_json()
    query = select(Client)
    if "name" in clients_info:
        query = query.where(Client.name.like(f"%{clients_info['name']}%"))
    if "description" in clients_info:
        query = query.where(Client.description.like(f"%{clients_info['description']}%"))
    with Session(engine) as session:
        return [
            client.to_dict() for client in session.execute(query).scalars().all()
        ], 200


@app.route("/shodan_budget", methods=["GET"])
def shodan_budget():
    query = (
        select(func.sum(Facture.amount), Client.name)
        .join(Client, Client.id == Facture.client_id)
        .group_by(Client.name)
    )
    with Session(engine) as session:
        return [list(row) for row in session.execute(query).all()]
