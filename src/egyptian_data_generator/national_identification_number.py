import random

from egyptian_data_generator.helpers import Helpers
from egyptian_data_generator.date import Date

class NationalID:
    def generate(self, _dateOfBirth = None, _governorate = None, _gender = None):
        governorates = {
            "Alexandria": "02",
            "Aswan": "28",
            "Asyut": "25",
            "Beheira": "18",
            "Beni Suef": "22",
            "Cairo": "01",
            "Dakahlia": "12",
            "Damietta": "11",
            "Faiyum": "23",
            "Gharbia": "16",
            "Giza": "21",
            "Ismailia": "19",
            "Kafr El Sheikh": "15",
            "Luxor": "29",
            "Marsa Matruh": "33",
            "Menofia": "17",
            "Minya": "24",
            "New Valley": "32",
            "North Sinai": "34",
            "Port Said": "03",
            "Qalyubia": "14",
            "Qena": "27",
            "Red Sea": "31",
            "Sharqia": "13",
            "Sohag": "26",
            "South Sinai": "35",
            "Suez": "04",
            "outside": "88"
        }
        
        
        if _dateOfBirth is None:
            _dateOfBirth = Date.between()
            
        yy = _dateOfBirth.split("-")[0]
        mm = _dateOfBirth.split("-")[1]
        dd = _dateOfBirth.split("-")[2]
        birthCentury = str(int(yy[0]) + 1)
            
        if _governorate is not None:
            govCode = governorates[_governorate]
        else:
            govCode = Helpers.oneChoice(list(governorates.values()))
        
        if _gender is not None:
            if(_gender == "female"):
                genderCode = str(random.randrange(0,10,2))
            else:
                genderCode = str(random.randrange(1,10,2))
        else:
            genderCode = str(random.randrange(0,10))
        
           
        return birthCentury + yy[2:] + mm + dd + govCode + str(random.randrange(100, 1000)) + genderCode + str(random.randrange(1, 10))

        


