from flask import jsonify, request, current_app as app
from . import db
from data_fetch import data_worker

@app.route("/", methods=["GET"])
def home():
    """ Home route """
    return jsonify({"msg": "HEY"})

@app.route("/reset", methods=["GET"])
def resetDB():
    """ reset database to match online data """
    data_worker.pull()
    return jsonify({"msg": "database reset"})
