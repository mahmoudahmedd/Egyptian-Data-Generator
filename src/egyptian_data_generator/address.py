import json
from egyptian_data_generator.helpers import Helpers


class Address:
    def __init__(self, _addressesData, _governorates, _governoratesValues, _governoratesKeys):
        self.addressesData = _addressesData
        self.governorates = _governorates
        self.governoratesValues = _governoratesValues
        self.governoratesKeys = _governoratesKeys
        self.res = {}
        
    def generate(self, _governorates = None):
        if _governorates is not None:
            temp = {}
            for value in _governorates:
                kay = self.governoratesKeys[self.governoratesValues.index(value)]
                temp[kay] = value
            self.governorates = temp
        
        self.res["governorat"] = Helpers.oneChoice(self.governoratesValues)
        
        key = self.governoratesKeys[self.governoratesValues.index(self.res["governorat"])]
        
        data = self.addressesData[key]
        governoratDate = Helpers.oneChoice(data)
        self.res["zip_code"] = governoratDate["postal_code"]
        self.res["address"] = governoratDate["address"]
        self.res["post_office"] = governoratDate["post_office"]
        self.res["lat"] = governoratDate["lat"]
        self.res["lng"] = governoratDate["lng"]

        firstElement = self.res["address"].split()[0]
        if(firstElement.isnumeric()):
            firstElement = int(firstElement)
            self.res["address"] = str(Helpers.intBetween(firstElement, firstElement + 10)) + self.res["address"][len(str(firstElement)):] + ", " + self.res["governorat"] + ", Egypt"
        else:
            self.res["address"] = str(Helpers.intBetween(1, 10)) + " " + self.res["address"] + ", " + self.res["governorat"] + ", Egypt"
               
        return self.res
        
