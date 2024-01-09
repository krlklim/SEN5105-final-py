class Patient:

    # initialization Patient attributes
    def __init__(self, first_name,
                 middle_name,
                 last_name,
                 address,
                 city, state,
                 zip_code,
                 phone_number,
                 emergency_contact_name,
                 emergency_contact_number):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_number = emergency_contact_number

    # method to return full name of the patient
    def full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    # method to return full address of the patient
    def full_address(self):
        return f"{self.address}, {self.city}, {self.state}, {self.zip_code}"

    # method to return emergency contact info
    def emergency_contact_info(self):
        return f"{self.emergency_contact_name} - {self.emergency_contact_number}"

    # method to display patient info
    def display_patient_info(self):
        print()
        print("__________________________________________________________________________________")
        print(f"PATIENT INFORMATION:")
        print(f"Name: {self.full_name()}")
        print(f"Address: {self.full_address}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Emergency Contact: {self.emergency_contact_info}")
        print("__________________________________________________________________________________")
        print()
