from egyptian_data_generator import *
import time
import pymysql



egyDataGen = EgyptianDataGenerator()


# Open database connection
db = pymysql.connect("localhost", "root", "123456", "graduation_project_database")

# prepare a cursor object using cursor() method
cursor = db.cursor()

start = time.time()

for i in range(1, 100):
    phoneNumber = egyDataGen.phoneNumber.generate()["intl_phone_number"]
    name = egyDataGen.name.generate()
    firstName = name["first_name"]
    lastName = name["last_name"]
    gender = name["gender"]
    dateOfBirth = egyDataGen.date.between()

    sql = "INSERT INTO users(phone_number, first_name, last_name, gender, date_of_birth, user_type) \
VALUES ('%s', '%s', '%s', '%s', '%s','%d' )" % \
   (phoneNumber, firstName, lastName, gender, dateOfBirth, 1)
    
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("Error")
        db.rollback()

db.close()

end = time.time()

print(end- start)




