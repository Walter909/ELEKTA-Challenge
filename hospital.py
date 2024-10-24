# Online Python - IDE, Editor, Compiler, Interpreter

"""
 Notes:
 - Treated "unspecified" as a default diagnosis so only delete "unspecified" diagnosis
 - Big O - n2 (main function)

 Artificial constraints:
 - Numbers for selecting opertaions 1, 2, 3, 4
 - Attributes type constraints: name letters only, age numbers only etc

 Areas for improvements:
 - Not case sensitive ex: u only not U
 - ID generation could be more secured
 - Contacts information could be encrypted

 """

class Patient():
    def __init__(self, id, name, age, gender, contacts, diagnosis="unspecified"):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.contacts = contacts
        self.diagnosis = diagnosis
        self.assign_physician()

    def assign_physician(self):
        if self.diagnosis == "breast" or self.diagnosis == "lung":
            self.physician = "Dr. Susan Jones"
            self.department = "J"
        else:
            self.physician = "Dr. Ben Smith"
            self.department = "S"

    def __str__(self):
        return f"id: {self.id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, " \
               f"Contacts: {self.contacts}, Diagnosis: {self.diagnosis}, " \
               f"Physician: {self.physician}, Department: {self.department} "


def adding_contacts():
    friends = []
    while True:
        contacts = input()
        if contacts == "D":
            break
        else:
            contact = contacts.split(" ")

            if len(contact) == 2 and contact[0].isalpha() and contact[1].isnumeric():
                friends.append((contact[0], contact[1]))
            else:
                print("Please enter a valid contact ex:John 123")

    return friends


def add_patient(id, hospital):
    # Collect info from user
    print("Please enter the patient Name (A-Z): ")
    while True:
        name = input()
        if name.isalpha() == False:
            print("Please enter a valid name (A-Z)")
        else:
            break

    print("Please enter the patient Age (Numbers 0-200): ")
    while True:
        age = input()
        if age.isnumeric() == False or int(age) < 0 or int(age) > 200:
            print("Please a valid age (Numbers 0-200)")
        else:
            break

    print("Please enter the patient Gender (M or F): ")
    while True:
        gender = input()
        if gender != "M" and gender != "F":
            print("Please enter a valid gender (M or F)")
        else:
            break

    print("Please enter the patient Contacts (Name Phone#) / Press D when done: ")
    friends = adding_contacts()

    print("Please enter the patient Diagnosis (unspecified, lung, breast or prostate): ")
    while True:
        diagnosis = input()
        if diagnosis != "lung" and diagnosis != "breast" and \
                diagnosis != "prostate" and diagnosis != "unspecified":
            print("Please enter a valid diagnosis: (unspecified, lung, breast or prostate)")
        else:
            break

    hospital[str(id)] = Patient(str(id), name, age, gender, friends, diagnosis)


def update_patient(medicalid, hospital):
    #Updating patient info
    try:
        p = hospital[medicalid]
        print(f"Current patient being changed\n {p}")
        print(f"What attribute of patient with id={medicalid} would you like to update?")
        while True:
            attribute = input()
            if attribute == "n" or attribute == "a" or attribute == "g" or attribute == "c" or \
                    attribute == "d":
                break
            else:
                print("Please enter a modifiable attribute ex: n - Name, a - Age, g - Gender, c - Contacts,"
                      " d - Diagnosis")

        print("Please enter the new value: ")
        while attribute == "n":
            newValue = input()
            if newValue.isalpha():
                p.name = newValue
                break
            else:
                print("Please enter a valid Name (letters)")

        while attribute == "a":
            newValue = input()
            if newValue.isnumeric():
                p.age = newValue
                break
            else:
                print("Please enter a valid Age (0-200)")

        while attribute == "g":
            newValue = input()
            if newValue == "M" or newValue == "F":
                p.gender = newValue
                break
            else:
                print("Please enter a valid gender (M or F)")

        while attribute == "d":
            newValue = input()
            if newValue == "unspecified" or newValue == "lung" or newValue == "breast"\
                    or newValue == "prostate":
                p.diagnosis = newValue
                p.assign_physician()
                break
            else:
                print("Please enter a valid diagnosis (unspecified, lung, breast or prostate)")

        if attribute == "c":
            p.contacts += adding_contacts()

        print(f"Success your patient record has been successfully update!\n {p}")
    except KeyError:
        print(f"I apologize that patient with medical id={medicalid} does not exist please try again")


def delete_patient(medicalid, hospital):
    #Deleting a patient record
    try:
        p = hospital[medicalid]
        if p.diagnosis != "unspecified":
            print(f"Sorry patient record {medicalid} already has a diagnosis and cannot be deleted")
            return
        else:
            hospital.pop(medicalid)
            print(f"Success you have deleted the patient with the medical id={medicalid} from your records")
        print(p)
    except KeyError:
        print(f"I apologize that patient with medical id={medicalid} does not exist please try again")


def main():
    hospital = {}
    id = 0
    while True:
        # Request action type:
        print("Welcome what would you like to do today: 1,2,3,4 - add, update, delete, done")
        start = input()
        if start == "1":
            # Adding Patient to Hospital Registry
            add_patient(id, hospital)
            id += 1
        elif start == "2":
            # Updating Patient in Hospital Registry by medicalId
            print("Please enter the medicalId record you would like to update")
            print(hospital)
            medicalid = input()
            update_patient(medicalid, hospital)
        elif start == "3":
            # Deleting Patient in Hospital Registry
            print("Please enter the patient medicalId record you would like to delete")
            medicalid = input()
            delete_patient(medicalid, hospital)
        elif start == "4":
            break

main()
