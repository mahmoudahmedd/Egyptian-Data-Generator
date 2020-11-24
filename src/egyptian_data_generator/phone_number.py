from egyptian_data_generator.helpers import Helpers


class PhoneNumber:
    def generate(self):
        res = {}
        providers = {
          "Vodafone": "100",
          "Etisalat": "111",
          "Orange": "122",
          "Etisalat": "114",
          "Orange": "120",
          "Vodafone": "101",
          "Etisalat": "112",
          "Vodafone": "106",
          "Orange": "127",
          "Orange": "128",
          "Vodafone": "109"
        }
        
        res["dialing_code"] = "+20"
        res["provider"] = Helpers.oneChoice(list(providers.values()))
        res["phone_number"] = "0" + res["provider"] + Helpers.replaceSymbolWithNumber("#######")
        res["intl_phone_number"] = res["dialing_code"] + res["phone_number"][1:]

        res["provider"] = list(providers.keys())[list(providers.values()).index(res["provider"])]
        return res
        


