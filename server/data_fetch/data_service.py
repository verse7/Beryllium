from application import db
from application.models import Mentor, Mentee
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

class DataFetcher():
    """ fetches data from online spreadsheet """

    def __init__(self):
        pass

    # fetch data from sheet
    def fetch(self):
        assignments = client.open("mocksheet").get_worksheet(0)
        mentors = client.open("mocksheet").get_worksheet(1)
        mentees = client.open("mocksheet").get_worksheet(2)

        assignments_recs = assignments.get_all_records()
        mentor_recs = mentors.get_all_records() 
        mentee_recs = mentees.get_all_records()

        return mentor_recs, mentee_recs


    # fetch and add to DB
    def pull(self):
        mentors, mentees = self.fetch()

        # wipe database
        db.drop_all()
        db.create_all()

        # add records to tables
        self.addMentors(mentors)
        self.addMentees(mentees)

        # commit changes
        db.session.commit()

    
    def addMentors(self, mentors):
        """ Add Mentor Records to db """
        mentor_list = []
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
                rec['MAX']
            )
            mentor_list.append(mentor)
            
        db.session.add_all(mentor_list)

    def addMentees(self, mentees):
        """ ADD Mentee Records """
        mentee_list = []
        for rec in mentees:
            # create Mentee record to add to DB
            mentee = Mentee(            
                rec['First Name'],      
                rec['Last Name'],       
                rec['Email Address'],   
                str(rec['Phone Number']),    
                rec['CONTRACT']
            )

            mentee_list.append(mentee)
        db.session.add_all(mentee_list)
