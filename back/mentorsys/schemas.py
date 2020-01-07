# Marshmallow Schemas for models
from mentorsys import ma


class MenteeSchema(ma.ModelSchema):
    class Meta:
        fiels = ('id', 'fname', 'lname', 'email', 'telnum', 'contract', 'mentor_id')


class MentorSchema(ma.ModelSchema):
    class Meta:
        fiels = ('id', 'fname', 'lname', 'email', 'telnum', 'contract', 'current', 'met_max')


mentee_schema = MenteeSchema()
mentees_schema = MenteeSchema(many=True)
mentor_schema = MentorSchema()
mentors_schema = MentorSchema(many=True)