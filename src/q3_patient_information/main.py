from patient import Patient  # importing Patient class
from procedure import Procedure  # importing Procedure class
from prettytable import PrettyTable  # importing prettytable library to print humanized table
from datetime import datetime  # library to manipulate date


def main():
    patient_data = {"first_name": input("Enter first name: "),
                    "middle_name": input("Enter middle name: "),
                    "last_name": input("Enter last name: "),
                    "address": input("Enter address: "),
                    "city": input("Enter city: "),
                    "state": input("Enter state: "),
                    "zip_code": input("Enter ZIP code: "),
                    "phone_number": input("Enter phone number: "),
                    "emergency_contact_name": input("Enter emergency contact name: "),
                    "emergency_contact_number": input("Enter emergency contact number: ")}
    procedure_data = [
        {"name": "Physical Exam",
         "date": f"{datetime.today().strftime('%Y-%m-%d')}",
         "practitioner": "Dr. Irvine",
         "charge": 250.00},
        {"name": "X-ray",
         "date": f"{datetime.today().strftime('%Y-%m-%d')}",
         "practitioner": "Dr. Jamison",
         "charge": 500.00},
        {"name": "Blood test",
         "date": f"{datetime.today().strftime('%Y-%m-%d')}",
         "practitioner": "Dr. Smith",
         "charge": 200.00}
    ]

    patient = Patient(**patient_data)  # sending patient_data and attributes to Patient class
    procedures = [Procedure(**data) for data in procedure_data]  # sending procedure_data and attributes to Procedure class

    patient.display_patient_info()  # Patient class method to display info

    procedure_table = PrettyTable()  # creating an object of PrettyTable library
    procedure_table.align = 'l'  # align mode for the table (l - align to the left)
    procedure_table.field_names = ["Procedure #1", "Procedure #2", "Procedure #3"]  # table headers

    # .add_row - adding rows to the table
    procedure_table.add_row([f"Procedure name: {procedures[0].name}",
                             f"Procedure name: {procedures[1].name}",
                             f"Procedure name: {procedures[2].name}"])
    procedure_table.add_row([f"Date: {procedures[0].date}",
                             f"Date: {procedures[1].date}",
                             f"Date: {procedures[2].date}"])
    procedure_table.add_row([f"Practitioner: {procedures[0].practitioner}",
                             f"Practitioner: {procedures[1].practitioner}",
                             f"Practitioner: {procedures[2].practitioner}"])
    procedure_table.add_row([f"Charge: {procedures[0].charge:.2f}",
                             f"Charge: {procedures[1].charge:.2f}",
                             f"Charge: {procedures[2].charge:.2f}"])

    print(procedure_table)

    total_charges = sum(procedure.charge for procedure in procedures)  # count total charges form the patient
    print(f"Total Charges for all Procedures: {total_charges:.2f}")


if __name__ == "__main__":
    main()
