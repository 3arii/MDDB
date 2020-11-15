import mysql.connector as mysql

# You must install and configure this part according to your own OS's Mysql installation which you can find how-to
# in the README file in the github page. Besides when/if you have created a user that isn't a developer and you
# didn't host it in localhost further configuration is needed refer to MySQL documentation for further reading.

db = mysql.connect(
    host="Put how you have configured your host as",
    user="your username",
    passwd=" your password",
    database="your database name"
)

mddb = db.cursor(buffered=True)

mddb.execute("CREATE DATABASE IF NOT EXISTS mddb")
mddb.execute(
    "CREATE TABLE IF NOT EXISTS patients (name VARCHAR(225),user_name VARCHAR(255))")


# adds new patient with the the given variables in the input.
def addpatient(self, name, age, phone_number, email, illness, doctor_name):

    name = self.name
    age = self.age
    phone_number = self.phone_number
    email = self.email
    illness = self.illness
    doctor_name = self.doctor_name

    name = input("Enter patient name:")
    age = input("Enter patient age:")
    phone_number = input("Enter patient phone number:")
    email = input("Enter patient e-mail:")
    illness = input("Enter the patient illness:")
    doctor_name = input(
        "Enter the name of the doctor in charge of this patient:")

    values = (str.name, str.age, str.phone_number,
              str.email, str.illness, str.doctor_name)

    query = "INSERT INTO patients (name, age, phone_number, email, illness, doctor_name) VALUES (%s, %s, %s, %s, %s, %s )"


def retrievepatients():  # retrieves patients from the patients table

    query = "SELECT * FROM patients"
    mddb.execute(query)
    patientnames = mddb.fetchall()
    return patientnames

    for patients in patientnames:
        print(patients)


def retrievecolumn(column_name):  # retrieve patient by specific matters

    column = input("Enter which attribute you want to search with:")
    query = "SELECT (column) FROM patients (%s)"

    mddb.execute(query)
    columns = mddb.fetchall()

    for column in columns:
        print(column)


def searchbyid(id):  # retrieve by id

    id = input("Enter the id of the patient:")

    query = "SELECT * FROM users WHERE id = (id)(%s)"
    mddb.execute(query)

    records = mddb.fetchall()

    for record in records:
        print(record)


def deletepatient(id):  # deletes patient by id name

    print("Enter the id of the patient(DISCLAIMER: This action is irreversible):")

    query = "DELETE FROM patients WHERE id = (id)(%s)"
    cursor = mddb.execute(query)

    db.commit()

# IMPORTANT TO REMEMBER: This is irreversible so be sure to run the List Patients
# command before commiting to this command


def help():
    print("Add patient: Add a new patient, the steps will be displayed by the program itself\nList Patients: Lists all available patients\nList by attribute: List by given attribute (ex:if you give name as attribute it will list only the names of patients')\nList by id: List by id(the creation order)\nDelete Patient: Deletes a patients by id(DISCLAIMER: Make sure you have the right id because this process is irreversible)) ")


print("Welcome to the Medical Doctor Database made by 3arii!")
user_input = input(
    "Enter your input or type help to see all commands, type command exit to exit:")
user_input = user_input.lower()


if user_input == "help":
    help()

elif user_input == "add patients":
    addpatient()

elif user_input == "list patients":
    retrievepatients()

elif user_input == "list by attribute":
    retrievecolumn()

elif user_input == "list by id":
    searchbyid()

elif user_input == "delete patient":
    deletepatient()

elif user_input == "exit":
    break

else:
    print("Wrong command given user the command help for all the available inputs. Run the program again.")
