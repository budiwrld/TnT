from flask import Blueprint, jsonify, request, redirect, url_for, session
from config import db
from models import Harrastaja, Valmentaja

auth = Blueprint('auth', __name__)

@auth.route('/sign-up/<user_type>', methods=['POST'])
def signup(user_type):
    if user_type == 'harrastaja':
        data = request.json

        harrastaja = Harrastaja(
            username=data['username'],
            password=data['password'],
            etunimi=data['etunimi'],
            sukunimi=data['sukunimi'],
            email=data['email'],
            numero=data['numero'],
            paikkakunta=data['paikkakunta']
        )
        try:
            db.session.add(harrastaja)
            db.session.commit()
            return jsonify(message="Harrastaja signup onnistunui"), 201
        except Exception as e:
            return jsonify(message=f"Rekistöröinti epäonnistui, yritä myöhemmin uudelleen, virhe: {e}"), 500


    elif user_type == 'valmentaja':
        pass

    elif user_type == 'staff':
        pass

    elif user_type == 'developer':
        pass
