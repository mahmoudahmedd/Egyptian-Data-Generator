import time
import json
from random import randint

from .date import Date
from .date_time import DateTime
from .helpers import Helpers
from .phone_number import PhoneNumber
from .finance import Finance
from .address import Address
from .name import Name
from .national_identification_number import NationalID

VERSION = "1.0.0"

class EgyptianDataGenerator:
  def __init__(self, _seed = time.time()):
    governorates = {
      "alexandria": "Alexandria",
      "aswan": "Aswan",
      "asyut": "Asyut",
      "beheira": "Beheira",
      "beni_suef": "Beni Suef",
      "cairo": "Cairo",
      "dakahlia": "Dakahlia",
      "damietta": "Damietta",
      "faiyum": "Faiyum",
      "gharbia": "Gharbia",
      "giza": "Giza",
      "ismailia": "Ismailia",
      "kafr_el_sheikh": "Kafr El Sheikh",
      "luxor": "Luxor",
      "marsa_matruh": "Marsa Matruh",
      "menofia": "Menofia",
      "minya": "Minya",
      "new_valley": "New Valley",
      "north_sinai": "North Sinai",
      "port_said": "Port Said",
      "qalyubia": "Qalyubia",
      "qena": "Qena",
      "red_sea": "Red Sea",
      "sharqia": "Sharqia",
      "sohag": "Sohag",
      "south_sinai": "South Sinai",
      "suez": "Suez"
    }
    
    filename = "egyptian_data_generator/data_provider/addresses/all.json"
    with open(filename, 'r+') as dataFile:
      addressesData = json.load(dataFile)
      
    governoratesValues = list(governorates.values())
    governoratesKeys = list(governorates.keys())
      
    self.helpers = Helpers()
    self.date = Date()
    self.dateTime = DateTime()
    self.phoneNumber = PhoneNumber()
    self.finance = Finance()
    self.address = Address(addressesData, governorates, governoratesValues, governoratesKeys)
    self.name = Name()
    self.nationalID = NationalID()
