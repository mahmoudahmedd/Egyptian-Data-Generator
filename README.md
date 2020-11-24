[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# Egyptian Data Generator
Generate Egyptian realistic datasets in Python for testing &amp; simulating the customer base.
<hr>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

Suppose you need to generate Egyptian realistic datasets with 100,000 rows to simulate the customer base so it will be complicated because the lack of Egyptian data... Therefore this tool will help you.

The specification:

* address
  * governorat      ("Giza")
  * zip_code        (12551)
  * address         ("54 El cooperation / Urban eastern m .Shortly")
  * post_office     ("Urban East")
  * latitude        (30.0130557)
  * longitude       (31.2088526)
* name
  * first_name      (Mahmoud)
  * last_name       (Ahmed)
  * full_name       (Mahmoud Ahmed)
  * user_name       (mahmoud_ahmed_0)
* NationalID
  * generate        (2541119632960)
* PhoneNumber
  * dialing_code     (+20)
  * provider         (Vodafone)
  * phone_number     (01014856695)
  * intl_phone_number (+201014856695)
* date
  * between         (1997-12-8)
  * recent          (1997-12-8)
* dateTime
  * between         (1997-12-8 11:03)
  * recent          (1997-12-8 11:03)
  * recentUnixTime  (1606251876)
* finance
  * visa13CreditCardNumber 
  * visa16CreditCardNumber
  * mastercardCreditCardNumber
* helpers
  * intBetween
  * oneChoice
  * replaceSymbolWithNumber


## Built With
* [Python 3.8](https://www.python.org/downloads/release/python-380/)
* [NumPy](https://numpy.org/)
* [JSON Data Model](https://www.json.org/json-en.html)

## Usage

```python
from egyptian_data_generator import *
import pymysql

egyDataGen = EgyptianDataGenerator()

db = pymysql.connect("localhost", "username", "password", "database_name")
cursor = db.cursor()

for i in range(1, 100000):
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
        db.rollback()

db.close()
```



<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Mahmoud Ahmed - [Twitter @1243Mahmoud](https://twitter.com/1243Mahmoud) - mahmoud_ahmed@stud.fci-cu.edu.eg

Project Link: [https://github.com/mahmoudahmedd/Egyptian-Data-Generator](https://github.com/mahmoudahmedd/Egyptian-Data-Generator)



<!-- MARKDOWN LINKS & IMAGES -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/mahmoudahmedd/Egyptian-Data-Generator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/mahmoudaahmedd/
