from patient import Patient
from procedure import Procedure
from prettytable import PrettyTable
from datetime import datetime


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

    patient = Patient(**patient_data)
    procedures = [Procedure(**data) for data in procedure_data]

    patient.display_patient_info()

    procedure_table = PrettyTable()
    procedure_table.align = 'l'
    procedure_table.field_names = ["Procedure #1", "Procedure #2", "Procedure #3"]
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

    total_charges = sum(procedure.charge for procedure in procedures)
    print(f"Total Charges for all Procedures: {total_charges:.2f}")


if __name__ == "__main__":
    main()
