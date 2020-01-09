from flask import jsonify, request
from mentorsys import app, db
from mentorsys.models import Mentor, Mentee, mentee_schema, mentees_schema, mentor_schema, mentors_schema
import mentorsys.data_service
from pprint import pprint

# default home route
@app.route("/", methods=["GET"])
def home():
    """ Home route """
    return {"msg": "HEY"}

# Retrievals
@app.route("/api/mentors", methods=["GET"])
def get_mentors():
    """ Get all mentor data """
    mentors = Mentor.query.all()
    print(mentors)
    result = mentors_schema.dump(mentors)
    # print(result)
    return jsonify(result)

@app.route("/api/mentees", methods=["GET"])
def get_mentees():
    """ Get all mentee data """
    mentees = Mentee.query.all()
    result = mentees_schema.dump(mentees)
    return jsonify(result)

@app.route("/api/mentors/<id>", methods=["GET"])
def view_mentor(id):
    """ return mentor with given ID """
    mentor = Mentor.query.get(id)
    return mentor_schema.jsonify(mentor)

@app.route("/api/mentees/<id>", methods=["GET"])
def view_mentee(id):
    """ return mentee with given id """
    mentee = Mentee.query.get(id)
    return mentee_schema.jsonify(mentee)

# additions
@app.route("/api/mentors", methods=["POST"])
def add_mentor():
    """ Add a mentor """
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
    return mentor_schema.jsonify(new_mentor)


@app.route("/api/mentees", methods=["POST"])
def add_mentee():
    """ Add a mentee """
    fname = request.json["fname"]
    lname = request.json["lname"]
    email = request.json["email"]
    telnum = request.json["telnum"]
    contract = request.json["contract"]

    new_mentee = Mentee(fname, lname, email, telnum, contract)
    # pprint(new_mentee)
    db.session.add(new_mentee)
    db.session.commit()
    return mentee_schema.jsonify(new_mentee)


# Assignments
@app.route("/api/assign/<mentee_id>&<mentor_id>", methods=["PUT"])
def assign_mentee(mentee_id, mentor_id):
    """ Assign mentor to mentee """
    mentee = Mentee.query.get(mentee_id)
    mentee.mentor_id = mentor_id
    db.session.commit()
    return mentee_schema.jsonify(mentee)

@app.route("/api/assign/<mentee_id>", methods=["PUT"])
def random_assign(mentee_id):
    """ assign mentee to a free mentor. 
    Priority is given to mentors with lower number of mentees. """
    free_mentors = Mentor.query.filter(Mentor.current < Mentor.met_max)
    chosen = free_mentors.order_by(Mentor.current).first()
    if chosen:
        return assign_mentee(mentee_id, chosen.id)
        # return mentor_schema.jsonify(chosen)
    # return {"msg" : "no free mentors"}

