from mentorsys import app, db
from mentorsys.models import Mentor, Mentee
from flask import jsonify
import mentorsys.data_service

#default home route
@app.route("/", methods=["GET"])
def home():
    return {"msg": "HEY"}

#Get all mentor data
@app.route("/mentors", methods=["GET"])
def get_mentors():
    mentors = Mentor.query.all()
    # print(mentors[0])
    return jsonify(Mentor.Schema(many=True).dump(mentors))

#Get all mentee data
@app.route("/mentees", methods=["GET"])
def get_mentees():
    mentees = Mentee.query.all()
    # print(mentors[0])
    return jsonify(Mentee.Schema(many=True).dump(mentees))

