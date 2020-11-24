import json
from egyptian_data_generator.helpers import Helpers

class Name:
    def generate(self, _gender = None):
        res = {}
        filename = "egyptian_data_generator/data_provider/names/data.json"
        
        if _gender is None:
            _gender = ["male", "female"]
            
        res["gender"] = Helpers.oneChoice(_gender)
        
        with open(filename, 'r+') as dataFile:
            data = json.load(dataFile)
            
            res["first_name"] = Helpers.oneChoice(list(data[res["gender"]]))
            res["last_name"] = Helpers.oneChoice(list(data["male"]))
            res["full_name"] = res["first_name"] + " " + res["last_name"]
            res["user_name"] = res["first_name"] + "_" + res["last_name"] + str(Helpers.intBetween(0, 99999)) + "_" + str(Helpers.intBetween(0, 99999))
        
        return res
        
