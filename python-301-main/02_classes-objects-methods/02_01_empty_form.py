# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.

import random
class PatientForm():

    def __init__(self, name, age, email, birth_date, phone_number, insurer):
        self.name = name
        self.age = age
        self.email = email
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.insurer = insurer
        self.patient_id = random.randint(1, 1000)

    def empty_field(self):
        print(f"""Please fill out the below fields: 
        Name: 
        Age: 
        Email: 
        Birthdate: 
        Phone Number: 
        Insurer Name: """)
        print()

    def completed_field(self):
        print(f"""Thank you {self.name.title()}, our records show: 
        ID: {self.patient_id}
        Age: {self.age}
        Email: {self.email}
        Birthdate: {self.birth_date}
        Phone Number: {self.phone_number}
        Insurer: {self.insurer}
        
        If there are no issues, your information will be saved in our records.""")

p1 = PatientForm()