from flask import jsonify, request
from mentorsys import app, db
from mentorsys.models import Mentor, Mentee
from mentorsys.schemas import *
import mentorsys.data_service
from pprint import pprint

# default home route
@app.route("/", methods=["GET"])
def home():
    return {"msg": "HEY"}


# Get all mentor data
@app.route("/mentors", methods=["GET"])
def get_mentors():
    mentors = Mentor.query.all()
    # print(mentors[0])
    return jsonify(Mentor.Schema(many=True).dump(mentors))


# Get all mentee data
@app.route("/mentees", methods=["GET"])
def get_mentees():
    mentees = Mentee.query.all()
    # print(mentors[0])
    return jsonify(Mentee.Schema(many=True).dump(mentees))


# Add a mentor
@app.route("/mentor", methods=["POST"])
def add_mentor():
    fname = request.json["fname"]
    lname = request.json["lname"]
    email = request.json["email"]
    telnum = request.json["telnum"]
    contract = request.json["contract"]
    current = request.json["current"]
    met_max = request.json["met_max"]

    new_mentor = Mentor(fname, lname, email, telnum, contract, current, met_max)

    db.session.add(new_mentor)
    db.session.commit()
    return jsonify(Mentor.Schema().dump(new_mentor))


# Add a mentee
@app.route("/mentee", methods=["POST"])
def add_mentee():
    fname = request.json["fname"]
    lname = request.json["lname"]
    email = request.json["email"]
    telnum = request.json["telnum"]
    contract = request.json["contract"]

    new_mentee = Mentee(fname, lname, email, telnum, contract)
    # pprint(new_mentee)
    db.session.add(new_mentee)
    db.session.commit()
    return jsonify(Mentor.Schema().dump(new_mentee))


# Assign mentor to mentee
@app.route("/assign/<mentee_id>&<mentor_id>", methods=["PUT"])
def assign_mentee(mentee_id, mentor_id):
    mentee = Mentee.query.get(mentee_id)
    mentee.mentor_id = mentor_id
    db.session.commit()
    return mentee_schema.jsonify(mentee)

