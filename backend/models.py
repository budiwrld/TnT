from uuid import uuid4
from dataclasses import dataclass
from datetime import datetime
from extensions import db

def get_uuid():
    return uuid4().hex

@dataclass
class Roolit:
    HARRASTAJA = 'harrastaja'
    VALMENTAJA = 'valmentaja'


class Harrastaja(db.Model):
    __tablename__ = 'harrastajat'
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    username = db.Column(db.String(45), unique=True)
    password = db.Column(db.Text, nullable=False)
    etunimi = db.Column(db.String(100), nullable=False)
    sukunimi = db.Column(db.String(100), nullable=False)
    ikä = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), unique=True)
    numero = db.Column(db.String(13), unique=True)
    paikkakunta = db.Column(db.String(40))
    kiinostunut = db.Column(db.String, default=[])
    rooli = db.Column(db.Text, nullable=True, default=Roolit.HARRASTAJA)

    def __init__(self, username, password, etunimi, sukunimi, email, numero, paikkakunta):
        self.username = username
        self.password = password
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.email = email
        self.numero = numero
        self.paikkakunta = paikkakunta

class Valmentaja(db.Model):
    __tablename__ = 'valmentajat'
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    username = db.Column(db.String(45), unique=True)
    password = db.Column(db.Text, nullable=False)
    etunimi = db.Column(db.String(100), nullable=False)
    sukunimi = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    numero = db.Column(db.String(13), unique=True)
    paikkakunta = db.Column(db.String(40), nullable=True)
    rooli = db.Column(db.String(10), nullable=True, default=Roolit.VALMENTAJA)

    mainokset = db.relationship('Mainos', backref='valmentaja', lazy=True)

    def __init__(self, username, password, etunimi, sukunimi, email, numero, paikkakunta):
        self.username = username
        self.password = password
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.email = email
        self.numero = numero
        self.paikkakunta = paikkakunta

class Mainos(db.Model):
    __tablename__ = 'mainokset'
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    valmentaja_id = db.Column(db.String(32), db.ForeignKey('valmentajat.id'), nullable=False)
    valmentaja = db.relationship('Valmentaja', backref='mainokset', uselist=False)
    laji = db.Column(db.String(50), nullable=False, default="")
    liitto = db.Column(db.String(45), nullable=False, unique=True)
    otsikko = db.Column(db.String(50), nullable=False)
    kuvaus = db.Column(db.Text, nullable=True)
    osoite = db.Column(db.Text, nullable=True)
    numero = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    luotu = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)