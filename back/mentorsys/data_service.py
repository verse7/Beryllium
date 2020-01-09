from mentorsys import db
from mentorsys.models import Mentor, Mentee
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

""" 
Code used to pull data from online google sheet to intialize test database
This data is similar to the actual data
"""
scope = [
    "https://spreadsheets.google.com/feeds",
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# ASK ROWAN FOR CREDS FILE -- not tracked in git
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)


# fetch data from sheet
def fetch():
    assignments = client.open("mocksheet").get_worksheet(0)
    mentors = client.open("mocksheet").get_worksheet(1)
    mentees = client.open("mocksheet").get_worksheet(2)

    assignments_recs = assignments.get_all_records()
    mentor_recs = mentors.get_all_records() 
    mentee_recs = mentees.get_all_records()

    # pprint(assignments_recs)
    # pprint(mentor_recs)
    # pprint(mentee_recs)

    return mentor_recs, mentee_recs


# fetch and add to DB
def fetch2db():
    mentors, mentees = fetch()

    # Add Mentor Records
    for rec in mentors:

        # create Mentor record to add to DB
        if rec['MAX'] == "":
            rec['MAX'] = 1
        mentor = Mentor(            
            rec['First Name'],      
            rec['Last Name'],       
            rec['Email Address'],   
            str(rec['Phone Number']),    
            rec['CONTRACT'],        
            rec['CURRENT'],         
            rec['MAX'])
        
        # print(mentor)
        # print("ADDED MENTOR")
        db.session.add(mentor)
    
    # db.session.commit()
    # print("DONE MENTORS")
    
    # ADD Mentee Records
    for rec in mentees:
        # create Mentee record to add to DB
        mentee = Mentee(            
            rec['First Name'],      
            rec['Last Name'],       
            rec['Email Address'],   
            str(rec['Phone Number']),    
            rec['CONTRACT'])
        db.session.add(mentee)
    
    db.session.commit()


""" def reset():
    db.drop_all()
    db.create_all()
    odb =
    db.session. """


# fetch()
fetch2db()
